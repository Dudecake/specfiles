#!/bin/sh

PKG=tcmu-runner
set -e
if [[ ! -d ${PKG}/.git ]]; then
  git clone --branch c9s-sig-storage-gluster-9 --depth=1 https://git.centos.org/rpms/tcmu-runner.git
else
  pushd ./${PKG} > /dev/null
  git restore SPECS/${PKG}.spec
  git pull
  popd > /dev/null
fi

ln -s ./${PKG}/*/* ./

exec ../build-rpm.sh "$@"
