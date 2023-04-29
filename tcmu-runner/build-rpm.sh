#!/bin/sh

PKG=tcmu-runner
BRANCH=c9s-sig-storage-gluster-9
set -e

../fetch-centos-pkg.sh ${PKG} ${BRANCH}

exec ../build-rpm.sh "$@"
