%define githash 924bb3b41a4126a4c89e4be8779ac014f0d41151

Name:          kube-spawn
Version:       0.2.1
Release:       1.git924bb3b%{?dist}
Summary:       A tool for creating multi-node Kubernetes clusters on a Linux machine using kubeadm & systemd-nspawn. Brought to you by the Kinvolk team. https://kinvolk.io
URL:           https://github.com/kinvolk/kube-spawn
License:       Apache
BuildRequires: docker
Requires:      systemd-container
Requires:      containernetworking-cni
#BuildArch:     noarch

Source0:    %{url}/archive/%{githash}.tar.gz
Source1:    0001-set-cni-dir.patch

%description
Control pulseaudio volume from the shell or mapped to keyboard shortcuts

%global debug_package %{nil}

# %prep
# %autosetup

%build
%__rm -r kube-spawn-%{githash}
%__tar -xf %_sourcedir/%{githash}.tar.gz
cd kube-spawn-%{githash}
%__patch -p1 -i %_sourcedir/0001-set-cni-dir.patch
%__make

%install
#%make_install
cd kube-spawn-%{githash}
#%__install -dm755 %{?buildroot}%{_libexecdir}/kube-spawn/
%__install -dm755 %{?buildroot}/usr/bin/
%__install kube-spawn %{?buildroot}/usr/bin/
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
