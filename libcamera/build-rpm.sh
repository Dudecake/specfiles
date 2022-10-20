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
ln -s ./${PKG}/${PKG}.spec

exec ../build-rpm.sh "$@"
