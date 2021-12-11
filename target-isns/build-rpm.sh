#!/bin/bash

set -e
if [[ ! -d target-isns/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/target-isns.git --branch rawhide --single-branch
else
  pushd ./target-isns > /dev/null
  git pull
  popd > /dev/null
fi
sed -i 's/\.tar\.gz/\.tar\.xz/g' ./target-isns/target-isns.spec
spectool -g ./target-isns/target-isns.spec -C target-isns
rpmbuild -bs ./target-isns/target-isns.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/target-isns"
RPM_FILE=$(rpm -q ./*.src.rpm --qf '%{name}-%{version}-%{release}.%{arch}.rpm\n')
ARCH="$(uname -m)"
if [[ ! -f "${2}/${ARCH}/os/${RPM_FILE}" ]]; then
  dnf builddep ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
fi
