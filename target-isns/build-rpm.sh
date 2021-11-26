#!/bin/bash

set -e
if [[ ! -d target-isns/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/target-isns.git --branch rawhide --single-branch
else
  pushd ./target-isns > /dev/null
  git pull
  popd > /dev/null
fi
spectool -g ./target-isns/target-isns.spec -C target-isns
rpmbuild -bs ./target-isns/target-isns.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/target-isns"
RPM_FILE=$(rpm -q ./*.src.rpm --qf '%{name}-%{version}-%{release}.%{arch}.rpm\n')
ARCH="$(uname -m)"
if [[ ! -f "${3}/${ARCH}/os/${RPM_FILE}" ]]; then
  exec mock -r "${1}-${ARCH}" rebuild ./*.src.rpm --resultdir "${2}"
fi
