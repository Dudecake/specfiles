#!/bin/bash

version="0.1.1"
release="1"
summary="MenuStart plugin to nwg-panel, also capable of working standalone"
url="https://github.com/nwg-piotr/nwg-menu"
license="MIT"
additional_build_requires=("pkgconfig(gdk-3.0)" "pkgconfig(gtk-layer-shell-0)")
additional_install='mkdir -p %{buildroot}%{_datadir}/%{name}/desktop-directories
%{__install} menu-start.css -t %{buildroot}%{_datadir}/%{name}
%{__install} desktop-directories/* -t %{buildroot}%{_datadir}/%{name}/desktop-directories'

version=${version} release=${release} summary="${summary}" url=${url} license=${license} additional_build_requires="${additional_build_requires[@]}" additional_install="${additional_install}" ../build-go-rpm.sh > nwg-menu.spec

exec ../build-rpm.sh "$@"
