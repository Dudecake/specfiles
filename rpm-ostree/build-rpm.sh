#!/bin/sh

PKG=rpm-ostree
BRANCH=rawhide
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}

exec ../build-rpm.sh "$@"
