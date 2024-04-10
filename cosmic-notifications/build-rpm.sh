#!/bin/sh

set -e

files="
%{_bindir}/cosmic-notifications
%{_datadir}/applications/com.system76.CosmicNotifications.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicNotifications.svg
%{_datadir}/metainfo/com.system76.CosmicNotifications.metainfo.xml
"

files="${files}" ../create-cosmic-spec.sh cosmic-notifications 'Layer Shell notifications daemon which integrates with COSMIC'

exec ../build-rpm.sh "$@"
