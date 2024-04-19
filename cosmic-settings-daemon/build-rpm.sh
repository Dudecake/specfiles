#!/bin/sh

set -e

files="
%{_bindir}/cosmic-settings-daemon
"

pkgname="cosmic-settings-daemon"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'Settings daemon for cosmic-settings'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
