#!/bin/bash

PKG=zsh-syntax-highlighting
BRANCH=rawhide
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}

sed -i 's:{_prefix}:{_prefix} DOC_DIR=%{buildroot}%{_docdir}/%{name} INSTALL="%{__install} -c":' ./${PKG}.spec

exec ../build-rpm.sh "$@"
