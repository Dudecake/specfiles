# -*-Mode: rpm-spec -*-

%global   forgeurl https://github.com/nwg-piotr/nwg-icon-picker
%global sys_name nwg_icon_picker
%global   forgesource %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

Name:           nwg-icon-picker
Version:        0.1.0
Summary:        Nwg-icon-picker is a tool to search GTK icons by name
Release:        2%{?dist}

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-gobject
Requires:       gtk3

%description
This program is a part of the nwg-shell project.

This program provides an intuitive GUI to manage multiple icon-picker,
save outputs configuration and workspace-to-output assignments.

%prep
%autosetup

%build
%py3_build

%install
%py3_install
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/*.py; do
sed '1{@^#!/usr/bin/env python@d}' $lib > $lib.new &&
touch -r $lib $lib.new &&
mv $lib.new $lib
done
install -D -t %{buildroot}%{_datadir}/pixmaps nwg-icon-picker.svg
install -D -t %{buildroot}%{_datadir}/applications nwg-icon-picker.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{python3_sitelib}/%{sys_name}/
%{python3_sitelib}/%{sys_name}-%{version}-py%{python3_version}.egg-info/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Sun Jun 04 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.1.0-1
- Update to 0.1.0
* Fri Dec 30 2022 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.0.1-1
- Initial build
