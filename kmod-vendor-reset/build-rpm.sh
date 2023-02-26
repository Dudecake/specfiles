#!/bin/sh

KVER="$(rpm -q ../zfs/kernel-core-*.rpm --qf '%{version}-%{release}\n')" envsubst < ./kmod-vendor-reset.spec.in > ./kmod-vendor-reset.spec
exec ../build-rpm.sh "$@"
