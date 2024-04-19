#!/bin/sh

set -e

files="
%{_bindir}/cosmic-settings
%{_datadir}/applications/com.system76.CosmicSettings.desktop
%{_datadir}/applications/com.system76.CosmicSettings.*.desktop
%{_datadir}/cosmic/com.system76.CosmicTheme.Dark.Builder/v1/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Dark/v1/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Light.Builder/v1/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Light/v1/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Mode/v1/*
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-dark-style-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-dark-style-slightly-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-dark-style-square.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-light-style-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-light-style-slightly-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-light-style-square.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-mode-dark.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-mode-light.svg
%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicSettings.svg
%{_datadir}/metainfo/com.system76.CosmicSettings.metainfo.xml
%{_datadir}/polkit-1/rules.d/cosmic-settings.rules
"

pkgname="cosmic-settings"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'The settings application for the COSMIC desktop environment'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
