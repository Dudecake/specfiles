%if 0%{?rhel}
%global distro centos
%elif 0%{?fedora}
%global distro fedora
%elif%{?mageia}
%global distro mageia
%elif%{?suse_version}
%global distro suse
%endif

Name:           ckoomen-release
Version:        0.0.1
Release:        1%{?dist}
Summary:        RPM Package containing my repository file and GPG Key

License:        EUPL-1.2
URL:            http://repo.ckoomen.eu
Source0:        %{url}/%{distro}/ckoomen.repo
#Source1:        %{url}/RPM-GPG-KEY-ckoomen

%description
Installs my custom made repo configuration file and GPG key

%install
%__install -Dm644 %{Source0} %{buildroot}%{_sysconfdir}/yum.repos.d/ckoomen.repo
%__install -Dm644 %{Source1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ckoomen

%files
#%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/ckoomen.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ckoomen
