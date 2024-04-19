#!/bin/sh

set -e

files="
%{_bindir}/cosmic-launcher
%{_datadir}/applications/com.system76.CosmicLauncher.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicLauncher.svg
%{_datadir}/metainfo/com.system76.CosmicLauncher.metainfo.xml
"

pkgname="cosmic-launcher"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'Layer shell frontend for Pop Launcher'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
