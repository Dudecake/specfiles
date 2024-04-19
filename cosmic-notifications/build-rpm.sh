#!/bin/sh

set -e

files="
%{_bindir}/cosmic-notifications
%{_datadir}/applications/com.system76.CosmicNotifications.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicNotifications.svg
%{_datadir}/metainfo/com.system76.CosmicNotifications.metainfo.xml
"

pkgname="cosmic-notifications"
files="${files}" ../create-cosmic-spec.sh "${2}" ${pkgname} 'Layer Shell notifications daemon which integrates with COSMIC'

if [[ -f ${pkgname}.spec ]]; then
  exec ../build-rpm.sh "$@"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
