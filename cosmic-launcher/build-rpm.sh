#!/bin/sh

set -e

files="
%{_bindir}/cosmic-launcher
%{_datadir}/applications/com.system76.CosmicLauncher.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicLauncher.svg
%{_datadir}/metainfo/com.system76.CosmicLauncher.metainfo.xml
"

files="${files}" ../create-cosmic-spec.sh cosmic-launcher 'Layer shell frontend for Pop Launcher'

exec ../build-rpm.sh "$@"
