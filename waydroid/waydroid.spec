Name:           waydroid
Version:        1.2.0
Release:        2%{?dist}
Summary:        Waydroid uses a container-based approach to boot a full Android system on a regular GNU/Linux system like Ubuntu.

License:        GPLv3+
URL:            https://waydro.id/
Source0:        https://github.com/waydroid/%{name}/archive/refs/tags/%{version}.tar.gz
Patch0:         https://github.com/waydroid/%{name}/commit/71f9249c9e08e9abbd08f6ce95d2906c23cfe433.patch
Patch1:         https://github.com/waydroid/%{name}/commit/9bee074239199570d70630281ff0053253675044.patch

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
%autosetup -p1

%install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications/

cat > %{buildroot}%{_bindir}/%{name} <<-EOF
#!/usr/bin/bash
exec /usr/bin/python %{_datadir}/%{name}/%{name}.py "$@"
EOF

chmod 0755 %{buildroot}/%{_bindir}/%{name}

%{__install} -m 0644 %{name}.py %{buildroot}%{_datadir}/%{name}/
%{__cp} -r tools data %{buildroot}%{_datadir}/%{name}/
%{__mv} %{buildroot}%{_datadir}/%{name}/data/Waydroid.desktop %{buildroot}%{_datadir}/applications/
%{__install} -Dm644 gbinder/anbox.conf -t %{buildroot}%{_sysconfdir}/gbinder.d
%{__install} -Dm644 debian/waydroid-container.service -t %{buildroot}%{_unitdir}

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
%config %{_sysconfdir}/gbinder.d/anbox.conf
%{_unitdir}/waydroid-container.service
