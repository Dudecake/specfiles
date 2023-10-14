#!/bin/bash

version="0.1.3"
release="2"
summary="GTK3-based button bar for wlroots-based compositors"
url="https://github.com/nwg-piotr/nwg-bar"
license="MIT"
additional_build_requires=("pkgconfig(gdk-3.0)" "pkgconfig(gtk-layer-shell-0)")
additional_install='mkdir -p %{buildroot}%{_datadir}/%{name}/images
%{__install} config/* -t %{buildroot}%{_datadir}/%{name}
%{__install} images/* -t %{buildroot}%{_datadir}/%{name}/images'
supplements="nwg-panel"

version=${version} release=${release} summary="${summary}" url=${url} license=${license} additional_build_requires="${additional_build_requires[@]}" additional_install="${additional_install}" supplements="${supplements}" ../build-go-rpm.sh > nwg-bar.spec

exec ../build-rpm.sh "$@"
