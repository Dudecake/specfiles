#!/bin/sh

for iommu_group in $(find /sys/kernel/iommu_groups/ -maxdepth 1 -mindepth 1 -type d | sort -n -t / -k 5); do
    echo "IOMMU group $(basename "$iommu_group")"
    for device in $(ls -1 "$iommu_group"/devices/); do
        echo -n $'\t'
        lspci -nns "$device"
    done
done
