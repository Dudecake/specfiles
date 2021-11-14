#!/bin/sh

set -e
spectool -g ./*.spec
rpmbuild -bs ./*.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(rpm -q ./*.src.rpm --qf '%{name}-%{version}-%{release}.%{arch}.rpm\n')
if [[ ! -f "${2}/${RPM_FILE}" ]]; then
  OLD_RPM=$(rpm -q ./*.src.rpm --qf '%{name}-*.%{arch}.rpm\n')
  [[ -f  "${2}/${OLD_RPM}" ]] && rm "${2}/${OLD_RPM}"
  exec mock -r "${1}" rebuild ./*.src.rpm --resultdir "${2}"
fi