#!/bin/bash

MACHINE="$(uname -m)"
BASEARCH="${MACHINE}"
[[ "${MACHINE}" = "x86_64" ]] && BASEARCH="x64"
[[ "${MACHINE}" = "aarch64" ]] && BASEARCH="arm64"
BASEARCH=${BASEARCH} envsubst < ./chectl-bin.spec.in > ./chectl-bin.spec
exec ../build-rpm.sh "$@"
