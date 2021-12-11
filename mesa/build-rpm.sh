#!/bin/bash

set -e
if [[ ! -d mesa/.git ]]; then
  git clone https://src.fedoraproject.org/rpms/mesa.git --branch rawhide --single-branch
else
  pushd ./mesa > /dev/null
  git restore mesa.spec
  git pull
  popd > /dev/null
fi
HASH="$(curl https://gitlab.freedesktop.org/api/v4/projects/176/repository/commits | grep -oP '(?<="id":")[^"]+' | head -n1)"
VER="$(grep -oP '(?<=ver )\d+\.\d\.\d' ./mesa/mesa.spec)"
sed -i "s/${VER}/22.0.0/; s/%autorelease/1.$(date -u +%Y%m%d).git${HASH:0:7}%{?dist}/; s/https:\/\/mesa.freedesktop.org\/archive\/%{name}-%{ver}.tar.xz/https:\/\/gitlab.freedesktop.org\/mesa\/mesa\/-\/archive\/${HASH}\/mesa-${HASH}.tar.gz/; s/%{name}-%{ver}/%{name}-${HASH}/" ./mesa/mesa.spec

spectool -g ./mesa/mesa.spec -C mesa
rpmbuild -bs ./mesa/mesa.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/mesa"
set +e
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  cp /etc/dnf/dnf.conf ./
  echo multilib_policy=all >> ./dnf.conf
  dnf builddep ./*.src.rpm -c ./dnf.conf
  [[ "${ARCH}" = "x86_64" ]] && dnf builddep ./.src.rpm --forcearch && rpmbuild --target i686 --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
fi
