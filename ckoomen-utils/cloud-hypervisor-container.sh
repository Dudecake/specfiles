#!/bin/sh

set -e

params=$(getopt -o '' -l network: -l container: -n cloud-hypervisor-container -- "$@")
if [[ $? -ne 0 ]]; then
  exit 1
fi

eval set -- "$params"
unset params
while :
do
  case "${1}" in
    --container)
      container="${2}"
      shift 2
      ;;
    --network)
      host_net="${2}"
      shift 2
      ;;
    --)
      shift
      break
      ;;
  esac
  sleep 1
done

if [[ -z "${container}" ]]; then
  echo 'Container argument is required' >&2
  exit 1
fi

set -x
container_root="$(podman mount ${container})"

cleanup() {
  podman unmount ${container}
}
trap cleanup ERR

if [[ -z "${host_net}" ]]; then
  cloud-hypervisor-virtiofs.sh "${container_root}"
else
  cloud-hypervisor-virtiofs.sh --network "${host_net}" "${container_root}"
fi

cleanup
