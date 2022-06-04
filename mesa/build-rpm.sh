#!/bin/bash

PKG=mesa
set -e
if [[ ! -d ${PKG}/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/${PKG}.git --branch rawhide --single-branch
else
  pushd ./${PKG} > /dev/null
  git restore ${PKG}.spec
  git pull
  popd > /dev/null
fi
readarray -t COMMIT_DATA <<< "$(curl -sS https://gitlab.freedesktop.org/api/v4/projects/176/repository/commits | jq '.[0] | .short_id, .created_at')"
HASH="${COMMIT_DATA[0]:1:7}"
DATE="$(echo ${COMMIT_DATA[1]:1:10} | sed 's/-//g')"
VER="$(grep -oP '(?<=ver )\d+\.\d\.\d' ./${PKG}/${PKG}.spec)"
sed -i "s/${VER}/22.2.0/; s/%autorelease/10.${DATE}.git${HASH}%{?dist}/; s/https:\/\/archive.mesa3d.org\/mesa-%{ver}.tar.xz/https:\/\/gitlab.freedesktop.org\/mesa\/mesa\/-\/archive\/${HASH}\/mesa-${HASH}.tar.gz/; s/%{name}-%{ver}/%{name}-${HASH}/; /00-mesa-defaults.conf/a %{_datadir}/drirc.d/00-radv-defaults.conf" ./${PKG}/${PKG}.spec
truncate -s0 ${PKG}/0001-llvmpipe-flush-resources-for-kms-swrast-path.patch

spectool -g ./${PKG}/${PKG}.spec -C ${PKG}
rpmbuild -bs ./${PKG}/${PKG}.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/${PKG}"
set +e
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  cp /etc/dnf/dnf.conf ./
  echo multilib_policy=all >> ./dnf.conf
  dnf builddep -y ./*.src.rpm -c ./dnf.conf
  #[[ "$(uname -m)" = "x86_64" ]] && linux32 rpmbuild --target i686 --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
else
  rm ./*.src.rpm
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
