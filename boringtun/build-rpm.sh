#!/bin/bash

curl -sSL https://github.com/cloudflare/boringtun/archive/refs/tags/v0.3.0.tar.gz | tar -xzf -
pushd boringtun-0.3.0 > /dev/null
cargo vendor
popd > /dev/null
tar -cf ./boringtun-0.3.0.tar.gz boringtun-0.3.0
rpmbuild -bs ./*.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
