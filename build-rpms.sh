#!/bin/bash

RESULTDIR="${PWD}/target"

set -e
for dir in ./*/; do
  pushd ${dir} > /dev/null
  SCRIPT="../build-rpm.sh"
  if [[ -x ./build-rpm.sh ]]; then
    SCRIPT="./build-rpm.sh"
  fi
  ${SCRIPT} "${1}" "${RESULTDIR}" || true
  popd > /dev/null
done