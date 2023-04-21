Name:           ckoomen-config
Version:        0.0.2
Release:        1%{?dist}
Summary:        Config for CKoomen

License:        EUPL-1.2
URL:            https://repo.ckoomen.eu/

BuildArch:      noarch

%if 0%{suse_version}
Requires:       udev
%else
Requires:       systemd-udev
%endif

%description
%{summary}

%package network
Summary:        Network config for CKoomen
Requires:       NetworkManager

%description network
Network config for CKoomen

%package network-wifi
Summary:        Wifi config for CKoomen
Requires:       ckoomen-config-network
Requires:       iwd

%description network-wifi
Wifi config for CKoomen

%package dracut
Summary:        Dracut config for CKoomen
Requires:       ckoomen-config
Requires:       dracut

%description dracut
Dracut config for CKoomen

%install
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/conf.d %{buildroot}%{_sysconfdir}/modules-load.d %{buildroot}%{_sysconfdir}/dracut.conf.d
cat << EOF > %{buildroot}%{_sysconfdir}/NetworkManager/conf.d/wifi_backend.conf
[device]
wifi.backend=iwd
EOF
cat << EOF > %{buildroot}%{_sysconfdir}/NetworkManager/conf.d/wake_on_lan.conf
[connection]
ethernet.wake-on-lan=magic
EOF
cat << EOF > %{buildroot}%{_sysconfdir}/modules-load.d/99-ckoomen.conf
vfio
vfio_iommu_type1
vfio_pci
EOF
cat << EOF > %{buildroot}%{_sysconfdir}/dracut.conf.d/99-ckoomen.conf
omit_dracutmodules+=" clevis network zfs "
EOF

%files
%config %{_sysconfdir}/modules-load.d/99-ckoomen.conf

%files network
%config %{_sysconfdir}/NetworkManager/conf.d/wake_on_lan.conf

%files network-wifi
%config %{_sysconfdir}/NetworkManager/conf.d/wifi_backend.conf

%files dracut
%config %{_sysconfdir}/dracut.conf.d/10-ckoomen.conf
