%global sys_name nwg_panel
%global forgeurl https://github.com/nwg-piotr/nwg-panel
%global forgesource %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

Name:       nwg-panel
Version:    0.9.14
Release:    2%{?dist}
Summary:    GTK3-based panel for sway window manager
BuildArch:  noarch

License:    MIT
URL:        %{forgeurl}
Source:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: python3-devel >= 3.4
BuildRequires: python3-setuptools
BuildRequires: systemd-rpm-macros

Requires:   libgtk-layer-shell0
Requires:   gtk3-tools
Requires:   python3-gobject
Requires:   python3-i3ipc
Requires:   python3-dasbus
Requires:   wlr-randr

Recommends: light
Recommends: playerctl
Recommends: python3-netifaces
Recommends: python3-psutil
Recommends: python3-pybluez

Recommends: pulseaudio-utils

%description
I have been using sway since 2019 and find it the most comfortable working
environment, but... Have you ever missed all the graphical bells and whistles
in your panel, we used to have in tint2? It happens to me. That's why I
decided to try to code a GTK-based panel, including best features from my two
favourites: Waybar and tint2. Many thanks to Developers and Contributors of
the both projects!

There are 8 modules available at the moment, and I don't plan on many more.
Basis system controls are available in the Controls module, and whatever else
you may need, there's an executor for that.


%prep
%autosetup -p1

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|'     nwg_panel/executors/arch_updates.py


%build
%py3_build


%install
%py3_install

# Remove shebang from Python libraries
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/{/,modules}/*.py; do
sed '1{@^#!/usr/bin/env python@d}' $lib > $lib.new &&
touch -r $lib $lib.new &&
mv $lib.new $lib
done

# Remove shebang from Python libraries
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/*.py; do
sed '1{@^#!/usr/bin/python@d}' $lib > $lib.new &&
touch -r $lib $lib.new &&
mv $lib.new $lib
done

install -Dpm 0644 %{name}.svg -t %{buildroot}%{_datadir}/pixmaps/
install -Dpm 0644 nwg-shell.svg -t %{buildroot}%{_datadir}/pixmaps/
install -Dpm 0755 %{name}-config.desktop -t %{buildroot}%{_datadir}/applications/
install -Dpm 0644 %{name}.service -t %{buildroot}%{_userunitdir}/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-config
%{_bindir}/nwg-dwl-interface
%{_bindir}/nwg-processes
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_userunitdir}/%{name}.service
%{python3_sitelib}/%{sys_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{sys_name}/


%changelog
* Fri Oct 13 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.14-1
- Update to 0.9.14

* Thu Sep 21 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.13-1
- Update to 0.9.13

* Fri Sep 01 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.12-1
- Update to 0.9.12

* Fri Aug 04 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.11-1
- Update to 0.9.11

* Tue Jul 11 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.10-1
- Update to 0.9.10

* Sat Jul 08 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.9-1
- Update to 0.9.9

* Wed Jun 28 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.8-1
- Update to 0.9.8

* Tue Jun 13 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.7-1
- Update to 0.9.7

* Tue Jun 06 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.6-2
- Added missing dependency python3-dasbus

* Mon Jun 05 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.6-1
- Update to 0.9.6
- Added patch providing support for pactl to interact with pipewire

* Tue May 23 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.3-1
- chore: Update to 0.9.3

* Sat May 06 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-1
- chore: Update to 0.9.1

* Thu May 04 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.0-1
- chore: Update to 0.9.0

* Tue May 02 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.7-1
- chore: Update to 0.8.7

* Mon May 01 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.6-1
- chore: Update to 0.8.6

* Fri Apr 28 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.5-1
- chore: Update to 0.8.5

* Mon Apr 10 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.3-1
- chore: Update to 0.8.3

* Sat Mar 11 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.1-1
- chore: Update to 0.8.1

* Sun Feb 19 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.17-1
- chore: Update to 0.7.17

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.16-1
- chore: Update to 0.7.16

* Sat Dec 10 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.15-1
- chore: Update to 0.7.15

* Sun Dec 04 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.14-1
- chore: Update to 0.7.14

* Fri Oct 28 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.13-1
- chore(update): 0.7.13

* Sun Oct 23 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.12-1
- chore(update): 0.7.12

* Thu Oct 13 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.11-1
- chore(update): 0.7.11

* Fri Oct 07 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.10-1
- chore(update): 0.7.10

* Thu Oct 06 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.9-1
- fix: Previous commit

* Thu Oct 06 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.8-2
- chore(update): 0.7.9

* Tue Sep 13 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.8-1
- chore(update): 0.7.8

* Thu Sep 01 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.7-1
- chore(update): 0.7.7

* Mon Aug 29 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.6-1
- chore(update): 0.7.6

* Mon Aug 22 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.5-1
- chore(update): 0.7.5

* Mon Aug 15 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.4-1
- chore(update): 0.7.4

* Sun Jul 31 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.3-1
- chore(update): 0.7.3

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.1-1
- chore(update): 0.7.1

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.11

* Mon Jun 06 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-1
- chore(update): 0.7.0

* Fri May 13 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.4-1
- chore(update): 0.6.4

* Wed Apr 13 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.3-1
- chore(update): 0.6.3

* Thu Mar 17 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.2-1
- chore(update): 0.6.2

* Tue Feb 01 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-1
- chore(update): 0.6.1

* Sat Jan 29 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.0-1
- chore(update): 0.6.0 (Pre-release for Rawhide only)

* Wed Jan 26 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.8-1
- chore(update): 0.5.8

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.7-1
- chore(update): 0.5.7

* Sun Jan 09 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.6-1
- chore(update): 0.5.6

* Thu Dec 30 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.3-1
- chore(update): 0.5.3

* Tue Dec 14 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.2-1
- chore(update): 0.5.2

* Mon Dec 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.1-1
- chore(update): 0.5.1

* Tue Nov 16 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-1
- chore(update): 0.5.0

* Mon Aug 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.3-1
- build(update): 0.4.3

* Fri Jul 30 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.2-1
- build(update): 0.4.2

* Thu Jul 29 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.1-1
- build(update): 0.4.1

* Mon Jul 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-1
- build(update): 0.4.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.3-1
- build(update): 0.3.3

* Wed Jun 09 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.2-1
- build(update): 0.3.2

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.1-2
- Rebuilt for Python 3.10
