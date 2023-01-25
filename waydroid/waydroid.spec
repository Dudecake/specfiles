Name:           waydroid
Version:        1.3.4
Release:        1%{?dist}
Summary:        Waydroid uses a container-based approach to boot a full Android system on a regular GNU/Linux system like Ubuntu.

License:        GPLv3+
URL:            https://waydro.id/
Source0:        https://github.com/waydroid/%{name}/archive/refs/tags/%{version}.tar.gz

Requires:       lxc
Requires:       python3-gbinder
Requires:       python3-gobject
Requires:       nftables
Requires:       dnsmasq
BuildRequires:  systemd-rpm-macros

BuildArch:      noarch

%description
%{summary}

%prep
%autosetup

%install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications/

cat > %{buildroot}%{_bindir}/%{name} <<-EOF
#!/usr/bin/bash
exec /usr/bin/python %{_datadir}/%{name}/%{name}.py "\\$@"
EOF

chmod 0755 %{buildroot}/%{_bindir}/%{name}

%{__install} -m 0644 %{name}.py %{buildroot}%{_datadir}/%{name}/
%{__cp} -r tools data %{buildroot}%{_datadir}/%{name}/
%{__mv} %{buildroot}%{_datadir}/%{name}/data/Waydroid.desktop %{buildroot}%{_datadir}/%{name}/data/waydroid.market.desktop %{buildroot}%{_datadir}/applications/
%{__install} -Dm 0644 %{buildroot}%{_datadir}/%{name}/data/id.waydro.waydroid.metainfo.xml -t %{buildroot}%{_datadir}/metainfo
%{__rm} %{buildroot}%{_datadir}/%{name}/data/id.waydro.waydroid.metainfo.xml
%{__install} -Dm644 systemd/waydroid-container.service -t %{buildroot}%{_unitdir}

%if 0%{?py_byte_compile:1}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python_Appendix/#manual-bytecompilation
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/Waydroid.desktop
%{_datadir}/applications/waydroid.market.desktop
%{_datadir}/metainfo/id.waydro.waydroid.metainfo.xml
%{_unitdir}/waydroid-container.service
