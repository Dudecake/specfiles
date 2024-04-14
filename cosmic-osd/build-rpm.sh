#!/bin/sh

set -e

files="
%{_bindir}/cosmic-osd
"

files="${files}" ../create-cosmic-spec.sh cosmic-osd 'OSDs for the COSMIC desktop environment'

exec ../build-rpm.sh "$@"
