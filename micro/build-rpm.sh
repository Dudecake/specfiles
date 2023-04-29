#!/bin/bash

PKG=micro
BRANCH=f37
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}

exec ../build-rpm.sh "$@"
