%define basearch ppc64le
%ifarch x86_64
%define basearch x64
%endif
%ifarch aarch64
%define basearch arm64
%endif

Name:       chectl-bin
Version:    7.74.0
Release:    1%{?dist}
Summary:    CLI to manage Eclipse Che server and workspaces
URL:        https://github.com/che-incubator/chectl
License:    EPL-2.0

Source0:    %{url}/releases/download/%{version}/chectl-linux-%{basearch}.tar.gz
ExclusiveArch: x86_64 aarch64 ppc64le

Provides:   chectl = %{version}

%description

%global debug_package %{nil}

%prep
%autosetup -n chectl

%build

%install
%__mkdir -p %{?buildroot}/opt %{?buildroot}%{_bindir}
%__cp -a . %{?buildroot}/opt/chectl
cat << EOF > %{?buildroot}%{_bindir}/chectl
#!/bin/sh
exec /opt/chectl/chectl "\$@"
EOF
chmod +x %{?buildroot}%{_bindir}/chectl

%files
%{_bindir}/chectl
/opt/chectl
