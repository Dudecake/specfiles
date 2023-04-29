#!/bin/bash

PKG=libcamera
BRANCH=rawhide
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}
# HASH="030e6f389e2d0fa3f10a47634f3609378ccaf70e"
# SHORT_HASH="${HASH:0:7}"
# pushd ./${PKG}-code > /dev/null
# git archive --remote=https://git.libcamera.org/libcamera/libcamera.git master --format=tar --prefix=${PKG}-${SHORT_HASH}/ ${SHORT_HASH} | xz > ../${PKG}/${PKG}-${SHORT_HASH}.tar.xz
# popd > /dev/null
# sed -i "s/%global commit .*/%global commit ${HASH}/; s/%global commitdate .*/%global commitdate 20211228/" ${PKG}/${PKG}.spec
set +e
ln -s ./${PKG}/* ./

exec ../build-rpm.sh "$@"
