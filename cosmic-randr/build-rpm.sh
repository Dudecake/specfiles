#!/bin/sh

set -e

files="
%{_bindir}/cosmic-randr
"

pkgname="cosmic-randr"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'Library and utility for displaying and configuring Wayland outputs'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
