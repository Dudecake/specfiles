#!/bin/sh

params=$(getopt -o '' -l nfs-server: -l iscsi-server: -l base-iqn: -n generate-ipxe -- "$@")
if [[ $? -ne 0 ]]; then
  exit 1
fi

eval set -- "$params"
unset params
while :
do
  case "${1}" in
    --nfs-server)
      nfs_server="${2}"
      shift 2
      ;;
    --iscsi-server)
      iscsi_server="${2}"
      shift 2
      ;;
    --base-iqn)
      base_iqn="${2}"
      shift 2
      ;;
    --)
      shift
      break
      ;;
  esac
done

[[ -x "${nfs_server}" ]]; nfs_server_set=$?
[[ -z "${iscsi_server}" ]]; iscsi_server_set=$?
[[ -z "${base_iqn}" ]]; base_iqn_set=$?

if [[ ${iscsi_server_set} -ne ${base_iqn_set} ]]; then
  echo "Both [iscsi-server] and [base-iqn] must be set" >&2
  exit 1
fi

if [[ ${nfs_server_set} -ne 1 ]] && [[ ${base_iqn_set} -ne 1 ]]; then
  echo "One of [nfs-server] and [base-iqn] must be set" >&2
  exit 1
fi

labels=()
declare -A cmdlines=()
declare -A initrds=()
declare -A kernels=()

if [[ ! -z ${nfs_server} ]]; then
  nfs_shares=($(showmount -e ${nfs_server} | grep -Po '^\/[^\s]+'))
  share_index=0
  nfs_prefix=nfs://${nfs_server}
  tmp_dir=$(mktemp -dp /run/media)
  for nfs_share in ${nfs_shares[@]}; do
    mount ${nfs_server}:${nfs_share} ${tmp_dir}
    if [[ -d ${tmp_dir}/boot/loader/entries ]]; then
      entries=(${tmp_dir}/boot/loader/entries/*.conf)
      for entry in ${entries[@]}; do
        cmdline="$(grep -Po '(?<=options ).*' ${entry}) ip=:::::eth0:dhcp elevator=noop net.ifnames=0 root=${nfs_server}:${nfs_share} nfsroot=${nfs_server}:${nfs_share}"
        kernel="$(grep -Po '(?<=linux ).*' ${entry})"
        initrd="$(grep -Po '(?<=initrd ).*' ${entry})"
        [[ -z ${kernel} ]] && continue
        label=nfs-${nfs_share:1}
        labels+=(${label})
        cmdlines[${label}]="${cmdline}"
        initrds[${label}]="${nfs_prefix}${nfs_share}/boot${initrd}"
        kernels[${label}]="${nfs_prefix}${nfs_share}/boot${kernel}"
        share_index=$((${share_index}+1))
      done
    fi
    sleep 0.1
    umount ${tmp_dir}
  done
  rmdir ${tmp_dir}
fi

if [[ ! -z ${iscsi_server} ]]; then
  iscsi_disks=($(iscsiadm -m discovery -p ${iscsi_server} -t sendtargets | grep -o 'iqn.*' | sort | uniq))
fi
cat << EOF
#!ipxe

EOF
if [[ ! -z ${nfs_server} ]]; then
  echo "set nfs-server ${nfs_server}"
fi
if [[ ! -z ${iscsi_server} ]]; then
  cat << EOF
set iscsi-server ${iscsi_server}
set base-iqn ${base_iqn}
set base-iscsi iscsi:\${iscsi-server}::::\${base-iqn}
isset \${hostname} && set initiator-iqn \${base-iqn}:\${hostname} || set initiator-iqn \${base-iqn}:\${mac}
EOF
fi

cat << EOF
set keep-san 1

set menu-timeout 5000
set submenu-timout \${menu-timeout}

cpuid --ext 29 && set arch x64 || set arch x86
cpuid --ext 29 && set archl amd64 || set archl i386

:start
menu iPXE boot menu for \${initiator-iqn}
EOF
if [[ ${#labels[@]} -ne 0 ]]; then
  echo "item --gap --             ------------------------- NFS Shares -------------------------------------"
  for label in ${labels[@]}; do
    echo "item ${label}             Boot ${label}"
  done
fi
if [[ ${#iscsi_disks[@]} -ne 0 ]]; then
  echo "item --gap --             ------------------------- ISCSI Shares -----------------------------------"
  for (( i=0; i<${#iscsi_disks[@]}; i++ )); do
    echo "item iscsi-${i}              Boot ${iscsi_disks[${i}]}"
  done
fi

cat << EOF
item --gap --             ------------------------- Advanced options -------------------------------
item --key c config       Configure settings
item shell                Drop to iPXE shell
item reboot               Reboot computer
item
item --key x exit         Exit iPXE and continue BIOS boot
choose --timeout \${menu-timeout} --default \${menu-default} selected || goto cancel
set menu-timeout 0
goto \${selected}

:cancel
echo You cancelled the menu, dropping you to a shell

:shell
echo Type 'exit' to get the back to the menu
shell
set menu-timeout 0
set submenu-timeout 0
goto start

:failed
echo Booting failed, dropping to shell
goto shell

:reboot
reboot

:exit
exit

:config
config
goto start
EOF

for label in ${labels[@]}; do
  cat << EOF

:${label}
EOF
  initrd="${initrds[${label}]}"
  [[ -z ${initrd} ]] || echo "initrd ${initrd} || goto failed"
  kernel="${kernels[${label}]}"
  echo "boot ${kernel} ${cmdlines[${label}]} || goto failed"
done

for (( i=0; i<${#iscsi_disks[@]}; i++ )); do
  iscsi_share=${iscsi_disks[${i}]}
  cat << EOF

:iscsi-${i}
echo "Booting ${iscsi_share}"
sanboot ${iscsi_share} || goto failed
EOF
done
