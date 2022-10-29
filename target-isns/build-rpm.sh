#!/bin/bash

PKG=target-isns
set -e
if [[ ! -d ${PKG}/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/${PKG}.git --branch rawhide --depth=1
else
  pushd ./${PKG} > /dev/null
  git pull
  popd > /dev/null
fi
sed -i 's/\.tar\.gz/\.tar\.xz/g' ./${PKG}/${PKG}.spec
set +e
ln -s ./${PKG}/* ./

exec ../build-rpm.sh "$@"
