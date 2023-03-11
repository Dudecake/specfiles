#!/bin/sh

KVER="$(rpm -q kernel-devel --qf '%{version}-%{release}\n')"
sed "s/\${KVER}/${KVER}/" ./kmod-vendor-reset.spec.in > ./kmod-vendor-reset.spec
exec ../build-rpm.sh "$@"
