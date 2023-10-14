#!/bin/bash

PKG=light
BRANCH=f38
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}

exec ../build-rpm.sh "$@"
