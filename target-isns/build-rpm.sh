#!/bin/bash

PKG=target-isns
BRANCH=rawhide
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}

sed -i 's/\.tar\.gz/\.tar\.xz/g' ./${PKG}/${PKG}.spec

exec ../build-rpm.sh "$@"
