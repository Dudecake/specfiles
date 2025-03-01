#!/bin/bash

PKG=bootc
BRANCH=rawhide
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}
sed -i '/cargo-rpm-macros/a BuildRequires: cargo-packaging' ${PKG}.spec
sed -i '/cargo-rpm-macros/d' ${PKG}.spec
exec ../build-rpm.sh "$@"
