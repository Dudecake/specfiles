#!/bin/bash

set -e
if [[ ! -d golang-helm-3/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/golang-helm-3.git --branch rawhide --single-branch
else
  pushd ./golang-helm-3 > /dev/null
  git pull
  popd > /dev/null
fi
spectool -g ./golang-helm-3/golang-helm-3.spec -C golang-helm-3
rpmbuild -bs ./golang-helm-3/golang-helm-3.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/golang-helm-3"
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
fi
