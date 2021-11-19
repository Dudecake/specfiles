%define githash 3bd96990f0ffd467889964ee206f0155bf4a2396

Name:           console-tdm
Version:        1.4
Release:        1.git3bd9699%{?dist}
Summary:        Bash based display manager
URL:            https://github.com/dopsi/%{name}
License:        GPLv3
Requires:       xorg-x11-xinit
BuildRequires:  make
BuildArch:      noarch

Source0:    %{url}/archive/%{githash}.tar.gz

%description
%{summary}

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{githash}

%build

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/tdm
%{_bindir}/tdmctl
%{_mandir}/man1/tdm.1*
%{_mandir}/man1/tdmctl.1*
%{_datadir}/bash-completion/completions/tdmctl
%{_datadir}/zsh/site-functions/_tdmctl
%{_datadir}/tdm
