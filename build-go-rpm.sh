#!/bin/bash

set -e
name=$(basename $PWD)

if [[ -z "${version}" || -z "${release}" || -z "${summary}" || -z "${url}" || -z "${license}" ]]; then
  echo 'Required value unset' >&2
  exit 1
fi

[[ -d ${name}-${version} ]] || curl -L ${url}/archive/refs/tags/v${version}.tar.gz | bsdtar -xf -

pushd ${name}-${version} > /dev/null

vendored_deps=($(grep go.mod go.sum | grep -Po '^[^\s]+'))

go mod vendor

bsdtar -cf ../vendor.tar.zst vendor
rm -rf vendor

popd > /dev/null

bsdtar -cf ${name}-${version}.tar.zst ${name}-${version}

cat << EOF
Name:       ${name}
Version:    ${version}
Release:    ${release}
Summary:    ${summary}

URL:        ${url}
License:    ${license}

Source:     %{name}-%{version}.tar.zst
Source1:    vendor.tar.zst

BuildRequires:  golang-packaging
BuildRequires:  zstd
EOF

for requires in ${additional_build_requires[@]}; do
  echo "BuildRequires:  ${requires}"
done

echo

for dep in ${vendored_deps[@]}; do
  echo "Provides:   bundled(golang(${dep}))"
done

echo

cat << EOF
%description
%{summary}

%prep
%autosetup -p1 -a1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -v %{?_smp_build_ncpus:-p %{?_smp_build_ncpus}}

%install
%{__install} -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
EOF

for install in "${additional_install[@]}"; do
  echo "${install}"
done

echo

cat << EOF
%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/%{name}
EOF

for file in ${additional_files[@]}; do
  echo "${file}"
done
