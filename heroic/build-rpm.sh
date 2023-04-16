#!/bin/bash

pkg=heroic
arch="$(rpm -E %{_arch})"
base_url="https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/releases"

if [[ "${arch}" = "x86_64" ]]; then
  version_tag="$(curl -sS ${base_url}/latest --head | grep -Po 'v\d+\.\d+\.\d+')"
  rpm_version="${version_tag:1:${#version_tag}}"
  rpm_file="${pkg}-${rpm_version}.${arch}.rpm"

  if [[ ! -f "{2}/os/${rpm_file}" ]]
    curl -L "${base_url}/download/${version_tag}/${rpm_file}" -o "${1}/${arch}/${rpm_file}"
  else
    echo "No rebuild neccesary for package $(basename $PWD)" >&2
  fi
fi
