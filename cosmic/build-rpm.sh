#!/bin/sh

set -ex

mkdir basedir
git clone --recurse-submodules https://pagure.io/fedora-cosmic/cosmic-packaging.git basedir/cosmic-packaging
cd basedir/cosmic-packaging

dnf install -y cargo

pushd . > /dev/null
for dir in ./*/; do
  popd > /dev/null
  pushd ${dir} > /dev/null
  if [[ -f ./srpm.sh ]]; then
    _package="$(basename $PWD)"
    mkdir -p ../../cosmic-rpms/${_package}
    cp ./*.spec ../../cosmic-rpms/${_package}
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
    ../../build-rpm.sh "$@"
  fi
done
