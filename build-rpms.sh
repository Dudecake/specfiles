#!/bin/bash

RESULTDIR="${2:-${PWD}/target}"

set -e
for dir in ./*/; do
  [[ -f "${dir}/.${1}.skip" ]] && continue
  pushd ${dir} > /dev/null
  SCRIPT="../build-rpm.sh"
  if [[ -x ./build-rpm.sh ]]; then
    SCRIPT="./build-rpm.sh"
  fi
  ${SCRIPT} "${1}" "${RESULTDIR}" || true
  popd > /dev/null
done
createrepo "${RESULTDIR}"
