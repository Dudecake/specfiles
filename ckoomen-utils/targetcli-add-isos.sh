#!/bin/bash

set -e

initiator_name=$(grep -Po 'iqn.*' /etc/iscsi/initiatorname.iscsi)
target_root="$(grep -Po 'iqn.*(?=:)' /etc/iscsi/initiatorname.iscsi | rev | cut -f 2- -d '.' | rev).iscsi"
existing_iscsi_shares=($(jq '.storage_objects[].dev' /etc/target/saveconfig.json -r))

# TODO: remove shares of size `0`

non_shared_files=($(find "${1}" -type f -name \*.iso))

(for file in "${non_shared_files[@]}"; do
  share_exists=0
  for existing_iscsi_share in ${existing_iscsi_shares[@]}; do
    [[ "${file}" = "${existing_iscsi_share}" ]] && share_exists=1
  done
  [[ ${share_exists} -eq 1 ]] && continue
  name=$(echo ${file} | grep -Po '[^\/]+(?=\.)' | sed 's/_/-/g' | tr '[:upper:]' '[:lower:]')

  cat << EOF
cd /backstores/fileio
create ${name} ${file} true
cd /iscsi
create ${target_root}:${name}
cd ${target_root}:${name}/tpg1
# set attribute prod_mode_write_protect=1
set attribute generate_node_acls=1
set attribute authentication=0
cd luns
create /backstores/fileio/${name}
EOF
done) | targetcli
