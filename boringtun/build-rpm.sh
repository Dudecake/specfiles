#!/bin/bash

curl -L https://github.com/cloudflare/boringtun/archive/refs/tags/v0.3.0.tar.gz | tar -xzf -
pushd boringtun-0.3.0 > /dev/null
cargo vendor
popd > /dev/null
tar -cf ./boringtun-0.3.0.tar.gz boringtun-0.3.0
rpmbuild -bs ./*.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(rpm -q ./*.src.rpm --qf '%{name}-%{version}-%{release}.%{arch}.rpm\n')
if [[ ! -f "${3}/${ARCH}/os/${RPM_FILE}" ]]; then
  exec mock -r "${1}-$(uname -m)" rebuild ./*.src.rpm --resultdir "${2}"
fi
