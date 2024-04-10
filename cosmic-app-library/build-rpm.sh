#!/bin/sh

set -e

files="
%{_bindir}/cosmic-app-library
%{_datadir}/applications/com.system76.CosmicAppLibrary.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppLibrary.svg
%{_datadir}/metainfo/com.system76.CosmicAppLibrary.metainfo.xml
"

files="${files}" ../create-cosmic-spec.sh cosmic-applibrary 'A boilerplate template to get started with GTK, Rust, Meson, Flatpak, Debian made for Cosmic.' cosmic-app-library

exec ../build-rpm.sh "$@"
