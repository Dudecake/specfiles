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
    [[ "${VERSION_ID}" = "rawhide" ]] && REPO="${REPO} --repo fedora,updates"
    KERNEL="${KERNEL_BASE}-devel-matched"
    KERNEL_MODULES="${KERNEL_BASE}-modules-core"
    ;&
  centos)
    KERNEL_VERSION="-$(dnf provides 'kernel(__skb_flow_dissect) = 0x73874cd8' | grep -Po '(?<=kernel-core-)\d\.\d+\.\d+-\d+' | sort | tail -n1)$(rpm -E '%{?dist}')"
    [[ "${KERNEL_VERSION}" = "-$(rpm -E '%{?dist}')" ]] && KERNEL_VERSION=""
    KERNEL="${KERNEL} ${KERNEL_BASE}${KERNEL_VERSION} ${KERNEL_BASE}-core${KERNEL_VERSION} ${KERNEL_BASE}-devel${KERNEL_VERSION}"
    KERNEL_HEADERS="${KERNEL_BASE}-headers${KERNEL_VERSION}.${ARCH}"
    KERNEL_MODULES="${KERNEL_MODULES} ${KERNEL_BASE}-modules${KERNEL_VERSION} ${KERNEL_BASE}-modules-extra${KERNEL_VERSION}"
    ;;
  opensuse*)
    KERNEL_BASE=kernel-default
    [[ "$(rpm -E %_arch)" = "aarch64" ]] || KERNEL_VERSION="-$(dnf list zfs-kmp-default.$(rpm -E %_arch) --repofrompath filesystems,https://download.opensuse.org/repositories/filesystems/openSUSE_Tumbleweed --repo filesystems | grep -Po '(?<=_k)\d+\.\d+\.\d+')"
    KERNEL="${KERNEL_BASE} ${KERNEL_BASE}-base ${KERNEL_BASE}-devel ${KERNEL_BASE}-devel"
    ;;
esac
dnf download ${KERNEL} ${KERNEL_HEADERS} ${KERNEL_MODULES} ${REPO} --releasever ${RELEASEVER} --downloaddir "${BUILDDIR}/${ARCH}"
createrepo --update "${BUILDDIR}/${ARCH}"
dnf install -y ${KERNEL_BASE}${KERNEL_VERSION} kernel-devel${KERNEL_VERSION}
