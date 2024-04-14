#!/bin/sh

set -e

files="
%{_bindir}/cosmic-settings-daemon
"

files="${files}" ../create-cosmic-spec.sh cosmic-settings-daemon 'Settings daemon for cosmic-settings'

exec ../build-rpm.sh "$@"
