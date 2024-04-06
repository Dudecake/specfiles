#!/bin/sh

set -e

dnf install -y cargo jq

name="cosmic-applets"

githash="$(curl -sSL https://api.github.com/repos/pop-os/${name}/commits/master | jq -r '.sha')"

sed "s/\${githash}/${githash}/; s/\${shorthash}/${githash:0:7}/g" cosmic-applet.spec.in > cosmic-applet.spec

[[ -d ${name}-${githash} ]] || curl -L https://github.com/pop-os/${name}/archive/${githash}.tar.gz | bsdtar -xf -

pushd ${name}-${githash} > /dev/null
[[ -d .vendor ]] || mkdir .vendor
cargo vendor > .vendor/config.toml
tar -cf ../vendor.tar vendor
rm -rf vendor
popd
tar -czf ${name}.tar.gz ${name}-${githash}

exec ../build-rpm.sh "$@"
