#!/bin/bash

PKG=libntirpc
set -e
if [[ ! -d ${PKG}/.git ]]; then
  git clone https://git.centos.org/rpms/${PKG}.git --branch c8s-sig-storage-nfs-ganesha-4 --single-branch
else
  pushd ./${PKG} > /dev/null
  git pull
  popd > /dev/null
fi
spectool -g ./${PKG}/SPECS/${PKG}.spec -C ${PKG}/SOURCES
rpmbuild -bs ./${PKG}/SPECS/${PKG}.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/${PKG}/SOURCES"
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
