#!/bin/bash

MACHINE="$(uname -m)"
BASEARCH="${MACHINE}"
[[ "${BASEARCH}" == "x86_64" ]]&& BASEARCH="amd64"
[[ "${BASEARCH}" == "aarch64" ]] && BASEARCH="arm64"

set -e
BASEARCH="${BASEARCH}" envsubst <./helm-bin.spec.in > ./helm-bin.spec
spectool -g ./helm-bin.spec
rpmbuild -bs ./helm-bin.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
fi
