#!/bin/bash

set -e
ARCH="$(rpm -E '%_arch')"
srcdir="${1}/kernel-source"
specfile="${srcdir}/kernel-ckoomen.spec"

[[ -d kernel-source ]] || git clone https://github.com/openSUSE/kernel-source -b stable --depth=1

pushd kernel-source
grep -q 'SPLIT_BASE' rpm/config.sh || echo 'SPLIT_BASE=Yes' >> rpm/config.sh
source rpm/config.sh
if [[ ! -f ./config/${ARCH}/ckoomen ]]; then
  cp ../ckoomen ./config/${ARCH}/
  echo -e "+${ARCH}\t${ARCH}/ckoomen" >> config.conf
  cat << EOF >> ./rpm/package-descriptions
=== kernel-ckoomen ===
The Standard Kernel with ckoomen config

The standard kernel for both uniprocessor and multiprocessor systems with ckoomen config.
EOF
fi
suffix=$(sed -rn 's/^Source0:.*\.(tar\.[a-z0-9]*)$/\1/p' rpm/kernel-source.spec.in)
[[ -f "linux-${SRCVERSION}.${suffix}" ]] || curl -L --remote-name-all https://cdn.kernel.org/pub/linux/kernel/v${SRCVERSION:0:1}.x/linux-${SRCVERSION}.{${suffix},${suffix:0:3}.sign}
./scripts/tar-up.sh -d "${srcdir}" -a ${ARCH} -f ckoomen
touch "${srcdir}/TOLERATE-UNKNOWN-NEW-CONFIG-OPTIONS"
[[ -z "${SBOOT_BASE}" ]] || cp ${SBOOT_BASE}.* "${srcdir}"
popd > /dev/null
rpmbuild -bs "${specfile}" -D "_srcrpmdir ${PWD}" -D "_sourcedir ${srcdir}"
RPM_FILE="$(ls -1 kernel-ckoomen-*.nosrc.rpm)"
if [[ ! -z "${FORCE_REBUILD}" || ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.nosrc.rpm
  rpmbuild -bb "${specfile}" -D "_rpmdir ${1}" -D "_srcrpmdir ${1}" -D "_sourcedir ${srcdir}"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
[[ -z "${SBOOT_BASE}" ]] || cp ${SBOOT_BASE}.* "${srcdir}/${SBOOT_BASE##*/}"
