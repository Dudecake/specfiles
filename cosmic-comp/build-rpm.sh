#!/bin/sh

set -e

install="
%make_install
%__install -Dm0644 config.ron %{buildroot}/%{_sysconfdir}/cosmic-comp/config.ron
"

files="
%{_bindir}/cosmic-comp
%{_sysconfdir}/cosmic-comp/config.ron
"

install="${install}" files="${files}" ../create-cosmic-spec.sh cosmic-comp 'Compositor for the COSMIC Desktop Environment'

exec ../build-rpm.sh "$@"
