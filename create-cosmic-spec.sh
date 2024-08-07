#!/bin/sh

set -e

dnf install -y cargo jq

repo="${1}"
reponame="${2}"
summary="${3}"
pkgname="${4:-${reponame}}"

release="$(curl -sSL "https://api.github.com/repos/pop-os/${reponame}/commits?per_page=1" --head | grep -Po '(?<=page=)\d+(?=>; rel="last")')"

spec="../cosmic.spec.in"
[[ -f ${pkgname}.spec.in ]] && spec="${pkgname}.spec.in"
version="$(grep -Po '(?<=Version:)\s*\d+\.\d+(\.\d+)?' ${spec} | tr -d '[:space:]')"

if [[ -f "${repo}/source/tree/${pkgname}-${version}-${release}.src.rpm" ]]; then
  echo "No rebuild neccesary for package ${RPM_FILE}" >&2
  exit
fi

hash_and_date=($(curl -sSL https://api.github.com/repos/pop-os/${reponame}/commits/master | jq -r '.sha,.commit.committer.date'))

githash="${hash_and_date[0]}"
date="${hash_and_date[1]:0:10}"

[[ -d ${reponame}-${githash} ]] || curl -L https://github.com/pop-os/${reponame}/archive/${githash}.tar.gz | bsdtar -xf -

uses_make=0
[[ -f ${reponame}-${githash}/Makefile ]] && uses_make=1
if [[ -z "${build}" ]]; then
  build='VERGEN_GIT_SHA="%{githash}" VERGEN_GIT_COMMIT_DATE="%{date}" just build-vendored'
  (( uses_make == 1 )) && build='VERGEN_GIT_SHA="%{githash}" VERGEN_GIT_COMMIT_DATE="%{date}" %make_build all VENDOR=1'
fi
if [[ -z "${install}" ]]; then
  install='just rootdir=%{buildroot} prefix=%{_prefix} install'
  (( uses_make == 1 )) && install='%make_install prefix=%{_prefix}'
fi

sed "s:\${githash}:${githash}:g; s:\${shorthash}:${githash:0:7}:g; s:\${release}:${release}:g; s:\${reponame}:${reponame}:g; s:\${pkgname}:${pkgname}:g; s:\${summary}:${summary}:g; s/\${date}/${date}/g; s:\${build}:${build//$'\n'/\\n}:; s:\${install}:${install//$'\n'/\\n}:; s:\${files}:${files//$'\n'/\\n}:g" ${spec} > ${pkgname}.spec

RPM_FILE=$(python3 -c "import specfile; print(specfile.Specfile(\"${pkgname}.spec\").expand(\"%name-%version-%release.src.rpm\"))")
if [[ -z "${FORCE_REBUILD}" && -f "${repo}/source/tree/${RPM_FILE}" ]]; then
  echo "No rebuild neccesary for package ${RPM_FILE}" >&2
  rm ${pkgname}.spec
  exit
fi

if [[ -f ${reponame}-${githash}/Cargo.lock ]]; then
  pushd ${reponame}-${githash} > /dev/null
  file=$(mktemp)
  python3 -c 'import sys, tomllib, json; f = open("./Cargo.lock", "rb"); print(json.dumps(tomllib.load(f))); f.close()' | jq -r '.package[] | "Provides:  bundled(crate(\(.name))) = \(.version)"' | sed 's/-/_/g' > ${file}
  [[ -d .vendor ]] || mkdir .vendor
  cargo vendor > .vendor/config.toml
  tar -cf ../vendor.tar vendor
  rm -rf vendor
  popd
  provides_section_start="$(grep -n '# provides' ${pkgname}.spec)"
  provides_section_start=${provides_section_start%:*}
  head -n${provides_section_start} ${pkgname}.spec > ${pkgname}.spec.tmp
  cat ${file} >> ${pkgname}.spec.tmp
  tail -n+$((${provides_section_start}+1)) ${pkgname}.spec >> ${pkgname}.spec.tmp
  mv ${pkgname}.spec.tmp ${pkgname}.spec
fi
tar -czf ${reponame}.tar.gz ${reponame}-${githash}
rm -rf ${reponame}-${githash}
