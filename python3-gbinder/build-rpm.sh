#!/bin/sh

../build-rpm.sh ${1} ${2}
RPMS="${1}/python3-gbinder*.rpm"
if [[ ! -f $RPMS ]]; then
  RPMS=${2}/$(uname -m)/os/python3-gbinder*.rpm
fi
dnf install -y ${RPMS}
