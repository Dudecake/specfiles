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
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
else
  rm ./*.src.rpm
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
