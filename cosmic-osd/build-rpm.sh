#!/bin/sh

set -e

files="
%{_bindir}/cosmic-osd
"

pkgname="cosmic-osd"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'OSDs for the COSMIC desktop environment'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
