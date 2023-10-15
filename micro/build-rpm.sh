#!/bin/bash

version="2.0.12"
release="1"
summary="A modern and intuitive terminal-based text editor"
url="https://github.com/zyedidia/micro"
license="MIT and ASL 2.0"

version=${version} release=${release} summary="${summary}" url=${url} license=${license} ../build-go-rpm.sh > micro.spec

exec ../build-rpm.sh "$@"
