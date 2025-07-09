#!/bin/bash

PKG=bootc
BRANCH=rawhide
set -e
../fetch-fedora-pkg.sh ${PKG} ${BRANCH}
sed -i '/BuildRequires: rust-toolset/a %elif 0%{?suse_version}\nBuildRequires: cargo-packaging' ${PKG}.spec
sed -i '/Source1/a Source9:        %{url}\/pull\/215.patch:' ${PKG}.spec
sed -i 's/0%{?fedora}/0%{?suse_version} || 0%{?fedora}/g' ${PKG}.spec
sed -i '/cargo_prep/i %if !0%{?suse_version}' ${PKG}.spec
sed -i '/cargo_prep/a %endif\n' ${PKG}.spec
sed -i '/cargo_vendor_manifest/i %if !0%{?suse_version}' ${PKG}.spec
sed -i '/%{cargo_license}/a %endif\n' ${PKG}.spec
sed -i '/%license LICENSE.dependencies/i %if !0%{?suse_version}' ${PKG}.spec
sed -i '/%license cargo-vendor.txt/a %endif' ${PKG}.spec
exec ../build-rpm.sh "$@"
