%define githash b7493170ecc956ac87df2c36183253c945be2dcf

Name:               footswitch
Version:            1.0
Release:            1.gitb749317%{?dist}
Summary:            Command line utlities for programming PCsensor and Scythe foot switches.
URL:                https://github.com/rgerganov/%{name}
License:            GPLv2
BuildRequires:      gcc
%if 0%{?suse_version}
BuildRequires:      libhidapi-devel
%else
BuildRequires:      hidapi-devel
%endif


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
