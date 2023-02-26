#!/bin/bash

VERSION="0.5.2"

curl -sSL https://github.com/cloudflare/boringtun/archive/refs/tags/boringtun-cli-${VERSION}.tar.gz | tar -xzf -
pushd boringtun-cli-${VERSION} > /dev/null
cargo vendor
popd > /dev/null
tar -cf $(rpm -E '%{_sourcedir}')/boringtun-cli-${VERSION}.tar.gz boringtun-cli-${VERSION}
VERSION="${VERSION}" envsubst <./boringtun-cli.spec.in > ./boringtun-cli.spec
exec ../build-rpm.sh "$@"
