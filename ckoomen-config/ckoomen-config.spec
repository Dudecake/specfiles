Name:           ckoomen-config
Version:        0.0.1
Release:        1%{?dist}
Summary:        Config for CKoomen

License:        EUPL-1.2
URL:            https://repo.ckoomen.eu/

BuildArch:      noarch

Requires:       systemd-udev

%description
%{summary}

%package network
Requires:       NetworkManager

%description network
Network config for CKoomen

%package network-wifi
Requires:       ckoomen-config-network
Requires:       iwd

%description network
Wifi config for CKoomen

%install
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/conf.d %{buildroot}%{_sysconfdir}/modules-load.d
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

%files
%{_sysconfdir}/modules-load.d/*

%files network
%{_sysconfdir}/NetworkManager/conf.d/wake_on_lan.conf

%files network-wifi
%{_sysconfdir}/NetworkManager/conf.d/wifi_backend.conf
