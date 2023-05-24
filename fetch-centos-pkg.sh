#!/bin/sh

if [[ $# -ne 2 ]]; then
  echo "'$0' requires exactly 2 arguments" >&2
  exit 1
fi

pkg=${1}
branch=${2}

set -e
if [[ ! -d ${pkg}/.git ]]; then
  git clone https://git.centos.org/rpms/${pkg}.git --branch ${branch} --depth=1
else
  git -C ${PWD}/${pkg} restore SPECS/${pkg}.spec
  git -C ${PWD}/${pkg} pull
fi

ln -sf ./${pkg}/*/* ./
