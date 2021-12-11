#!/bin/bash

MACHINE="$(uname -m)"
ZFS_VERSION="2.1.1"

if [[ ! -f "${2}/${ARCH}/os/zfs-${ZFS_VERSION}-1.${MACHINE}.*.rpm" ]]; then
  curl -L https://github.com/openzfs/zfs/releases/download/zfs-${ZFS_VERSION}/zfs-${ZFS_VERSION}.tar.gz | tar -xzf -
  pushd zfs-${ZFS_VERSION} > /dev/null
  PYTHON=/usr/bin/python3.9 ./configure
  make -j1 srpm
  popd > /dev/null
  dnf builddep ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
fi
