#!/bin/bash

GROUP=virgl
PKG=virglrenderer
set -e
if [[ ! -d ${PKG}/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/${PKG}.git --branch rawhide --depth=1
else
  pushd ./${PKG} > /dev/null
  git restore ${PKG}.spec
  git pull
  popd > /dev/null
fi
HASH=$(grep -oP '(?<=gitversion ).+' ./${PKG}/${PKG}.spec)
sed -i "s/virglrenderer-%{gitdate}.tar.xz/https:\/\/gitlab.freedesktop.org\/${GROUP}\/${PKG}\/-\/archive\/${HASH}\/${PKG}-${HASH}.tar.gz/; s/%meson/%meson -Dvenus-experimental=true/" ./${PKG}/${PKG}.spec
spectool -g ./${PKG}/${PKG}.spec -C ${PKG}
rpmbuild -bs ./${PKG}/${PKG}.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/${PKG}"
set +e
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
else
  rm ./*.src.rpm
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
