#!/bin/sh

../build-rpm.sh ${1} ${2}
RPM_ROOT="${1}"
if [[ ! -f ${1}/libglibutil{,-devel}*.rpm ]]; then
  RPM_ROOT=${2}
fi
dnf install -y ${RPM_ROOT}/libglibutil{,-devel}*.rpm
