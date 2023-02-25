#!/bin/bash

VERSION="0.5.2"

curl -sSL https://github.com/cloudflare/boringtun/archive/refs/tags/v${VERSION}.tar.gz | tar -xzf -
pushd boringtun-${VERSION} > /dev/null
cargo vendor
popd > /dev/null
tar -cf $(rpm -E '%{_sourcedir}')/boringtun-${VERSION}.tar.gz boringtun-${VERSION}
VERSION="${VERSION}" envsubst <./boringtun.spec.in > ./boringtun.spec
exec ../build-rpm.sh "$@"
