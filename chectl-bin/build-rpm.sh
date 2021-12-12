#!/bin/bash

MACHINE="$(uname -m)"
BASEARCH="${MACHINE}"
[[ "${MACHINE}" = "x86_64" ]] && BASEARCH="x64"
[[ "${MACHINE}" = "aarch64" ]] && BASEARCH="arm64"
BASEARCH=${BASEARCH} envsubst < ./chectl-bin.spec.in > ./chectl-bin.spec
spectool -g ./chectl-bin.spec
rpmbuild -bs ./chectl-bin.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
else
  echo "No rebuild neccesary for package $(dirname $PWD/.)" >&2
fi
