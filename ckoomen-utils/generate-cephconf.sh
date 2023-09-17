#!/bin/bash

params=$(getopt -o '' -l fsid: -l hostnames: -l addresses: -l public-network: -n generate-cephconf -- "$@")
if [[ $? -ne 0 ]]; then
  exit 1
fi

eval set -- "$params"
unset params
while :
do
  case "${1}" in
    --fsid)
      fsid="${2}"
      shift 2
      ;;
    --hostnames)
      hostnames="${2}"
      shift 2
      ;;
    --addresses)
      addresses="${2}"
      shift 2
      ;;
    --public-network)
      public_network="${2}"
      shift 2
      ;;
    --)
      shift
      break
      ;;
  esac
done

cat << EOF
[global]
fsid = ${fsid}
mon initial members = ${hostnames}
mon host = ${addresses}
public network = ${public_network}
auth cluster required = cephx
auth service required = cephx
auth client required = cephx
osd pool default size = 3
osd pool default min size = 2

[mds.${HOSTNAME}]
host = ${HOSTNAME}

[mon]
mgr_initial_modules = dashboard
EOF
