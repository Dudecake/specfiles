Name:           boringtun
Version:        0.3.0
Release:        1%{?dist}
Summary:        Implementation of the WireGuard® protocol designed for portability and speed

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            https://github.com/cloudflare/boringtun
Source:         boringtun-0.3.0.tar.gz
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
%cargo_build -a

%install
%cargo_install -a
setcap cap_net_admin+epi %{?buildroot}%{_bindir}/boringtun
