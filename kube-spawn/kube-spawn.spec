Name:          kube-spawn
Version:       0.3.0
Release:       1%{?dist}
Summary:       A tool for creating multi-node Kubernetes clusters on a Linux machine using kubeadm & systemd-nspawn. Brought to you by the Kinvolk team. https://kinvolk.io
URL:           https://github.com/kinvolk/%{name}
License:       Apache
BuildRequires: golang
Requires:      systemd-container
Requires:      containernetworking-cni

Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:    0001-set-cni-dir.patch

%description
Control pulseaudio volume from the shell or mapped to keyboard shortcuts

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version} -p1
%__sed -i 's/$(shell git describe --tags --always --dirty)/v%{version}/'

%build
DOCKERIZED=n %__make

%install
#%make_install
#%__install -dm755 %{?buildroot}%{_libexecdir}/kube-spawn/
%__install -Dm755 kube-spawn %{?buildroot}/usr/bin/
#%__install kube-spawn %{?buildroot}%{_libexecdir}/kube-spawn/
#%__cat << EOF > %{?buildroot}usr/bin/kube-spawn
##!/bin/sh
#if [ "$1" = "create" ] || [ "$1" = "start" ]; then
#  exec /usr/libexec/kube-spawn/kube-spawn --cni-plugin-dir /usr/libexec/cni $@
#else
#  exec /usr/libexec/kube-spawn/kube-spawn $@
#fi
#EOF
#%__chmod +x %{?buildroot}%{_bindir}/kube-spawn

%files
%{_bindir}/kube-spawn
#%{_libexecdir}/%{name}/kube-spawn

%changelog
