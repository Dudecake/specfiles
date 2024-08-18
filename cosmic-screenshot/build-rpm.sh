#!/bin/sh

set -e

files="
%{_bindir}/cosmic-screenshot
%{_datadir}/applications/com.system76.CosmicScreenshot.desktop
%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicScreenshot.svg
%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicScreenshot.svg
%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicScreenshot.svg
%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicScreenshot.svg
%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicScreenshot.svg
%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicScreenshot.svg
%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicScreenshot.svg
"

pkgname="cosmic-screenshot"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'Utility for capturing screenshots via XDG Desktop Portal'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
