#!/bin/sh

set -e

files="
%{_bindir}/cosmic-app-library
%{_datadir}/applications/com.system76.CosmicAppLibrary.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppLibrary.svg
%{_datadir}/metainfo/com.system76.CosmicAppLibrary.metainfo.xml
"

pkgname="cosmic-applibrary"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'A boilerplate template to get started with GTK, Rust, Meson, Flatpak, Debian made for Cosmic.' cosmic-app-library

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
