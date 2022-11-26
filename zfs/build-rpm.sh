#!/bin/bash

MACHINE="$(uname -m)"
KERNEL_VERSION="$(rpm -q --qf %{version}-%{release}.%{arch} kernel)"
ZFS_VERSION="2.1.6"

if [[ ! -f "${2}/${MACHINE}/os/kmod-zfs-${KERNEL_VERSION}-${ZFS_VERSION}-1*.${MACHINE}.rpm" ]]; then
  curl -sSL https://github.com/openzfs/zfs/releases/download/zfs-${ZFS_VERSION}/zfs-${ZFS_VERSION}.tar.gz | tar -xzf -
  pushd zfs-${ZFS_VERSION} > /dev/null
  dnf install -y --skip-broken epel-release gcc make autoconf automake libtool rpm-build libtirpc-devel libblkid-devel libuuid-devel libudev-devel openssl-devel zlib-devel libaio-devel libattr-devel elfutils-libelf-devel python3 python3-devel python3-setuptools python3-cffi libffi-devel git ncompress libcurl-devel
  [[ "${VERSION_ID}" = "rawhide" ]] && RELEASEVER="--releasever=37 --disablerepo=* --enablerepo=fedora --enablerepo=updates"
  dnf install -y kernel-devel ${RELEASEVER}
  ./configure
  make -j1 srpm
  popd > /dev/null
  rpmbuild --rebuild ./zfs-${ZFS_VERSION}/*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  dnf download kernel kernel-core kernel-devel kernel-headers kernel-modules kernel-modules-extra ${RELEASEVER}
  mv ./zfs-${ZFS_VERSION}/*.src.rpm ./kernel*.rpm "${1}"
else
  rm ./*.src.rpm
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
