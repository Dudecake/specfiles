%define githash ed1211d9d0ffd21a64c0822c9ceb2986797aa9db

Name:               footswitch
Version:            1.0
Release:            1.gited1211d%{?dist}
Summary:            Command line utlities for programming PCsensor and Scythe foot switches.
URL:                https://github.com/rgerganov/%{name}
License:            GPLv2
BuildRequires:      gcc
BuildRequires:      hidapi-devel

Source0:            %{url}/archive/%{githash}.tar.gz

%description
%{summary}

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{githash}
sed -i 's:/etc:\$\(PREFIX\)/etc:g; s:\$\(PREFIX\)/bin:\$\(PREFIX\)/usr/bin:g' ./Makefile

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}/etc/udev/rules.d
%{__install} -p footswitch %{buildroot}%{_bindir}
%{__install} -p scythe %{buildroot}%{_bindir}
%{__install} -p 19-footswitch.rules %{buildroot}/etc/udev/rules.d

%files
%{_bindir}/footswitch
%{_bindir}/scythe
%config %{_sysconfdir}/udev/rules.d/19-footswitch.rules
