#!/bin/sh

set -e

files="
%{_bindir}/cosmic-files
%{_datadir}/applications/com.system76.CosmicFiles.desktop
%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicFiles.svg
%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicFiles.svg
%{_datadir}/metainfo/com.system76.CosmicFiles.metainfo.xml
"

files="${files}" ../create-cosmic-spec.sh cosmic-files 'File browser built using libcosmic for the COSMIC Desktop Environment'
sed -i '/mkdir/a rm build.rs' cosmic-files.spec

exec ../build-rpm.sh "$@"
