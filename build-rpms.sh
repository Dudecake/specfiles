#!/bin/bash

SCRIPTDIR="$(dirname "$(readlink -f "$0")")"
ARCH="$(rpm -E '%_arch')"
BUILDDIR="${BUILDDIR:-${PWD}/target}"
RESULTDIR="${RESULTDIR:-${PWD}/repo}"
. /etc/os-release

RELEASEVER="${VERSION_ID}"
if [[ "${REDHAT_BUGZILLA_PRODUCT_VERSION}" = "rawhide" ]]; then
  RELEASEVER="$[${VERSION_ID}-1]"
  VERSION_ID="${REDHAT_BUGZILLA_PRODUCT_VERSION}"
  rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-${RELEASEVER}-${ARCH}
fi

set -e
cd ${SCRIPTDIR}
mkdir -p ${BUILDDIR}/{noarch,${ARCH},source}
[[ "${ID}" = "fedora" ]] && REPO="--repo fedora,updates"
dnf download kernel kernel-core kernel-devel kernel-headers.${ARCH} kernel-modules kernel-modules-extra ${REPO} --releasever ${RELEASEVER} --downloaddir "${PWD}/zfs"
cat << EOF > /etc/yum.repos.d/build.repo
[build-noarch]
name=build noarch
baseurl=file://${BUILDDIR}/noarch
enabled=1
priority=10

[build-${ARCH}]
name=build ${ARCH}
baseurl=file://${BUILDDIR}/${ARCH}
enabled=1
priority=10
EOF
createrepo --update "${BUILDDIR}/${ARCH}"
set +e
failed_pkgs=()
pushd . > /dev/null
for dir in ./*/; do
  popd > /dev/null
  pushd ${dir} > /dev/null
  if [[ -f ./.skip || -f "./.${ID}.skip" || -f "./.${ID}-${VERSION_ID}.skip" ]]; then
    echo "Skipping package ${dir} as it is excluded" >&2
    continue
  fi
  SCRIPT="../build-rpm.sh"
  if [[ -x ./build-rpm.sh ]]; then
    SCRIPT="./build-rpm.sh"
  elif [[ -f ./*.spec ]]; then
    continue
  fi
  ${SCRIPT} "${BUILDDIR}" "${RESULTDIR}"
  if [[ $? -ne 0 ]]; then
    echo "Could not build ${dir}" >&2
    failed_pkgs+=("${dir}")
  else
    createrepo --update "${BUILDDIR}/noarch"
    createrepo --update "${BUILDDIR}/${ARCH}"
  fi
done
[[ -d "${RESULTDIR}/${ARCH}" ]] || mkdir -p ${RESULTDIR}/{aarch64,x86_64,ppc64le}/{debug/tree,os} ${RESULTDIR}/source/tree
if [[ ! -z "${GPG_PATH}" ]]; then
  find ${BUILDDIR} -type f -name \*.rpm -exec rpm -D "_gpg_path ${GPG_PATH}" -D "_gpg_name ${GPG_NAME}" --addsign  {} \;
fi
mv ${BUILDDIR}/source/*.src.rpm "${RESULTDIR}/source/tree/"
mv ${BUILDDIR}/${ARCH}/*-debug{info,source}-*.rpm "${RESULTDIR}/${ARCH}/debug/tree/"
cp ${BUILDDIR}/noarch/*.noarch.rpm "${RESULTDIR}/aarch64/os"
cp ${BUILDDIR}/noarch/*.noarch.rpm "${RESULTDIR}/x86_64/os"
cp ${BUILDDIR}/noarch/*.noarch.rpm "${RESULTDIR}/ppc64le/os"
rm ${BUILDDIR}/noarch/*.noarch.rpm
mv ${BUILDDIR}/${ARCH}/*.rpm "${RESULTDIR}/${ARCH}/os"
for repo in "${RESULTDIR}/source/tree" "${RESULTDIR}/${ARCH}/debug/tree" "${RESULTDIR}/${ARCH}/os"; do
  createrepo --update "${repo}"
  rm -f $(repomanage --old "${repo}")
done
find "${RESULTDIR}" -type d -name repodata.old\* -exec rm -rf {} +
if [[ ${#failed_pkgs[@]} -ne 0 ]]; then
  echo "Could not build packages '${failed_pkgs[*]}'" >&2
fi
