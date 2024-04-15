#!/bin/bash

PKG=pop-icon-theme
BRANCH=rawhide
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}

exec ../build-rpm.sh "$@"
