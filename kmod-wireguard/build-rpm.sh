#!/bin/sh

PKG=kmod-wireguard
BRANCH=c8s-sig-kmods
set -e

../fetch-centos-pkg.sh ${PKG} ${BRANCH}

KERNEL_VERSION="$(rpm -q --qf %{version}-%{release} kernel-devel)"

sed -i "s/kernel_version .\+/kernel-version ${KERNEL_VERSION}/" ./${PKG}.spec

exec ../build-rpm.sh "$@"
