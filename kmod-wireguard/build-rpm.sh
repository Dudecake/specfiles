#!/bin/bash

branch=c8-sig-kmods
rpm -qi centos-stream-release > /dev/null
[[ 0 -eq $? ]] && branch=c8s-sig-kmods
PKG=kmod-wireguard
set -e
if [[ ! -d ${PKG}/.git ]]; then
  git clone https://git.centos.org/rpms/${PKG}.git --branch ${branch} --single-branch
else
  pushd ./${PKG} > /dev/null
  git pull
  popd > /dev/null
fi
sed -i "s/4.18.0-348.el8/$(rpm -q --qf '%{version}-%{release}\n' kernel)/" ./${PKG}/SPECS/${PKG}.spec 
spectool -g ./${PKG}/SPECS/${PKG}.spec -C ${PKG}
rpmbuild -bs ./${PKG}/SPECS/${PKG}.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/${PKG}"
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
