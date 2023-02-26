%define githash 64c726e502e48e63de4834fad0bdf12c026f7899

Name:       sbkeys
Version:    1.1.0
Release:    2.git64c726e%{?dist}
Summary:    Simple script to generate Secure Boot keys

License:    GPLv3
URL:        https://github.com/electrickite/%{name}
Source0:    %{url}/archive/%{githash}.tar.gz

Requires:   %{_bindir}/openssl
Requires:   %{_bindir}/uuidgen
Requires:   %{_bindir}/cert-to-efi-sig-list
Requires:   %{_bindir}/sign-efi-sig-list
Recommends: %{_bindir}/wget
Recommends: %{_bindir}/sbsiglist

BuildArch:  noarch

%description
%{summary}

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{githash}

%install
%{__install} -Dm755 sbkeys %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
