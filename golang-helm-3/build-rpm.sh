#!/bin/bash

PKG=golang-helm-3
set -e
if [[ ! -d ${PKG}/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/${PKG}.git --branch rawhide --depth=1
else
  pushd ./${PKG} > /dev/null
  git pull
  popd > /dev/null
fi
ln -s ./${PKG}/${PKG}.spec

exec ../build-rpm.sh "$@"
