#!/bin/sh

set -e

install="
%make_install
"

files="
%{_bindir}/cosmic-comp
%{_datadir}/cosmic/com.system76.CosmicSettings.Shortcuts/v1/defaults
%{_datadir}/cosmic/com.system76.CosmicSettings.WindowRules/v1/tiling_exception_defaults
"

pkgname="cosmic-comp"
install="${install}" files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'Compositor for the COSMIC Desktop Environment'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
