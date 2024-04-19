#!/bin/sh

set -e

install="
install -Dm0755 target/release//cosmic-greeter %{buildroot}/%{_bindir}/cosmic-greeter
install -Dm0755 target/release//cosmic-greeter-daemon %{buildroot}/%{_bindir}/cosmic-greeter-daemon
install -Dm0644 dbus/com.system76.CosmicGreeter.conf %{buildroot}/%{_datadir}/dbus-1/system.d/com.system76.CosmicGreeter.conf
install -Dm0644 debian/cosmic-greeter.sysusers %{buildroot}/%{_sysusersdir}/cosmic-greeter.conf
install -Dm0644 debian/cosmic-greeter.tmpfiles %{buildroot}/%{_tmpfilesdir}/cosmic-greeter.conf
install -Dm0644 cosmic-greeter.toml %{buildroot}/%{_prefix}/etc/greetd/cosmic-greeter.toml
install -Dm0644 debian/cosmic-greeter.service %{buildroot}/%{_unitdir}/cosmic-greeter.service
install -Dm0644 debian/cosmic-greeter-daemon.service %{buildroot}/%{_unitdir}/cosmic-greeter-daemon.service
"

files="
%{_bindir}/cosmic-greeter
%{_bindir}/cosmic-greeter-daemon
%{_datadir}/dbus-1/system.d/com.system76.CosmicGreeter.conf
%{_sysusersdir}/cosmic-greeter.conf
%{_tmpfilesdir}/cosmic-greeter.conf
%{_prefix}/etc/greetd/cosmic-greeter.toml
%{_unitdir}/cosmic-greeter.service
%{_unitdir}/cosmic-greeter-daemon.service
"

pkgname="cosmic-greeter"
install="${install}" files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'libcosmic greeter for greetd, which can be run inside cosmic-comp'

patches="Patch1: service.patch

BuildRequires:   systemd-rpm-macros
%{?sysusers_requires_compat}
"

custom="%post
%systemd_post cosmic-greeter.service
%systemd_post cosmic-greeter-daemon.service

%preun
%systemd_preun cosmic-greeter.service
%systemd_preun cosmic-greeter-daemon.service

%postun
%systemd_postun cosmic-greeter.service
%systemd_postun cosmic-greeter-daemon.service
"

if [[ -f ${pkgname}.spec ]]; then
  sed -i "/# patches/a ${patches//$'\n'/\\n}" cosmic-greeter.spec
  sed -i "/# custom/a ${custom//$'\n'/\\n}" cosmic-greeter.spec

  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
