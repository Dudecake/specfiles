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
Summary:    Production-Grade Container Scheduling and Management
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
%__mkdir -p %{?buildroot}/opt %{?buildroot}/usr/bin
%__cp -a . %{?buildroot}/opt/chectl
cat << EOF >%{?buildroot}/usr/bin/chectl

%files
/opt/chectl
