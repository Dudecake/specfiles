#!/bin/sh

set -e

files="
%{_bindir}/cosmic-panel
%{_datadir}/cosmic/com.system76.CosmicPanel.Dock/*
%{_datadir}/cosmic/com.system76.CosmicPanel.Panel/*
%{_datadir}/cosmic/com.system76.CosmicPanel/*
"

files="${files}" ../create-cosmic-spec.sh cosmic-panel 'Panel for COSMIC Desktop Environment'

exec ../build-rpm.sh "$@"
