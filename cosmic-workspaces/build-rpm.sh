#!/bin/sh

set -e

files="
%{_bindir}/cosmic-workspaces
%{_datadir}/applications/com.system76.CosmicWorkspaces.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicWorkspaces.svg
"

pkgname="cosmic-workspaces"
files="${files}" ../create-cosmic-spec.sh "${2}" cosmic-workspaces-epoch 'The settings application for the COSMIC desktop environment' ${pkgname}

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
