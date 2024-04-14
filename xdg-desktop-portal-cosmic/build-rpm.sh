#!/bin/sh

set -e

files="
%{_libexecdir}/xdg-desktop-portal-cosmic
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.cosmic.service
%{_datadir}/xdg-desktop-portal/portals/cosmic.portal
%{_datadir}/xdg-desktop-portal/cosmic-portals.conf
%{_datadir}/icons/hicolor/scalable/actions/screenshot-screen-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/screenshot-selection-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/screenshot-window-symbolic.svg
"

files="${files}" ../create-cosmic-spec.sh xdg-desktop-portal-cosmic 'XDG Desktop Portals for the COSMIC Desktop Environment'

exec ../build-rpm.sh "$@"
