#!/bin/bash

PKG=zsh-syntax-highlighting
BRANCH=rawhide
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}

sed -i 's:{_prefix}:{_prefix} DOC_DIR=%{_docdir}/%{name}:' ./${PKG}.spec
exit
exec ../build-rpm.sh "$@"
