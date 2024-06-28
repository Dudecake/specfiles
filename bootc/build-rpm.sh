#!/bin/bash

curl -sSLO https://github.com/containers/bootc/raw/main/contrib/packaging/bootc.spec

exec ../build-rpm.sh "$@"
