Name:           patterns-ckoomen
Version:        0.0.24
Release:        1%{?dist}
Summary:        Patterns for openSUSE

License:        EUPL-1.2
Group:          Metapackages
URL:            https://repo.ckoomen.eu/opensuse/

%description
%{summary}

%package base
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_base
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10001
Provides:       pattern-visible()
Requires:       (pattern() = base or pattern() = microos_base)
# Only on leap
%if 0%{?suse_version} < 1599
Requires:       pattern() = microos_container_runtime
%endif
Requires:       bsdtar
Requires:       attr
Requires:       man
Requires:       zsh
Requires:       zsh-syntax-highlighting
Requires:       flatpak-zsh-completion
Requires:       ckoomen-config-zsh
Requires:       ckoomen-utils
Requires:       opendoas
Requires:       sl
Requires:       units
Requires:       git-core
Requires:       arch-install-scripts
Requires:       toolbox
Requires:       podman-compose
Requires:       podman-remote
Requires:       podmansh
Requires:       iperf
Requires:       picocom
Requires:       sbsigntools
Requires:       setroubleshoot
Requires:       setroubleshoot-server
Requires:       systemd-zram-service
Requires:       libiscsi-utils
# IDM
Requires:       freeipa-client
Requires:       oddjob
Requires:       oddjob-mkhomedir
# Network config
Requires:       firewalld
Requires:       firewalld-zsh-completion
Requires:       net-tools
Requires:       bridge-utils
Requires:       wireguard-tools
Requires:       wol
Requires:       ckoomen-config
Requires:       ckoomen-config-network
# Monitoring
Requires:       btop
Requires:       iotop
Requires:       mtr
Requires:       ncdu
Requires:       nmap
Requires:       mlocate

%description base
%{summary}

%package virtualization
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_virtualization
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10002
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_base
%if 0%{?suse_version} < 1599
Requires:       pattern() = microos_kvm_host
%else
Requires:       pattern() = kvm_server
%endif
Requires:       libvirt-client
Requires:       libvirt-daemon-config-network
Requires:       libvirt-daemon-config-nwfilter
Requires:       libvirt-daemon
Requires:       libvirt-daemon-qemu
Requires:       qemu-arm
Requires:       qemu-uefi-aarch64
Requires:       qemu-x86
Requires:       qemu-tools
Requires:       qemu-hw-display-qxl
Requires:       qemu-hw-display-virtio-gpu-pci
Requires:       qemu-hw-usb-host
Requires:       qemu-hw-usb-redirect
Requires:       qemu-ui-spice-app
Requires:       qemu-vhost-user-gpu
Requires:       virt-install
Requires:       libvirt-daemon-driver-storage-gluster
Requires:       libvirt-daemon-driver-storage-iscsi
Requires:       qemu-block-gluster
Requires:       qemu-block-iscsi
Requires:       butane
Requires:       driverctl
Requires:       virtio-win
Requires:       virt-top
Requires:       cloud-hypervisor
Requires:       edk2-cloud-hypervisor
%ifarch x86_64
Requires:       rust-hypervisor-firmware-bin
%endif
Requires:       ipxe-bootimgs
%ifarch x86_64
Requires:       vendor-reset-kmp-default
%endif
# Storage
Requires:       ckoomen-config-dracut
Requires:       zfs
Requires:       zfs-kmp-default
# Temporarily add glusterfs until everything is in ceph
Requires:       glusterfs

%description virtualization
%{summary}

%package iot
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_iot
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10003
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_virtualization
Requires:       tcpdump
# Storage
Requires:       ceph
Requires:       ceph-iscsi
Requires:       ceph-mgr-dashboard
Requires:       ceph-radosgw
Requires:       cephfs-top
Requires:       nfs-ganesha-ceph
%if 0%{suse_version} < 1599
Requires:       nfs-ganesha-glusterfs
%endif
Requires:       targetcli-fb
Requires:       target-isns
Requires:       tcmu-runner
# Kubernetes
Requires:       helm
Requires:       helm-zsh-completion
Requires:       ceph-csi
Requires:       ceph-csi-helm-charts
Requires:       cri-tools
Requires:       cri-o
Requires:       cri-o-kubeadm-criconfig
Requires:       kubernetes1.25-kubeadm

