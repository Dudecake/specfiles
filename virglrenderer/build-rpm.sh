#!/bin/bash

GROUP=virgl
PKG=virglrenderer
BRANCH=rawhide
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}
HASH=$(grep -oP '(?<=gitversion ).+' ./${PKG}/${PKG}.spec)
sed -i "s/virglrenderer-%{gitdate}.tar.xz/https:\/\/gitlab.freedesktop.org\/${GROUP}\/${PKG}\/-\/archive\/${HASH}\/${PKG}-${HASH}.tar.gz/; s/%{name}-%{gitdate}/%{name}-%{gitversion}/; s/%meson /%meson -Dvenus-experimental=true /" ./${PKG}/${PKG}.spec
set +e
ln -s ./${PKG}/* ./

exec ../build-rpm.sh "$@"
