%define kernel_flavour default

Name:           patterns-ckoomen
Version:        0.0.38
Release:        4%{?dist}
Summary:        Patterns for openSUSE

License:        EUPL-1.2
Group:          Metapackages
URL:            https://repo.ckoomen.eu/opensuse/

%description
%{summary}

%package base-minimal
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_base_minimal
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10001
Provides:       pattern-visible()
Requires:       (pattern() = base or pattern() = microos_base)
%if 0%{?suse_version} < 1599
Requires:       pattern() = microos_container_runtime
%endif
Requires:       bsdtar
Requires:       attr
Requires:       man
Requires:       opendoas
Requires:       git-core
# Shell
Requires:       zsh
Requires:       zsh-syntax-highlighting
Requires:       flatpak-zsh-completion
Requires:       ckoomen-config-zsh

%description base-minimal
%{summary}

%package base
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_base
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10002
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_base_minimal
Requires:       ckoomen-utils
Requires:       sl
Requires:       units
Requires:       qemu-guest-agent
Requires:       picocom
Requires:       sbsigntools
Requires:       systemd-zram-service
Requires:       usbutils
Requires:       libiscsi-utils
# Container support
Requires:       arch-install-scripts
Requires:       qemu-linux-user
Requires:       toolbox
Requires:       podman-compose
Requires:       podman-remote
Requires:       podmansh
# Selinux
Requires:       setroubleshoot
Requires:       setroubleshoot-server
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
Requires:       iperf
Requires:       bind-utils
Requires:       wol
Requires:       ckoomen-config
Requires:       ckoomen-config-network
# Monitoring
Requires:       btop
Requires:       iotop-c
Requires:       mtr
Requires:       ncdu
Requires:       dysk
Requires:       nmap
Requires:       mlocate

%description base
%{summary}

%package virtualization-minimal
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_virtualization_minimal
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10003
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_base_minimal
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
Requires:       qemu-ivshmem-tools
Requires:       qemu-hw-display-qxl
Requires:       qemu-hw-display-virtio-gpu-pci
Requires:       qemu-hw-usb-host
Requires:       qemu-hw-usb-redirect
Requires:       qemu-ui-spice-app
Requires:       qemu-vhost-user-gpu
Requires:       virt-install
Requires:       glusterfs
Requires:       libvirt-daemon-driver-storage-gluster
Requires:       libvirt-daemon-driver-storage-iscsi
Requires:       qemu-block-iscsi
Requires:       butane
Requires:       driverctl
Requires:       virtio-win
Requires:       virt-top
Requires:       cloud-hypervisor
Requires:       edk2-cloud-hypervisor
Requires:       ipxe-bootimgs
%ifarch x86_64
Requires:       qemu-kvm
Requires:       rust-hypervisor-firmware-bin
%endif
Requires:       kubernetes1.30-client
# Storage
Requires:       ckoomen-config-dracut

%description virtualization-minimal
%{summary}

%package virtualization
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_virtualization
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10004
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_base
Requires:       pattern() = ckoomen_virtualization_minimal

Requires:       kernel-%{kernel_flavour}-devel
%ifarch x86_64
Requires:       /usr/bin/readelf
Recommends:     vendor-reset-kmp-%{kernel_flavour}
%endif

%description virtualization
%{summary}

%package iot
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_iot
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10005
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
Requires:       ckoomen-utils-ceph
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
Requires:       kubernetes-kubeadm
Requires:       kompose
%ifarch x86_64
Requires:       katacontainers
%endif
Requires:       kernel-cloud-hypervisor-guest

%description iot
%{summary}

%package hw-accel
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_hw_accel
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10006
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_base_minimal
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
Provides:       pattern-order() = 10007
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_hw_accel
Requires:       pattern() = ckoomen_base
Requires:       gamescope
Requires:       waycheck
Requires:       xwayland-run
Requires:       firejail
Requires:       firejail-zsh-completion
Requires:       firewall-applet
Requires:       filelight
Requires:       kdeconnect-kde
Requires:       ckoomen-config-network-wifi
%ifarch x86_64
Requires:       steam-devices
%endif
# GPU
Requires:       virglrenderer-test-server
Requires:       radeontop
# Applications
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
Provides:       pattern-order() = 10008
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
# Coding
Requires:       code
Requires:       lapce
Requires:       maven-wrapper
Requires:       java-21-openjdk
Requires:       java-21-openjdk-devel
Requires:       java-21-openjdk-javadoc
Requires:       java-21-openjdk-src
Requires:       zig-wrapper
# Utils
Requires:       android-tools
Requires:       libcamera-tools
# Applications
Requires:       falkon
Requires:       firefox
Requires:       mozilla-openh264
Requires:       chromium
%ifarch x86_64
Requires:       discord
%endif
Requires:       meld
Requires:       virt-manager
Requires:       virt-viewer
# Media players
Requires:       celluloid
Requires:       easyeffects
Requires:       qpwgraph

%description desktop-applications
%{summary}

%package media
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_media
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10009
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
Requires:       gimp
Requires:       krita
Requires:       blender
Requires:       kdenlive
Requires:       ffmpeg
Requires:       kicad
Recommends:     FreeCAD

%description media
%{summary}

%package games
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_games
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10010
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
Requires:       desmume
Requires:       dolphin-emu
Requires:       dosbox
Requires:       endless-sky
Requires:       gamehub
Requires:       mangohud
Requires:       openttd
#Requires:       visualboyadvance-m
Requires:       wesnoth
Requires:       widelands
Requires:       xonotic
Requires:       pioneer
Requires:       warsow
%ifarch x86_64
Requires:       cataclysm-dda
Requires:       openclonk
Requires:       ppsspp
Requires:       ppsspp-qt
#Requires:       scorched3d
Requires:       heroic
Requires:       steam
%endif

%description games
%{summary}

%package plasma
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_plasma
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10011
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
Requires:       (pattern() = kde_plasma or pattern() = microos_kde_desktop)
Requires:       ark
Requires:       gwenview
Requires:       okular
Requires:       kamoso
Requires:       kalk
Requires:       krecorder
Requires:       krfb
Requires:       krdc
Requires:       ksshaskpass6
Requires:       pam_kwallet6
Requires:       xwaylandvideobridge

%description plasma
%{summary}

%install
mkdir -p %{buildroot}%{_docdir}/%{name}
PATTERNS='
    base-minimal base virtualization-minimal virtualization iot hw-accel desktop desktop-applications media games plasma
'
for i in $PATTERNS; do
    echo "This file marks the pattern $i to be installed." \
        > %{buildroot}%{_docdir}/%{name}/${i}.txt
done

%files base-minimal
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/base-minimal.txt

%files base
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/base.txt

%files virtualization-minimal
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/virtualization-minimal.txt

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
