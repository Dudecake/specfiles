#!/bin/sh

set -e

files="
%{_bindir}/cosmic-screenshot
%{_datadir}/applications/com.system76.CosmicScreenshot.desktop
"

pkgname="cosmic-screenshot"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'Utility for capturing screenshots via XDG Desktop Portal'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
