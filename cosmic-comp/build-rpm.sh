#!/bin/sh

set -e

install="
%make_install
%__install -Dm0644 config.ron %{buildroot}/%{_sysconfdir}/cosmic-comp/config.ron
"

files="
%{_bindir}/cosmic-comp
%{_sysconfdir}/cosmic-comp/config.ron
"

pkgname="cosmic-comp"
install="${install}" files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'Compositor for the COSMIC Desktop Environment'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
