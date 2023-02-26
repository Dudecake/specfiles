#!/bin/sh

set -e
spectool -gR ./*.spec
pectool ./*.spec | grep -Po '(?<=: )(?!http).+' | xargs -I{} cp {} $(rpm -E '%{_sourcedir}')
rpmbuild -bs ./*.spec -D "_srcrpmdir ${PWD}"
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}/source"
else
  rm ./*.src.rpm
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
