#!/bin/bash

set -e
# git clone https://src.fedoraproject.org/rpms/mesa.git --branch rawhide --single-branch
HASH="$(curl https://gitlab.freedesktop.org/api/v4/projects/176/repository/commits | grep -oP '(?<="id":")[^"]+' | head -n1)"
VER="$(grep -oP '(?<=ver )\d+\.\d\.\d' ./mesa/mesa.spec)"
sed -i "s/${VER}/22.0.0/; s/%autorelease/1.git${HASH:0:7}%{?dist}/; s/https:\/\/mesa.freedesktop.org\/archive\/%{name}-%{ver}.tar.xz/https:\/\/gitlab.freedesktop.org\/mesa\/mesa\/-\/archive\/${HASH}\/mesa-${HASH}.tar.gz/; s/%{name}-%{ver}/%{name}-${HASH}/" ./mesa/mesa.spec

spectool -g ./mesa/mesa.spec -C mesa
rpmbuild -bs ./mesa/mesa.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/mesa"
RPM_FILE=$(rpm -q ./*.src.rpm --qf 'mesa-filesystem-%{version}-%{release}.%{arch}.rpm\n')
if [[ ! -f "${2}/${RPM_FILE}" ]]; then
  OLD_RPM=$(rpm -q ./*.src.rpm --qf '%{name}-*.%{arch}.rpm\n')
  [[ -f  "${2}/${OLD_RPM}" ]] && rm "${2}/${OLD_RPM}"
  ARCH="$(uname -m)"
  [[ "${ARCH}" = "x86_64" ]] && mock -r "${1}-i386" rebuild ./*.src.rpm --resultdir "${2}"
  exec mock -r "${1}-${ARCH}" rebuild ./*.src.rpm --resultdir "${2}"
fi
