%define githash e455d6752221b9e9c3818cc304c873b9c2792490

Name:               footswitch
Version:            1.0
Release:            2.gite455d67%{?dist}
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
%make_build CFLAGS="-fPIE -I/usr/include/hidapi"

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}/etc/udev/rules.d
%{__install} -p footswitch %{buildroot}%{_bindir}
%{__install} -p scythe %{buildroot}%{_bindir}
%{__install} -p 19-footswitch.rules %{buildroot}/etc/udev/rules.d

%files
%license LICENSE
%doc README.md
%{_bindir}/footswitch
%{_bindir}/scythe
%config %{_sysconfdir}/udev/rules.d/19-footswitch.rules
