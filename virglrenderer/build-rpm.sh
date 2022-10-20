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
ln -s ./${PKG}/${PKG}.spec

exec ../build-rpm.sh "$@"
