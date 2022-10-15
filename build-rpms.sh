#!/bin/bash

SCRIPTDIR="$(dirname "$(readlink -f "$0")")"
ARCH="$(uname -m)"
BUILDDIR="${BUILDDIR:-${PWD}/target}"
RESULTDIR="${RESULTDIR:-${PWD}/repo}"
. /etc/os-release

set -e
cd ${SCRIPTDIR}
mkdir -p ${BUILDDIR}
ln -s . ${BUILDDIR}/noarch
ln -s . ${BUILDDIR}/${ARCH}
dnf config-manager --add-repo "file://${BUILDDIR}/\$basearch/os/" --add-repo "file://${RESULTDIR}"
pushd . > /dev/null
for dir in ./*/; do
  popd > /dev/null
  pushd ${dir} > /dev/null
  [[ -f ./.skip || -f "./.${ID}-${VERSION_ID}.skip" ]] && continue
  SCRIPT="../build-rpm.sh"
  if [[ -x ./build-rpm.sh ]]; then
    SCRIPT="./build-rpm.sh"
  elif [[ -f ./*.spec ]]; then
    continue
  fi
  ${SCRIPT} "${BUILDDIR}" "${RESULTDIR}" || echo "Could not build ${dir}" >&2
done
[[ -d "${RESULTDIR}/${ARCH}" ]] || mkdir -p ${RESULTDIR}/{aarch64,x86_64,ppc64le}/{debug/tree,os} ${RESULTDIR}/source/tree
# TODO: sign rpms
set +e
mv ${BUILDDIR}/*.src.rpm "${RESULTDIR}/source/tree/"
mv ${BUILDDIR}/*-debug{info,source}-*.rpm "${RESULTDIR}/${ARCH}/debug/tree/"
cp ${BUILDDIR}/*.noarch.rpm "${RESULTDIR}/aarch64/os"
cp ${BUILDDIR}/*.noarch.rpm "${RESULTDIR}/x86_64/os"
cp ${BUILDDIR}/*.noarch.rpm "${RESULTDIR}/ppc64le/os"
rm ${BUILDDIR}/*.noarch.rpm
mv ${BUILDDIR}/*.rpm "${RESULTDIR}/${ARCH}/os"
set -x
for repo in "${RESULTDIR}/source/tree" "${RESULTDIR}/${ARCH}/debug/tree" "${RESULTDIR}/${ARCH}/os"; do
  createrepo "${repo}"
  rm -f $(repomanage --old "${repo}")
done
find "${RESULTDIR}" -type d -name repodata.old\* -exec rm -rf {} +
