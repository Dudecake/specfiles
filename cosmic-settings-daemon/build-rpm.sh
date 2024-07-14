#!/bin/sh

set -e

files="
%{_bindir}/cosmic-settings-daemon
%{_datadir}/cosmic/com.system76.CosmicSettings.Shortcuts/v1/system_actions
%{_datadir}/polkit-1/rules.d/cosmic-settings-daemon.rules
"

pkgname="cosmic-settings-daemon"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'Settings daemon for cosmic-settings'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
