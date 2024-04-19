#!/bin/sh

set -e

files="
%{_bindir}/cosmic-panel
%{_datadir}/cosmic/com.system76.CosmicPanel.Dock/*
%{_datadir}/cosmic/com.system76.CosmicPanel.Panel/*
%{_datadir}/cosmic/com.system76.CosmicPanel/*
"

pkgname="cosmic-panel"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'Panel for COSMIC Desktop Environment'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
