#!/bin/bash

VERSION="0.4.0"

curl -sSL https://github.com/cloudflare/boringtun/archive/refs/tags/v${VERSION}.tar.gz | tar -xzf -
pushd boringtun-${VERSION} > /dev/null
cargo vendor
popd > /dev/null
tar -cf ./boringtun-${VERSION}.tar.gz boringtun-${VERSION}
VERSION="${VERSION}" envsubst <./boringtun.spec.in > ./boringtun.spec
rpmbuild -bs ./*.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
