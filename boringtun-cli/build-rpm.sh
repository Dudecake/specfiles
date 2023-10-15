#!/bin/bash

set -e

VERSION="0.5.2"

sed "s/\${VERSION}/${VERSION}/" ./boringtun-cli.spec.in > ./boringtun-cli.spec
RPM_FILE=$(python3 -c "import specfile; print(specfile.Specfile(\"boringtun-cli.spec\").expand(\"%name-%version-%release.src.rpm\"))")
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  tarball="$(rpm -E %{_sourcedir}/boringtun-cli-${VERSION}.tar.gz)"
  curl -L https://github.com/cloudflare/boringtun/archive/refs/tags/boringtun-cli-${VERSION}.tar.gz -o "${tarball}"
  bsdtar -xf "${tarball}"
  pushd boringtun-boringtun-cli-${VERSION} > /dev/null
  dnf install -y cargo
  cargo vendor
  bsdtar -cf ../vendor.tar.zst vendor
  popd > /dev/null
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
