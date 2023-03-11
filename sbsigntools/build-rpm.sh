#!/bin/bash

PKG=sbsigntools
set -e
if [[ ! -d ${PKG}/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/${PKG}.git --branch rawhide --depth=1
else
  pushd ./${PKG} > /dev/null
  git restore ${PKG}.spec
  git pull
  popd > /dev/null
fi
set +e
ln -s ./${PKG}/* ./

exec ../build-rpm.sh "$@"