%description iot
%{summary}

%package hw-accel
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_hw_accel
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10004
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_base
%ifarch x86_64
Requires:       libvulkan_intel
Requires:       intel-vaapi-driver
Requires:       libvdpau_va_gl1
%endif
Requires:       libvulkan_lvp
Requires:       libvulkan_radeon
Requires:       libvdpau_radeonsi
Requires:       libvdpau_virtio_gpu
Requires:       Mesa-libRusticlOpenCL
Requires:       clinfo
Requires:       libvirglrenderer1

%description hw-accel
%{summary}

%package desktop
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_desktop
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10004
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_hw_accel
Requires:       pattern() = ckoomen_virtualization
#Requires:       gamescope
Requires:       firejail
Requires:       firejail-zsh-completion
Requires:       firewall-applet
Requires:       maven-wrapper
Requires:       java-17-openjdk
Requires:       java-17-openjdk-devel
Requires:       kdeconnect-kde
Requires:       yakuake
Requires:       ckoomen-config-network-wifi
%ifarch x86_64
Requires:       steam-devices
%endif
# GPU
Requires:       virglrenderer-test-server
Requires:       radeontop
# Applications
Requires:       falkon
Requires:       firefox
Requires:       chromium
Requires:       joystickwake
Requires:       nextcloud-client

%description desktop
%{summary}

%package desktop-applications
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_desktop_applications
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10005
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
# Coding
Requires:       code
Requires:       java-17-openjdk-javadoc
Requires:       java-17-openjdk-src
Requires:       kubernetes-client
# Utils
Requires:       android-tools
Requires:       libcamera-tools
# Applications
%ifarch x86_64
Requires:       discord
%endif
Requires:       keepassxc
Requires:       meld
Requires:       virt-manager
Requires:       virt-viewer
# Media
Requires:       celluloid
Requires:       easyeffects
Requires:       helvum

%description desktop-applications
%{summary}

%package media
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_media
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10006
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
Requires:       gimp
Requires:       krita
Requires:       blender
Requires:       kdenlive
Requires:       ffmpeg
Requires:       kicad

%description media
%{summary}

%package games
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_games
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10007
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
%ifarch x86_64
Requires:       cataclysm-dda
%endif
Requires:       desmume
Requires:       dolphin-emu
Requires:       dosbox
Requires:       endless-sky
Requires:       gamehub
Requires:       mangohud
%ifarch x86_64
Requires:       openclonk
%endif
Requires:       openttd
%ifarch x86_64
Requires:       ppsspp
Requires:       ppsspp-qt
%endif
#Requires:       scorched3d
#Requires:       visualboyadvance-m
Requires:       wesnoth
Requires:       widelands
Requires:       xonotic
%ifarch x86_64
Requires:       heroic
%endif
Requires:       pioneer
Requires:       warsow

%description games
%{summary}

%package plasma
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_plasma
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10008
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
Requires:       (pattern() = kde_plasma or pattern() = microos_kde_desktop)
Requires:       akregator
Requires:       gwenview
Requires:       kamoso
Requires:       krecorder
Requires:       krfb
Requires:       krdc
Requires:       ksshaskpass5

%description plasma
%{summary}

%install
mkdir -p %{buildroot}%{_docdir}/%{name}
PATTERNS='
    base virtualization iot hw-accel desktop desktop-applications media games plasma
'
for i in $PATTERNS; do
    echo "This file marks the pattern $i to be installed." \
        > %{buildroot}%{_docdir}/%{name}/${i}.txt
done

%files base
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/base.txt

%files virtualization
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/virtualization.txt

%files iot
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/iot.txt

%files hw-accel
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/hw-accel.txt

%files desktop
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/desktop.txt

%files desktop-applications
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/desktop-applications.txt

%files media
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/media.txt

%files games
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/games.txt

%files plasma
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/plasma.txt
