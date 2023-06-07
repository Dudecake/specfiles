#!/bin/bash

MACHINE="$(rpm -E '%_arch')"
KERNEL_VERSION="$(rpm -q --qf %{version}-%{release}.%{arch} kernel-devel)"
ZFS_VERSION="2.1.12"
REL="1$(rpm -E '%dist')"

if [[ ! -x "${FORCE_REBUILD}" || ! -f "${2}/${MACHINE}/os/kmod-zfs-${KERNEL_VERSION}-${ZFS_VERSION}-${REL}.${MACHINE}.rpm" ]]; then
  curl -sSL https://github.com/openzfs/zfs/releases/download/zfs-${ZFS_VERSION}/zfs-${ZFS_VERSION}.tar.gz | tar -xzf -
  dnf install -y --skip-broken epel-release gcc make autoconf automake libtool rpm-build libtirpc-devel libblkid-devel libuuid-devel libudev-devel openssl-devel zlib-devel libaio-devel libattr-devel elfutils-libelf-devel python3 python3-devel python3-setuptools python3-cffi libffi-devel git ncompress libcurl-devel --enablerepo crb
  dnf install -y --skip-broken --enablerepo=epel --enablerepo=powertools python3-packaging dkms -x kernel\*
  pushd zfs-${ZFS_VERSION} > /dev/null
  ./configure
  make -j1 srpm
  popd > /dev/null
  if [[ ! -f "${2}/${MACHINE}/os/zfs-${ZFS_VERSION}-${REL}.${MACHINE}.rpm" ]]; then
    rpmbuild --rebuild ./zfs-${ZFS_VERSION}/zfs{,-dkms}-${ZFS_VERSION}-${REL}.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  fi
  rpmbuild --rebuild ./zfs-${ZFS_VERSION}/zfs-kmod-${ZFS_VERSION}-${REL}.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./zfs-${ZFS_VERSION}/*.src.rpm "${1}/source"
else
  rm ./*.src.rpm
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
