#!/bin/bash

set -e

VERSION="0.5.2"

tarball="$(rpm -E %{_sourcedir}/boringtun-cli-${VERSION}.tar.gz)"
curl -L https://github.com/cloudflare/boringtun/archive/refs/tags/boringtun-cli-${VERSION}.tar.gz -o "${tarball}"
bsdtar -xf "${tarball}"
pushd boringtun-boringtun-cli-${VERSION} > /dev/null
dnf install -y cargo
cargo vendor
bsdtar -cf ../vendor.tar.zst vendor
popd > /dev/null
sed "s/\${VERSION}/${VERSION}/" ./boringtun-cli.spec.in > ./boringtun-cli.spec
exec ../build-rpm.sh "$@"
