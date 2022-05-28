#!/bin/sh

set -e
spectool -g ./*.spec
rpmbuild -bs ./*.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}"
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
else
  rm ./*.src.rpm
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
