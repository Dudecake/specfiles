%define basearch %_arch
%if "%{basearch}" == "x86_64"
%define basearch x64
%endif
%if "%{basearch}" == "aarch64"
%define basearch arm64
%endif

Name:       chectl-bin
Version:    7.61.0
Release:    1%{?dist}
Summary:    Production-Grade Container Scheduling and Management
URL:        https://github.com/che-incubator/chectl
License:    EPL-2.0

Source0:    %{url}/releases/download/%{version}/chectl-linux-%{basearch}.tar.gz

Provides:   chectl = %{version}

%description

%global debug_package %{nil}

%prep
%autosetup -n chectl

%build

%install
%__mkdir -p %{?buildroot}/opt
%__cp -a . %{?buildroot}/opt/chectl

%files
/opt/chectl
