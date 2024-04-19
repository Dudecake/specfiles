#!/bin/sh

set -e

files="
%{_bindir}/cosmic-edit
%{_datadir}/applications/com.system76.CosmicEdit.desktop
%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicEdit.svg
%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicEdit.svg
%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicEdit.svg
%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicEdit.svg
%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicEdit.svg
%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicEdit.svg
%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicEdit.svg
%{_datadir}/metainfo/com.system76.CosmicEdit.metainfo.xml
"

pkgname="cosmic-edit"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'Text editor built using libcosmic for the COSMIC Desktop Environment'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
