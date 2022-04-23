#!/bin/bash

PKG=resource-agents
set -e
if [[ ! -d ${PKG}/.git ]]; then
  git clone https://git.centos.org/rpms/${PKG}.git --branch c8s  --single-branch
else
  pushd ./${PKG} > /dev/null
  git pull
  popd > /dev/null
fi
HASH=$(spectool -l ./${PKG}/SPECS/${PKG}.spec | grep -Po '(?<=resource-agents-).{8}(?=\.)')
REPO=resource-agents
if [[ ! -d ${REPO}/.git ]]; then
  git clone https://github.com/ClusterLabs/resource-agents.git --branch main  --single-branch
  pushd ./${REPO} > /dev/null
  git checkout ${HASH}
  popd > /dev/null
else
  pushd ./${REPO} > /dev/null
  git pull
  git checkout ${HASH}
  popd > /dev/null
fi
TARFILE=${PKG}/SOURCES/ClusterLabs-resource-agents-${HASH}.tar.gz
TAG=$(git log --pretty="format:%h" -n 1)
distdir="ClusterLabs-resource-agents-${TAG}"
TARFILE="${distdir}.tar.gz"
rm -rf $TARFILE $distdir
git archive --prefix=$distdir/ HEAD | gzip > $TARFILE
spectool -g ./${PKG}/SPECS/${PKG}.spec -C ${PKG}/SOURCES
rpmbuild -bs ./${PKG}/SPECS/${PKG}.spec -D "_srcrpmdir ${PWD}" -D "_sourcedir ${PWD}/${PKG}/SOURCES"
RPM_FILE=$(ls -1 ./*.src.rpm | head -n1)
if [[ ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  dnf builddep -y ./*.src.rpm --enablerepo powertools
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}"
else
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
