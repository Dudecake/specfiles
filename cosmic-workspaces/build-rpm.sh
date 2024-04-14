#!/bin/sh

set -e

files="
%{_bindir}/cosmic-workspaces
%{_datadir}/applications/com.system76.CosmicWorkspaces.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicWorkspaces.svg
"

files="${files}" ../create-cosmic-spec.sh cosmic-workspaces-epoch 'The settings application for the COSMIC desktop environment' cosmic-workspaces

exec ../build-rpm.sh "$@"
