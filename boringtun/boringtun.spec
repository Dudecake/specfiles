Name:           boringtun
Version:        0.3.0
Release:        1%{?dist}
Summary:        Implementation of the WireGuard® protocol designed for portability and speed

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            https://github.com/cloudflare/boringtun
Source:         boringtun-%{version}.tar.gz
Patch0:         vendor.patch

BuildRequires:  cargo
BuildRequires:  rust-packaging

%description
%{summary}

%prep
%setup -q
%cargo_prep
%autopatch -p1

%build
/usr/bin/env CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 /usr/bin/cargo build -j8 --release --all-features

%install
%cargo_install -a
rm -rf %{?buildroot}%{_datadir}

%files
%caps(cap_net_admin+epi) %{_bindir}/boringtun
