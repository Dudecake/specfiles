Name:           ckoomen-config
Version:        0.0.8
Release:        3%{?dist}
Summary:        Config for CKoomen

License:        EUPL-1.2
URL:            https://repo.ckoomen.eu/
Source0:        zshrc

BuildArch:      noarch

%if 0%{?suse_version}
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

%package zsh
Summary:        Zsh config for CKoomen
Requires:       zsh

%description zsh
Zsh config for CKoomen

%install
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/conf.d \
        %{buildroot}%{_sysconfdir}/modules-load.d \
        %{buildroot}%{_sysconfdir}/ld.so.conf.d \
        %{buildroot}%{_sysconfdir}/dracut.conf.d \
        %{buildroot}%{_sysconfdir}/skel

cp %{_sourcedir}/wifi_backend.conf %{buildroot}%{_sysconfdir}/NetworkManager/conf.d/wifi_backend.conf
cp %{_sourcedir}/wake_on_lan.conf %{buildroot}%{_sysconfdir}/NetworkManager/conf.d/wake_on_lan.conf
cp %{_sourcedir}/modules-load-dropin.conf %{buildroot}%{_sysconfdir}/modules-load.d/99-dudecake.conf
cp %{_sourcedir}/dracut-dropin.conf %{buildroot}%{_sysconfdir}/dracut.conf.d/99-dudecake.conf
cat << EOF > %{buildroot}%{_sysconfdir}/ld.so.conf.d/jack.conf
%{_libdir}/pipewire-0.3/jack
EOF
cp %{_sourcedir}/zshrc %{buildroot}%{_sysconfdir}/skel/.zshrc

%files
%config %{_sysconfdir}/modules-load.d/99-ckoomen.conf
%config %{_sysconfdir}/ld.so.conf.d/jack.conf

%files network
%config %{_sysconfdir}/NetworkManager/conf.d/wake_on_lan.conf

%files network-wifi
%config %{_sysconfdir}/NetworkManager/conf.d/wifi_backend.conf

%files dracut
%config %{_sysconfdir}/dracut.conf.d/99-ckoomen.conf

%files zsh
%{_sysconfdir}/skel/.zshrc
