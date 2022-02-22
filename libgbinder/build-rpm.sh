#!/bin/sh

../build-rpm.sh ${1} ${2}
RPMS="${1}/libgbinder*.rpm"
if [[ ! -f $RPMS ]]; then
  RPMS=${2}/$(uname -m)/os/libgbinder*.rpm
fi
dnf install -y ${RPMS}
