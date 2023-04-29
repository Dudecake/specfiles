#!/bin/bash

PKG=sbsigntools
BRANCH=rawhide
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}
ln -sf sbsigntools-gnuefi-centos.patch sbsigntools-gnuefi.patch
./${PKG}-mktarball.sh

exec ../build-rpm.sh "$@"
