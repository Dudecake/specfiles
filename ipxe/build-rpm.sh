#!/bin/sh

set -e
dnf download --repofrompath ipxe,https://download.opensuse.org/tumbleweed/repo/src-oss/ --repo ipxe --source ipxe
bsdtar -xf ipxe-*.src.rpm
sed "s/__release/$(rpm -q ipxe-*.src.rpm --qf '%{release}'/)" ./ipxe.spec.patch.in > ./ipxe.spec.patch
patch < ./ipxe.spec.patch
sed -i 's/%{gcc_version}/12/g' ./ipxe.spec
if [[ -z "$(rpm -E '%{?suse_version}')" ]]; then
  for arch in aarch64 x86_64; do
    for item in $(find /usr/bin -maxdepth 1 -type f -name ${arch}\*-linux-\*); do
      ln -sf ${item} /usr/local/bin/${arch}-suse-linux-${item##*linux-}
    done
  done
fi
exec ../build-rpm.sh "$@"
