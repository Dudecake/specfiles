#!/bin/bash

version="0.3.9"
release="1"
summary="Application drawer for wlroots-based Wayland compositors"
url="https://github.com/nwg-piotr/nwg-drawer"
license="MIT"
additional_build_requires=("pkgconfig(gdk-3.0)" "pkgconfig(gtk-layer-shell-0)")
additional_install='mkdir -p %{buildroot}%{_datadir}/%{name}/desktop-directories
%{__install} desktop-directories/* -t %{buildroot}%{_datadir}/%{name}/desktop-directories'

version=${version} release=${release} summary="${summary}" url=${url} license=${license} additional_build_requires="${additional_build_requires[@]}" additional_install="${additional_install}" ../build-go-rpm.sh > nwg-drawer.spec

exec ../build-rpm.sh "$@"
