#!/bin/sh

set -e

files="
%{_bindir}/cosmic-session
%{_bindir}/start-cosmic
%{_userunitdir}/cosmic-session.target
%{_datadir}/wayland-sessions/cosmic.desktop
%{_datadir}/applications/cosmic-mimeapps.list
"

install="
# main binary
install -Dm0755 target/release/cosmic-session %{buildroot}%{_bindir}/cosmic-session

# session start script
install -Dm0755 data/start-cosmic %{buildroot}%{_bindir}/start-cosmic

# systemd target
install -Dm0644 data/cosmic-session.target %{buildroot}%{_userunitdir}/cosmic-session.target

# session
install -Dm0644 data/cosmic.desktop %{buildroot}%{_datadir}/wayland-sessions/cosmic.desktop

# mimeapps
install -Dm0644 data/cosmic-mimeapps.list %{buildroot}%{_datadir}/applications/cosmic-mimeapps.list
"

build="just vendor=1 all" install="${install}" files="${files}" ../create-cosmic-spec.sh cosmic-session 'Session manager for the COSMIC desktop environment'

exec ../build-rpm.sh "$@"
