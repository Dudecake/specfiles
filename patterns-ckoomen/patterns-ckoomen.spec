%define kernel_flavour default

Name:           patterns-ckoomen
Version:        0.0.41
Release:        12%{?dist}
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
# Network config
Requires:       bind-utils
# Monitoring
Requires:       btop
Requires:       iotop-c
Requires:       mtr
Requires:       ncdu
Requires:       dysk
Requires:       nmap
Requires:       mlocate
Requires:       tree

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
Requires:       udisks2
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
# For ipa-client-install
Requires:       python3-ifaddr
Requires:       oddjob
Requires:       oddjob-mkhomedir
# Network config
Requires:       firewalld
Requires:       firewalld-zsh-completion
Requires:       bridge-utils
Requires:       wireguard-tools
Requires:       iperf
Requires:       wol
Requires:       ckoomen-config
Requires:       ckoomen-config-network

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
Requires:       (pattern() = microos_kvm_host or pattern() = kvm_server)
Requires:       libvirt-client
Requires:       libvirt-daemon-config-network
Requires:       libvirt-daemon-config-nwfilter
Requires:       libvirt-daemon
Requires:       libvirt-daemon-qemu
Requires:       qemu-linux-user
Requires:       qemu-arm
Requires:       qemu-uefi-aarch64
Requires:       qemu-x86
Requires:       qemu-tools
Requires:       qemu-ivshmem-tools
Requires:       qemu-hw-display-qxl
Requires:       qemu-hw-display-virtio-gpu-pci
Requires:       qemu-hw-usb-host
Requires:       qemu-hw-usb-redirect
Requires:       qemu-vhost-user-gpu
Requires:       virt-install
Requires:       libvirt-daemon-driver-storage-iscsi
Requires:       qemu-block-iscsi
Requires:       driverctl
Requires:       virtio-win
Requires:       cloud-hypervisor
Requires:       edk2-cloud-hypervisor
Requires:       kernel-cloud-hypervisor-guest
Requires:       ipxe-bootimgs
%ifarch x86_64
Requires:       qemu-kvm
Requires:       rust-hypervisor-firmware-bin
%endif
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

Requires:       qemu-ui-spice-app
Requires:       glusterfs
Requires:       libvirt-daemon-driver-storage-gluster
Requires:       virt-top
Requires:       kernel-%{kernel_flavour}-devel
Requires:       mtools
Requires:       /usr/bin/ukify
# For ukify
Requires:       python3-pefile
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
# DHCP
Requires:       bind
Requires:       kea
Requires:       tftp
# Storage
Requires:       zfs
Requires:       zfstools
Requires:       targetcli-fb
Requires:       ckoomen-utils-targetcli
Requires:       target-isns
Requires:       tcmu-runner

%description iot
%{summary}

%package kubernetes
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_kubernetes
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10006
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_iot
Requires:       helm
Requires:       helm-zsh-completion
Requires:       cri-tools
Requires:       cri-o
Requires:       cri-o-kubeadm-criconfig
Requires:       kubernetes-kubeadm
Requires:       kompose
%ifarch x86_64
Recommends:       katacontainers
%endif

%description kubernetes
%{summary}

%package hw-accel
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_hw_accel
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10007
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
Requires:       vulkan-validationlayers

%description hw-accel
%{summary}

%package desktop
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_desktop
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10008
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
Requires:       /usr/bin/fusermount
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
Provides:       pattern-order() = 10009
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
# Coding
Requires:       code
Requires:       lapce
Requires:       zed
Requires:       maven-wrapper
Requires:       java-21-openjdk
Requires:       java-21-openjdk-devel
Requires:       java-21-openjdk-javadoc
Requires:       java-21-openjdk-src
Requires:       java-21-openjdk-jmods
# For openjfx
Requires:       libgthread-2_0-0
Requires:       zig-wrapper
Requires:       osc
Requires:       build
Requires:       python3-keyring
Requires:       obs-service-format_spec_file
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
Provides:       pattern-order() = 10010
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
Provides:       pattern-order() = 10011
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
Provides:       pattern-order() = 10012
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
Requires:       (pattern() = kde_plasma or pattern() = microos_kde_desktop)
Requires:       ark
Requires:       gwenview
Requires:       okular
Requires:       kamoso
Requires:       kalk
Requires:       krecorder
Requires:       krdp6
Requires:       krfb
Requires:       krdc
Requires:       ksshaskpass6
Requires:       pam_kwallet6
Requires:       xwaylandvideobridge

%description plasma
%{summary}

%package cosmic
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_cosmic
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10013
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
Requires:       cosmic-desktop

%description cosmic
%{summary}

%install
mkdir -p %{buildroot}%{_docdir}/%{name}
PATTERNS='
    base-minimal base virtualization-minimal virtualization iot kubernetes hw-accel desktop desktop-applications media games plasma cosmic
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

%files kubernetes
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/kubernetes.txt

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

%files cosmic
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/cosmic.txt
