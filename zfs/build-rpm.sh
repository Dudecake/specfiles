#!/bin/bash

MACHINE="$(uname -m)"
ZFS_VERSION="2.1.1"

if [[ ! -f "${3}/${ARCH}/os/zfs-${ZFS_VERSION}-1.${MACHINE}.*.rpm" ]]; then
  curl -L https://github.com/openzfs/zfs/releases/download/zfs-${ZFS_VERSION}/zfs-${ZFS_VERSION}.tar.gz | tar -xzf -
  pushd zfs-${ZFS_VERSION} > /dev/null
  ./configure
  make -j1 srpm
  popd > /dev/null
  exec mock -r "${1}-${MACHINE}" rebuild ./zfs-${ZFS_VERSION}/zfs*.src.rpm --resultdir "${2}"
fi
