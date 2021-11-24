Name:           ckoomen-release
Version:        0.0.1
Release:        1%{?dist}
Summary:        RPM Package containing my repository file and GPG Key

License:        EUPL-1.2
URL:            http://repo.ckoomen.eu
Source0:        %{url}/fedora/ckoomen.repo
Source1:        %{url}/fedora/RPM-GPG-KEY-ckoomen

%description
Installs my custom made repo configuration file and GPG key

%install
%__install -Dm644 %{Source0} %{buildroot}%{_sysconfdir}/yum.repos.d/ckoomen.repo
%__install -Dm644 %{Source1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ckoomen

%files
#%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/ckoomen.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ckoomen
