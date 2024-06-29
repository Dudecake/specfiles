#!/bin/bash

set -ex

curl -sSLO https://github.com/containers/bootc/raw/main/contrib/packaging/bootc.spec

version="$(grep -Po '(?<=Version:)\s*\d+\.\d+(\.\d+)?' bootc.spec)"

verlte() {
    [  "$1" = "`echo -e "$1\n$2" | sort -V | head -n1`" ]
}

verlt() {
    [ "$1" = "$2" ] && return 1 || verlte $1 $2
}

verlt "${version}" '0.1.13' && sed -i "s:${version}:0.1.13:g" bootc.spec

exec ../build-rpm.sh "$@"
