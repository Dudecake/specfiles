#!/bin/sh

set -e
dnf download --repofrompath ipxe,https://download.opensuse.org/tumbleweed/repo/src-oss/ --repo ipxe --source ipxe
srcrpm=ipxe-*.src.rpm
bsdtar -xf ${srcrpm}
release="$(rpm -q ${srcrpm} --qf '%{release}')"
new_release=$(perl -e "print ${release} + 1")
sed "s/__release__/${release}/; s/__new_release__/${new_release}/" ./ipxe.spec.patch.in > ./ipxe.spec.patch
patch < ./ipxe.spec.patch
sed -i "s/%{gcc_version}/$(rpm -q gcc --qf '%{version}')/g" ./ipxe.spec
if [[ -z "$(rpm -E '%{?suse_version}')" ]]; then
  for arch in aarch64 x86_64; do
    for item in $(find /usr/bin -maxdepth 1 -type f -name ${arch}\*-linux-\*); do
      ln -sf ${item} /usr/local/bin/${arch}-suse-linux-${item##*linux-}
    done
  done
fi
rm ${srcrpm}
exec ../build-rpm.sh "$@"
