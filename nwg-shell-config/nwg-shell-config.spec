# -*-Mode: rpm-spec -*-

%global   forgeurl https://github.com/nwg-piotr/nwg-shell-config
%global sys_name nwg_shell_config
%global   forgesource %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

Name:           nwg-shell-config
Version:        0.5.22
Summary:        Allows to set the common sway preferences
Release:        2%{?dist}

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-gobject
Requires:       python3-i3ipc
Requires:       python3-geopy

Recommends:     gtklock
Recommends:     playerctl
Recommends:     gammastep

%description
Nwg-shell-config allows to set the common sway preferences
(screen, input devices, idle and lock screen configuration,
main applications key bindings), as well as switch between
predefined desktop styles. Each of the above may be adjusted
to user’s taste, that includes placement of the application drawer,
dock, exit menu, and notification center.

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
install -m644 -D -t %{buildroot}%{_datadir}/pixmaps nwg-shell-config.svg
install -m644 -D -t %{buildroot}%{_datadir}/pixmaps nwg-shell-update.svg
install -m644 -D -t %{buildroot}%{_datadir}/applications nwg-shell-config.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{python3_sitelib}/%{sys_name}/
%{python3_sitelib}/%{sys_name}-%{version}-py%{python3_version}.egg-info/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Wed Oct 11 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.22-1
- Update to 0.5.22

* Tue Oct 10 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.21-1
- Update to 0.5.21

* Wed Oct 04 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.20-1
- Update to 0.5.20

* Tue Oct 03 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.19-1
- Update to 0.5.19

* Fri Sep 15 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.18-1
- Update to 0.5.18

* Fri Sep 01 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.17-1
- Update to 0.5.17

* Sat Aug 05 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.14-1
- Update to 0.5.14

* Fri Jul 28 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.13-1
- Update to 0.5.13

* Sat Jul 22 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.12-1
- Update to 0.5.12

* Sun Jul 16 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.11-1
- Update to 0.5.11

* Sun Jul 02 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.9-1
- Update to 0.5.9

* Sat Jul 01 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.8-1
- Update to 0.5.8

* Sun Jun 18 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.7-1
- Update to 0.5.7

* Tue Jun 13 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.6-1
- Update to 0.5.6

* Fri Jun 09 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.5-1
- Update to 0.5.5

* Mon Jun 05 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.2-1
- Update to 0.5.2

* Sun Jun 04 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.0-2
- Added gammastep as recommended package

* Sun Jun 04 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.0-1
- Update to 0.5.0

* Mon Feb 27 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.4.14-1
- Update to 0.4.14

* Fri Dec 30 2022 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.4.10-2
- Added dependencies

* Thu Dec 29 2022 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.4.10-1
- Initial build
