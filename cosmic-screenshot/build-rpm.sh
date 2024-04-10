#!/bin/sh

set -e

files="
%{_bindir}/cosmic-screenshot
%{_datadir}/applications/com.system76.CosmicScreenshot.desktop
"

files="${files}" ../create-cosmic-spec.sh cosmic-screenshot 'Utility for capturing screenshots via XDG Desktop Portal'

exec ../build-rpm.sh "$@"
