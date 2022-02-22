#!/bin/sh

../build-rpm.sh ${1} ${2}
RPM_ROOT="${1}"
if [[ ! -f ${1}/python3-gbinder*.rpm ]]; then
  RPM_ROOT=${2}
fi
dnf install -y ${RPM_ROOT}/python3-gbinder*.rpm
