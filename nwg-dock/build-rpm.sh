#!/bin/bash

version="0.3.9"
release="1"
summary="GTK3-based dock for sway"
url="https://github.com/nwg-piotr/nwg-dock"
license="MIT"
additional_build_requires=("pkgconfig(gdk-3.0)" "pkgconfig(gtk-layer-shell-0)")
additional_install='mkdir -p %{buildroot}%{_datadir}/%{name}/images
%{__install} config/* -t %{buildroot}%{_datadir}/%{name}
%{__install} images/* -t %{buildroot}%{_datadir}/%{name}/images'

version=${version} release=${release} summary="${summary}" url=${url} license=${license} additional_build_requires="${additional_build_requires[@]}" additional_install="${additional_install}" ../build-go-rpm.sh > nwg-dock.spec

exec ../build-rpm.sh "$@"
