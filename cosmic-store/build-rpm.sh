#!/bin/sh

set -e

files="
%{_bindir}/cosmic-store
%{_datadir}/applications/com.system76.CosmicStore.desktop
%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicStore.svg
%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicStore.svg
%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicStore.svg
%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicStore.svg
%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicStore.svg
%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicStore.svg
%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicStore.svg
%{_datadir}/metainfo/com.system76.CosmicStore.metainfo.xml
"

files="${files}" ../create-cosmic-spec.sh cosmic-store 'COSMIC App Store'

exec ../build-rpm.sh "$@"
