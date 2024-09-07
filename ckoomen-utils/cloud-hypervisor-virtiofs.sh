#!/bin/sh

set -e

params=$(getopt -o '' -l network: -n cloud-hypervisor-virtiofs -- "$@")
if [[ $? -ne 0 ]]; then
  exit 1
fi

# The MAC address must be attached to the macvtap and be used inside the guest
mac="c2:67:4f:53:29:ce"
# Host network adapter to bridge the guest onto
host_net="$(ip r s default | grep -Po '(?<=dev )[^\s]+' | head -n1)"
tap_device="macvtap0"

eval set -- "$params"
unset params
while :
do
  case "${1}" in
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

root_dir="${1}"
init="${2}"
# Create the macvtap0 as a new virtual MAC associated with the host network
ip link add link "$host_net" name ${tap_device} type macvtap
ip link set ${tap_device} address "$mac" up
ip link show ${tap_device}

virtiofsd_sock="$(mktemp --suffix .virtiofsd.sock)"

cleanup() {
  rm ${virtiofsd_sock}
  ip link delete dev ${tap_device} type macvtap
}
trap cleanup ERR

# A new character device is created for this interface
tapindex=$(< /sys/class/net/${tap_device}/ifindex)
tapdevice="/dev/tap$tapindex"

kernel="/usr/share/cloud-hypervisor/vmlinux.bin"
image="/tmp/cloud-hypervisor-nfs.img"
cmdline="console=hvc0 rootfstype=virtiofs root=/dev/root rw panic=15"
[[ -z "${init}" ]] || cmdline="${cmdline} init=${init}"
# TODO: search '/boot/loader/entries' for kernels to use

/usr/libexec/virtiofsd --socket-path=${virtiofsd_sock} --shared-dir="${root_dir}" --cache=never --posix-acl &
sleep 1
cloud-hypervisor \
        --cpus boot=4 \
        --memory size=4G,shared=on \
        --balloon size=0,free_page_reporting=on \
        --kernel "${kernel}" \
        --fs tag=/dev/root,socket=${virtiofsd_sock} \
        --cmdline "${cmdline}" \
        --net fd=3,mac=$mac \
        --watchdog \
        --pvpanic \
        --console tty 3<>$"$tapdevice"

cleanup
