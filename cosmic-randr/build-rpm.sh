#!/bin/sh

set -e

files="
%{_bindir}/cosmic-randr
"

files="${files}" ../create-cosmic-spec.sh cosmic-randr 'Library and utility for displaying and configuring Wayland outputs'

exec ../build-rpm.sh "$@"
