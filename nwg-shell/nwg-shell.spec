%global   forgeurl https://github.com/nwg-piotr/nwg-shell
%global   sys_name nwg_shell
%global   forgesource %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

Name:           nwg-shell
Version:        0.5.14
Summary:        Meta-package, installer and updater
Release:        4%{?dist}

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-gobject
Requires:       python3-dasbus
Requires:       gtk3-tools
Requires:       foot
Requires:       grim
Requires:       ImageMagick
Requires:       jq
Requires:       libappindicator-gtk3
Requires:       light
Requires:       font(dejavusans)
Requires:       font(dejavusansmono)
Requires:       font(dejavuserif)
Requires:       network-manager-applet
Requires:       papirus-icon-theme
Requires:       playerctl
Requires:       pulseaudio-utils
Requires:       (mate-polkit or polkit-gnome or polkit-kde-agent-5)
Requires:       python3-geopy
Requires:       python3-pyaml
Requires:       slurp
Requires:       swappy
Requires:       sway
Requires:       swayidle
Requires:       swaylock
Requires:       swaybg
Requires:       wl-clipboard
Requires:       xorg-x11-server-Xwayland
Requires:       wlsunset
Requires:       azote
Requires:       gopsuinfo
Requires:       nwg-bar
Requires:       nwg-dock
Requires:       nwg-drawer
Requires:       nwg-menu
Requires:       nwg-look
Requires:       nwg-panel
Requires:       nwg-shell-config
Requires:       nwg-displays
Requires:       SwayNotificationCenter
Requires:       gtklock
# Requires:       gtklock-userinfo-module
# Requires:       gtklock-powerbar-module
# Requires:       gtklock-playerctl-module

Recommends:     thunar

Suggests:       chromium
Suggests:       mousepad

%description
%{summary}

%prep
%autosetup -p1

%build
%py3_build
for lib in scripts/*; do
sed --in-place "1 s:(#!)s*/usr.*:1%{__python3}:" $lib
done

%install
%py3_install
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/*.py; do
sed --in-place '1{/^#!.*python/d}' $lib
done
install -D -t %{buildroot}%{_bindir} scripts/screenshot
install -D -t %{buildroot}%{_datadir}/backgrounds nwg-shell.jpg


%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{python3_sitelib}/%{sys_name}/
%{python3_sitelib}/%{sys_name}-%{version}-py%{python3_version}.egg-info/
%{_datadir}/backgrounds/*

%changelog
* Wed Oct 11 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.14-1
- Update to 0.5.14

* Tue Oct 10 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.13-1
- Update to 0.5.13

* Thu Oct 05 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.12-1
- Update to 0.5.12

* Tue Oct 03 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.11-1
- Update to 0.5.11

* Fri Sep 15 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.10-1
- Update to 0.5.10

* Fri Sep 01 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.9-1
- Update to 0.5.9

* Thu Aug 03 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.7-1
- Update to 0.5.7

* Tue Jun 20 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.6-1
- Update to 0.5.6

* Thu Jun 15 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.5-1
- Update to 0.5.5

* Tue Jun 13 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.3-1
- Update to 0.5.3

* Fri Jun 09 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.2-1
- Update to 0.5.2

* Fri Jun 09 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.5.0-1
- Update to 0.5.0

* Sun Jun 04 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.4.3-2
- Removed dependency on pamixer

* Sun Jun 04 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.4.3-1
- Update to 0.4.3

* Mon Feb 27 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.4.2-1
- Update to 0.4.2

* Sun Jan 01 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.3.9-3
- Removed Arch Linux specific scripts
- Presets patched to remove Arch Linux specific calls

* Sat Dec 31 2022 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.3.9-2
- Fixed dependencies

* Sat Dec 31 2022 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.3.9-1
- Initial build
