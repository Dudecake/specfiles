#!/bin/sh

set -e

pkgname="cosmic-icons"
../create-cosmic-spec.sh "${2}" ${pkgname} 'System76 Cosmic icon theme for Linux'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
