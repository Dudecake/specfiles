#!/bin/bash

ARCH="$(uname -m)"
BUILDDIR="${2:-${PWD}/target}"
RESULTDIR="${3:-${PWD}/repo}"

set -e
for dir in ./*/; do
  [[ -f "${dir}/.${1}.skip" ]] && continue
  pushd ${dir} > /dev/null
  SCRIPT="../build-rpm.sh"
  if [[ -x ./build-rpm.sh ]]; then
    SCRIPT="./build-rpm.sh"
  fi
  ${SCRIPT} "${1}" "${BUILDDIR}" "${RESULTDIR}" || true
  popd > /dev/null
done
[[ -d "${RESULTDIR}/${ARCH}" ]] || mkdir -p ${RESULTDIR}/${ARCH}/{debug/tree,os} ${RESULTDIR}/source/tree
mv ${BUILDDIR}/*.src.rpm "${RESULTDIR}/source/tree/"
mv ${BUILDDIR}/*-debuginfo-*.rpm "${RESULTDIR}/${ARCH}/debug/tree/"
mv ${BUILDDIR}/*.noarch.rpm "${RESULTDIR}/${ARCH}/os"
for repo in "${RESULTDIR}/source/tree/" "${RESULTDIR}/${ARCH}/debug/tree/" "${RESULTDIR}/${ARCH}/os"; do
  rm $(repomanage --old ${repo})
  createrepo --update ${repo}
done
