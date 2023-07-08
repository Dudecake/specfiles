#!/bin/sh

set -e
curl -L https://download.opensuse.org/repositories/openSUSE:/Factory/standard/src/ipxe-1.21.1+git20230120.a99e435c-2.3.src.rpm | bsdtar -xf -
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
