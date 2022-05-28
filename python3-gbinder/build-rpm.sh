#!/bin/sh

../build-rpm.sh ${1} ${2}
RPMS="${2}/python3-gbinder*.rpm"
if [[ ! -f $RPMS ]]; then
  RPMS=${1}/$(uname -m)/os/python3-gbinder*.rpm
fi
dnf install -y ${RPMS}
