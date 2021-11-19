#!/bin/bash

if [[ ! -d golang-helm-3/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/golang-helm-3.git --branch rawhide --single-branch
else
  pushd ./golang-helm-3 > /dev/null
  git pull
  popd > /dev/null
fi
spectool -g ./golang-helm-3/golang-helm-3.spec -C golang-helm-3
rpmbuild -bs ./golang-helm-3/golang-helm-3.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/golang-helm-3"
RPM_FILE=$(rpm -q ./*.src.rpm --qf '%{name}-%{version}-%{release}.%{arch}.rpm\n')
if [[ ! -f "${3}/${ARCH}/os/${RPM_FILE}" ]]; then
    exec mock -r "${1}-${ARCH}" rebuild ./*.src.rpm --resultdir "${2}"
fi
