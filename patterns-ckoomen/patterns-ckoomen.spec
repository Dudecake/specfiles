Name:           patterns-ckoomen
Version:        0.0.4
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
Requires:       pattern() = microos_base
# Only on leap
%if 0%{suse_version} < 1599
Requires:       pattern() = microos_container_runtime
%endif
Requires:       bsdtar
Requires:       zsh
Requires:       opendoas
Requires:       sl
Requires:       units
Requires:       arch-install-scripts
Requires:       iperf
Requires:       picocom
Requires:       sbsigntools
Requires:       clevis-dracut
Requires:       setroubleshoot
Requires:       setroubleshoot-server
Requires:       systemd-zram-service
# IDM
Requires:       freeipa-client
Requires:       oddjob
Requires:       oddjob-mkhomedir
# Kernel
Requires:       kernel-firmware-amdgpu
Requires:       kernel-firmware-i915
Requires:       kernel-firmware-intel
Requires:       kernel-firmware-network
# Network config
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
%if 0%{suse_version} < 1599
Requires:       pattern() = microos_kvm_host
#else
Requires:       pattern() = kvm_server
Requires:       libvirt
Requires:       libvirt-daemon-qemu
Requires:       qemu-tools
Requires:       virt-install
%endif
Requires:       libvirt-daemon-driver-storage-gluster
Requires:       butane
Requires:       driverctl
Requires:       virtio-win
Requires:       virt-top
Requires:       cloud-hypervisor
Requires:       edk2-cloud-hypervisor
Requires:       rust-hypervisor-firmware-bin
Requires:       ipxe-bootimgs
Requires:       vendor-reset-kmp-default
# Storage
Requires:       zfs
Requires:       zfs-kmp-default

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
Requires:       nfs-ganesha-ceph
Requires:       glusterfs
Requires:       nfs-ganesha-glusterfs
Requires:       targetcli-fb
Requires:       target-isns
Requires:       tcmu-runner
# Kubernetes
Requires:       helm
Requires:       crio-tools
Requires:       cri-o
Requires:       cri-o-kubeadm-cricon
Requires:       kubernetes-kubeadm

%description iot
%{summary}

%package desktop
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_desktop
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10004
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_virtualization
#Requires:       gamescope
Requires:       firejail
Requires:       firewall-applet
Requires:       java-17-openjdk
Requires:       java-17-openjdk-devel
Requires:       java-17-openjdk-javadoc
Requires:       java-17-openjdk-src
Requires:       kdeconnect-kde
Requires:       yakuake
Requires:       ckoomen-config-network-wifi
# Utils
Requires:       android-tools
Requires:       libcamera-tools
# GPU
Requires:       libvulkan_intel
Requires:       libvulkan_lvp
Requires:       libvulkan_radeon
Requires:       Mesa-libRusticlOpenCL
Requires:       clinfo
Requires:       virglrenderer
Requires:       virglrenderer-test-server
Requires:       radeontop
# Applications
Requires:       discord
Requires:       gimp
Requires:       krita
Requires:       falkon
Requires:       chromium
Requires:       code
Requires:       joystickwake
Requires:       waydroid
Requires:       keepassxc
Requires:       meld
Requires:       nextcloud-client
Requires:       virt-manager
Requires:       virt-viewer
# Media
Requires:       blender
Requires:       celluloid
Requires:       easyeffects
Requires:       ffmpeg
Requires:       helvum
Requires:       kdenlive

%description desktop
%{summary}

%package games
Summary:        openSUSE base CKoomen pattern
Group:          Metapackages
Provides:       pattern() = ckoomen_desktop
Provides:       pattern-category() = CKoomen
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 10005
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
Requires:       cataclysm-dda
Requires:       desmume
Requires:       dolphin-emu
Requires:       dosbox
Requires:       endless-sky
Requires:       gamehub
Requires:       mangohud
#Requires:       openclonk
Requires:       openttd
Requires:       ppsspp
Requires:       ppsspp-qt
#Requires:       scorched3d
#Requires:       visualboyadvance-m
Requires:       wesnoth
Requires:       widelands
Requires:       xonotic
%ifarch x86_64
Requires:       heroic
Requires:       steam-devices
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
Provides:       pattern-order() = 10006
Provides:       pattern-visible()
Requires:       pattern() = ckoomen_desktop
Requires:       pattern() = microos_kde_desktop
Requires:       akregator
Requires:       kamoso
Requires:       krecorder
Requires:       krfb
Requires:       krdc

%description plasma
%{summary}

%install
mkdir -p %{buildroot}%{_docdir}/%{name}
PATTERNS='
    base virtualization iot desktop games plasma
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

%files desktop
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/desktop.txt

%files games
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/games.txt

%files plasma
%dir %{_docdir}/patterns-ckoomen
%{_docdir}/patterns-ckoomen/plasma.txt
