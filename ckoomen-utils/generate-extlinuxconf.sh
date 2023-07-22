#!/bin/sh

set -e
if [[ -f /boot/extlinux/extlinux.conf ]]; then
  mv /boot/extlinux/extlinux.conf{,.bak}
fi

set -x
files=(/boot/vmlinuz-*)
first=1
for (( i=${#files[@]}-1; i>=0; i-- )); do
  file=${files[i]}
  kernel=${file:$(expr index "${file}" -)}
  if [[ "${kernel: -1}" -eq "0" ]]; then
    continue
  fi

  if [[ ${first} ]]; then
    cat << EOF > /boot/extlinux/extlinux.conf
TIMEOUT 30
DEFAULT linux-jetson

MENU TITLE p2771-0000 SD Card boot options

LABEL linux-jetson
      MENU LABEL jetson kernel
      LINUX /boot/Image
      APPEND \${cbootargs} root=/dev/mmcblk0p1 rw rootfstype=ext4

LABEL linux-arch
      MENU LABEL linux-arch
      LINUX /boot/Image
      INITRD /boot/initramfs-4.19.4-1-ARCH.img
      FDT /boot/dtbs/nvidia/tegra186-p2771-0000.dtb
#      APPEND \${cbootargs} root=UUID=966073c1-dd7f-4434-bb70-0c988bf63a8b rw rootfstype=ext4
      APPEND console=ttyS0,115200n8 console=tty0 fbcon=map:0 memtype=0 no_console_suspend=1 earlycon=uart8250,mmio32,0x03100000 nvdumper_reserved=0x2772e0000 gpt tegraid=18.1.2.0.0 tegra_keep_boot_clocks maxcpus=6 boot.slot_suffix= boot.ratchetvalues=0.2.1 androidboot.serialno=0324717071984 bl_prof_dataptr=0x10000@0x277040000 sdhci_tegra.en_boot_part_access=1 console=ttyS0 root=/dev/mmcblk2p1 rootwait rw rootfstype=ext4 rd.timeout=90
EOF
    unset first
  fi

  #/usr/src/kernels/${kernel}/scripts/extract-vmlinux ${file} > /boot/Image-${kernel}
  if [[ ! -f /boot/Image-${kernel} ]]; then
    zcat ${file} > /boot/Image-${kernel}
    chmod +x /boot/Image-${kernel}
  fi

  cat << EOF >> /boot/extlinux/extlinux.conf

LABEL linux-${kernel}
      MENU LABEL linux-${kernel}
      LINUX /boot/Image-${kernel}
      INITRD /boot/initramfs-${kernel}.img
      FDTDIR /boot/dtb-${kernel}
#      FDT /boot/dtb-${kernel}/nvidia/tegra186-p2771-0000.dtb
#      APPEND \${cbootargs} root=UUID=966073c1-dd7f-4434-bb70-0c988bf63a8b rw rootfstype=ext4
      APPEND \${cbootargs} console=ttyS0 root=/dev/mmcblk0p1 rd.timeout=90 rw rootfstype=ext4
EOF
done

files=(/boot/Image-*)
for file in ${files}; do
  kernel=${file:$(expr index "${file}" -)}
  if [[ ! -f /boot/vmlinuz-${kernel} ]]; then
    rm ${file}
  fi
done
