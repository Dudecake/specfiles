%if 0%{?rhel}
%global distro centos
%elseif 0%{?fedora}
%global distro fedora
%elseif 0%{?mageia}
%global distro mageia
%elseif 0%{?suse_version}
%global distro suse
%endif

Name:           ckoomen-release
Version:        0.0.1
Release:        2%{?dist}
Summary:        RPM Package containing my repository file and GPG Key

License:        EUPL-1.2
URL:            https://repo.ckoomen.eu
Source0:        %{url}/%{distro}/ckoomen.repo
Source1:        %{url}/RPM-GPG-KEY-ckoomen

BuildArch:      noarch

%description
Installs my custom made repo configuration file and GPG key

%install
%__install -Dm644 %{_sourcedir}/ckoomen.repo %{buildroot}%{_sysconfdir}/yum.repos.d/ckoomen.repo
%__install -Dm644 %{_sourcedir}/RPM-GPG-KEY-ckoomen %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ckoomen

%files
#%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/ckoomen.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ckoomen
