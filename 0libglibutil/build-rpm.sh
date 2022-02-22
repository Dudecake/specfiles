#!/bin/sh

../build-rpm.sh ${1} ${2}
RPMS="${1}/libglibutil*.rpm"
if [[ ! -f $RPMS ]]; then
  RPMS=${2}/$(uname -m)/os/libglibutil*.rpm
fi
dnf install -y ${RPMS}
