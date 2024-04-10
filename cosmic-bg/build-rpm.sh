#!/bin/sh

set -e

files="
%{_bindir}/cosmic-bg
%{_datadir}/applications/com.system76.CosmicBackground.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicBackground.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.system76.CosmicBackground-symbolic.svg
%{_datadir}/metainfo/com.system76.CosmicBackground.metainfo.xml
%{_datadir}/cosmic/com.system76.CosmicBackground/*
"

files="${files}" ../create-cosmic-spec.sh cosmic-bg 'COSMIC session service which applies backgrounds to displays'

exec ../build-rpm.sh "$@"
