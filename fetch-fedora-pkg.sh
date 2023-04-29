#!/bin/sh

if [[ $# -ne 2 ]]; then
  echo "'$0' requires exactly 2 arguments" >&2
  exit 1
fi

pkg=${1}
branch=${2}

set -e
if [[ ! -d ${pkg}/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/${pkg}.git --branch ${branch} --depth=1
else
  pushd ./${pkg} > /dev/null
  git restore ${pkg}.spec
  git pull
  popd > /dev/null
fi

ln -sf ./${pkg}/* ./
