#!/bin/bash

MACHINE="$(uname -m)"
BASEARCH="${MACHINE}"
[[ "${BASEARCH}" == "x86_64" ]]&& BASEARCH="amd64"
[[ "${BASEARCH}" == "aarch64" ]] && BASEARCH="arm64"

set -e
BASEARCH="${BASEARCH}" envsubst <./helm-bin.spec.in > ./helm-bin.spec
spectool -g ./helm-bin.spec
rpmbuild -bs ./helm-bin.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(rpm -q ./*.src.rpm --qf '%{name}-%{version}-%{release}.%{arch}.rpm\n')
if [[ ! -f "${3}/${ARCH}/os/${RPM_FILE}" ]]; then
  exec mock -r "${1}-$(uname -m)" rebuild ./*.src.rpm --resultdir "${2}"
fi
