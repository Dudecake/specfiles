#!/bin/sh

set -e

dnf install -y cargo jq

reponame="${1}"
summary="${2}"
pkgname="${3:-${reponame}}"

hash_and_date=($(curl -sSL https://api.github.com/repos/pop-os/${reponame}/commits/master | jq -r '.sha,.commit.committer.date'))

githash="${hash_and_date[0]}"
date="${hash_and_date[1]}"

spec="../cosmic.spec.in"
[[ -f ${pkgname}.spec.in ]] && spec="${pkgname}.spec.in"

sed "s:\${githash}:${githash}:g; s:\${shorthash}:${githash:0:7}:g; s:\${reponame}:${reponame}:g; s:\${pkgname}:${pkgname}:g; s:\${summary}:${summary}:g; s/\${date}/${date}/g; s:\${files}:${files//$'\n'/\\n}:g" ${spec} > ${pkgname}.spec

[[ -d ${reponame}-${githash} ]] || curl -L https://github.com/pop-os/${reponame}/archive/${githash}.tar.gz | bsdtar -xf -

pushd ${reponame}-${githash} > /dev/null
[[ -d .vendor ]] || mkdir .vendor
cargo vendor > .vendor/config.toml
tar -cf ../vendor.tar vendor
rm -rf vendor
popd
tar -czf ${reponame}.tar.gz ${reponame}-${githash}
rm -rf ${reponame}-${githash}
