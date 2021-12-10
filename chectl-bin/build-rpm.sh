#!/bin/bash

MACHINE="$(uname -m)"
BASEARCH="${MACHINE}"
[[ "${MACHINE}" = "x86_64" ]] && BASEARCH="x64"
[[ "${MACHINE}" = "aarch64" ]] && BASEARCH="arm64"
BASEARCH=${BASEARCH} envsubst < ./chectl-bin.spec.in > ./chectl-bin.spec
spectool -g ./chectl-bin.spec
rpmbuild -bs ./chectl-bin.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(rpm -q ./*.src.rpm --qf '%{name}-%{version}-%{release}.%{arch}.rpm\n')
if [[ ! -f "${2}/${ARCH}/os/${RPM_FILE}" ]]; then
  exec rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
fi
