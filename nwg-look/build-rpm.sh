#!/bin/bash

version="0.2.4"
release="1"
summary="GTK3 settings editor adapted to work in the wlroots environment"
url="https://github.com/nwg-piotr/nwg-look"
license="MIT"
additional_build_requires=("pkgconfig(gdk-3.0)")
additional_install='mkdir -p %{buildroot}%{_datadir}/{%{name}/langs,pixmaps,applications}
%{__install} stuff/main.glade -t %{buildroot}%{_datadir}/%{name}
%{__install} langs/* -t %{buildroot}%{_datadir}/%{name}/langs
%{__install} stuff/nwg-look.svg -t %{buildroot}%{_datadir}/pixmaps
%{__install} stuff/nwg-look.desktop -t %{buildroot}%{_datadir}/applications'

version=${version} release=${release} summary="${summary}" url=${url} license=${license} additional_build_requires="${additional_build_requires[@]}" additional_install="${additional_install}" ../build-go-rpm.sh > nwg-look.spec

exec ../build-rpm.sh "$@"
