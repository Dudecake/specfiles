#!/bin/bash

PKG=libcamera
set -e
if [[ ! -d ${PKG}/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/${PKG}.git --branch rawhide --depth=1
  # git clone https://git.libcamera.org/libcamera/libcamera.git --branch master --depth=1 ${PKG}-code
else
  pushd ./${PKG} > /dev/null
  git pull
  popd > /dev/null
fi
# HASH="030e6f389e2d0fa3f10a47634f3609378ccaf70e"
# SHORT_HASH="${HASH:0:7}"
# pushd ./${PKG}-code > /dev/null
# git archive --remote=https://git.libcamera.org/libcamera/libcamera.git master --format=tar --prefix=${PKG}-${SHORT_HASH}/ ${SHORT_HASH} | xz > ../${PKG}/${PKG}-${SHORT_HASH}.tar.xz
# popd > /dev/null
# sed -i "s/%global commit .*/%global commit ${HASH}/; s/%global commitdate .*/%global commitdate 20211228/" ${PKG}/${PKG}.spec

spectool -g ./${PKG}/${PKG}.spec -C ${PKG}
rpmbuild -bs ./${PKG}/${PKG}.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/${PKG}"
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
else
  rm ./*.src.rpm
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
