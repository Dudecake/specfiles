#!/bin/bash

MACHINE="$(uname -m)"
ZFS_VERSION="2.1.2"

if [[ ! -f "${2}/${ARCH}/os/zfs-${ZFS_VERSION}-1.${MACHINE}.*.rpm" ]]; then
  curl -L https://github.com/openzfs/zfs/releases/download/zfs-${ZFS_VERSION}/zfs-${ZFS_VERSION}.tar.gz | tar -xzf -
  pushd zfs-${ZFS_VERSION} > /dev/null
  ./configure
  make -j1 srpm
  popd > /dev/null
  rpmbuild --rebuild ./zfs-${ZFS_VERSION}/*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./zfs-${ZFS_VERSION}/*.src.rpm "${1}"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
