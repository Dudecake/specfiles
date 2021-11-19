#!/bin/bash

MACHINE="$(uname -m)"
ZFS_VERSION="2.1.1-1"

if [[ ! -f "${3}/${ARCH}/os/zfs-${ZFS_VERSION}.${MACHINE}.*.rpm" ]]; then
  curl -L --remote-name-all http://download.zfsonlinux.org/fedora/34/SRPMS/zfs{,-dkms}-${ZFS_VERSION}.fc34.src.rpm
  exec mock -r "${1}-${MACHINE}" rebuild ./*.src.rpm --resultdir "${2}"
fi
