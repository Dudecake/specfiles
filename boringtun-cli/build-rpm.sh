#!/bin/bash

VERSION="0.5.2"

curl -sSL https://github.com/cloudflare/boringtun/archive/refs/tags/boringtun-cli-${VERSION}.tar.gz | tar -xzf -
mv boringtun-boringtun-cli-${VERSION} boringtun-cli-${VERSION}
pushd boringtun-cli-${VERSION} > /dev/null
CARGO_HOME=/usr/share/cargo cargo fetch
popd > /dev/null
tar -cf boringtun-cli-${VERSION}.tar.gz boringtun-cli-${VERSION}
sed "s/\${VERSION}/${VERSION}/" ./boringtun-cli.spec.in > ./boringtun-cli.spec
exec ../build-rpm.sh "$@"
