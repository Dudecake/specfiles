#!/bin/bash

version="0.1.5"
release="1"
summary="Displays customizable system usage info"
url="https://github.com/nwg-piotr/gopsuinfo"
license="BSD"
additional_install='mkdir -p %{buildroot}%{_datadir}/%{name}/icons_{light,dark}
%{__install} icons_light/* -t %{buildroot}%{_datadir}/%{name}/icons_light
%{__install} icons_dark/* -t %{buildroot}%{_datadir}/%{name}/icons_dark'
supplements="nwg-panel"

version=${version} release=${release} summary="${summary}" url=${url} license=${license} additional_build_requires="${additional_build_requires[@]}" additional_install="${additional_install}" supplements="${supplements}" ../build-go-rpm.sh > nwg-bar.spec

exec ../build-rpm.sh "$@"
