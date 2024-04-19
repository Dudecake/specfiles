#!/bin/sh

set -e

pkgname="cosmic-applets"
../create-cosmic-spec.sh "${2}" ${pkgname} '' cosmic-applet

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
