#!/bin/bash

MACHINE="$(uname -m)"
BASEARCH="${MACHINE}"
[[ "${MACHINE}" = "x86_64" ]] && BASEARCH="x64"
[[ "${MACHINE}" = "aarch64" ]] && BASEARCH="arm64"
BASEARCH=${BASEARCH} envsubst < ./chectl-bin.spec.in > ./chectl-bin.spec
spectool -g ./chectl-bin.spec
rpmbuild -bs ./chectl-bin.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(rpm -q ./*.src.rpm --qf '%{name}-%{version}-%{release}.%{arch}.rpm\n')
if [[ ! -f "${3}/${ARCH}/os/${RPM_FILE}" ]]; then
  exec mock -r "${1}-$(uname -m)" rebuild ./*.src.rpm --resultdir "${2}"
fi
