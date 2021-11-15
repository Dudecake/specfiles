#!/bin/sh

set -e
spectool -g ./*.spec
rpmbuild -bs ./*.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(rpm -q ./*.src.rpm --qf '%{name}-%{version}-%{release}.%{arch}.rpm\n')
if [[ ! -f "${3}/${ARCH}/os/${RPM_FILE}" ]]; then
  exec mock -r "${1}-$(uname -m)" rebuild ./*.src.rpm --resultdir "${2}"
fi
