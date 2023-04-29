#!/bin/bash

PKG=golang-helm-3
BRANCH=rawhide
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}

exec ../build-rpm.sh "$@"
