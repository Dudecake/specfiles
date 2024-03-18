Name:       gleam-bin
Version:    1.0.0
Release:    0%{?dist}
Summary:    A friendly language for building type-safe, scalable systems!
URL:        https://gleam.run
License:    Apache-2.0

Source0:    https://github.com/gleam-lang/gleam/releases/download/v%{version}/gleam-v%{version}-%{_arch}-unknown-linux-musl.tar.gz
ExclusiveArch:  x86_64 aarch64

Provides:   gleam
Conflicts:  gleam

%description
%{summary}

%global debug_package %{nil}

%prep
%setup -cq

%build

%install
%__mkdir -p %{?buildroot}%{_bindir}/
%{__cp} -a gleam %{?buildroot}%{_bindir}

%files
%{_bindir}/gleam
