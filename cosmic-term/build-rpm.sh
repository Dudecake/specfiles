#!/bin/sh

set -e

files="
%{_bindir}/cosmic-term
%{_datadir}/applications/com.system76.CosmicTerm.desktop
%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicTerm.svg
%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicTerm.svg
%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicTerm.svg
%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicTerm.svg
%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicTerm.svg
%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicTerm.svg
%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicTerm.svg
%{_datadir}/metainfo/com.system76.CosmicTerm.metainfo.xml
"

files="${files}" ../create-cosmic-spec.sh cosmic-term 'WIP COSMIC terminal emulator'

exec ../build-rpm.sh "$@"
