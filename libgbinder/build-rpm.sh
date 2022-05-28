#!/bin/sh

../build-rpm.sh ${1} ${2}
RPMS="${2}/libgbinder*.rpm"
if [[ ! -f $RPMS ]]; then
  RPMS=${1}/$(uname -m)/os/libgbinder*.rpm
fi
dnf install -y ${RPMS}
