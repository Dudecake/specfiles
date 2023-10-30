#!/bin/bash

ARCH="$(rpm -E '%_arch')"
BUILDDIR="${BUILDDIR:-${PWD}/target}"
RESULTDIR="${RESULTDIR:-${PWD}/repo}"
. /etc/os-release

set -e
REPO="--disablerepo build-noarch,build-${ARCH} --setopt=previous.priority=100"
KERNEL_BASE=kernel
case "${ID}" in
  fedora)
    if [[ "${VERSION_ID}" = "rawhide" ]]; then
      REPO="${REPO} --repo fedora,updates"
      RELEASEVER="--releasever $((${VERSION_ID} - 1))"
    fi
    KERNEL="${KERNEL_BASE}-devel-matched"
    KERNEL_MODULES="${KERNEL_BASE}-modules-core"
    ;&
  centos)
    KERNEL="${KERNEL} ${KERNEL_BASE} ${KERNEL_BASE}-core ${KERNEL_BASE}-devel"
    KERNEL_HEADERS="${KERNEL_BASE}-headers"
    KERNEL_MODULES="${KERNEL_MODULES} ${KERNEL_BASE}-modules ${KERNEL_BASE}-modules-extra"
    ;;
  opensuse*)
    KERNEL_BASE=kernel-default
    [[ "$(rpm -E %_arch)" = "aarch64" ]] || KERNEL_VERSION="-$(dnf list zfs-kmp-default.$(rpm -E %_arch) --repofrompath filesystems,https://download.opensuse.org/repositories/filesystems/openSUSE_Tumbleweed --repo filesystems | grep -Po '(?<=_k)\d+\.\d+\.\d+')"
    KERNEL="${KERNEL_BASE} ${KERNEL_BASE}-base ${KERNEL_BASE}-devel ${KERNEL_BASE}-devel"
    ;;
esac
dnf download ${KERNEL} ${KERNEL_HEADERS} ${KERNEL_MODULES} ${REPO} ${RELEASEVER} --downloaddir "${BUILDDIR}/${ARCH}"
createrepo --update "${BUILDDIR}/${ARCH}"
dnf install -y ${KERNEL_BASE} kernel-devel
