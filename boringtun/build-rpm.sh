#!/bin/bash

curl -L https://github.com/cloudflare/boringtun/archive/refs/tags/v0.3.0.tar.gz | tar -xzf -
pushd boringtun-0.3.0 > /dev/null
cargo vendor
popd > /dev/null
tar -cf ./boringtun-0.3.0.tar.gz boringtun-0.3.0
rpmbuild -bs ./*.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(rpm -q ./*.src.rpm --qf '%{name}-%{version}-%{release}.%{arch}.rpm\n')
if [[ ! -f "${2}/${ARCH}/os/${RPM_FILE}" ]]; then
  exec rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
fi
