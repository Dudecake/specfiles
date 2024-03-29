#!/bin/sh

set -ex

script_dir="${PWD}"

[[ -d ${1}/cosmic-basedir ]] && rm -rf ${1}/cosmic-basedir
mkdir ${1}/cosmic-basedir
git clone --recurse-submodules https://pagure.io/fedora-cosmic/cosmic-packaging.git ${1}/cosmic-basedir/cosmic-packaging
cd ${1}/cosmic-basedir/cosmic-packaging

dnf install -y cargo

pushd . > /dev/null
for dir in ./*/; do
  popd > /dev/null
  pushd ${dir} > /dev/null
  if [[ -f ./srpm.sh ]]; then
    _package="$(basename $PWD)"
    [[ -d ../../cosmic-rpms/${_package} ]] || mkdir -p ../../cosmic-rpms/${_package}
    sed 's/%autorelease/1/g' ./${_package}.spec > ../../cosmic-rpms/${_package}/${_package}.spec
    . ./srpm.sh
    mkdir ../${_package}
    sed 's/dbus-devel/dbus-1-devel/g; s/libappstream-glib/libappstream-glib8/g; s/libseat-devel/seatd-devel/g; s/mesa-libgbm-devel/libgbm-devel/g; /rust-rav1e+nasm-rs-devel/d; s/rustc/rust/g' ./${_package}.spec > ../${_package}/${_package}.spec
    if [[ -f ./vendor.tar ]]; then
      mv ./${_package}.tar.gz "$(rpm -E '%_sourcedir')"
      mv vendor.tar ../${_package}
    elif [[ -f ./${_package}.tar.gz ]]; then
      mv ./${_package}.tar.gz ../${_package}
    fi
    cd ../${_package}
    ${script_dir}/../build-rpm.sh "$@"
  fi
done
