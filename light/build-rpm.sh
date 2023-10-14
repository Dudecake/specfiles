#!/bin/bash

PKG=light
BRANCH=f38
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}
sed -i '/%make_install/a rm -rf %{buildroot}%{_datadir}/doc' ./${PKG}.spec

exec ../build-rpm.sh "$@"
