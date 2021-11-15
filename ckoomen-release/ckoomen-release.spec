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
%__install -Dm644 ckoomen.repo %{buildroot}%{_sysconfdir}/yum.repos.d/
%__install -Dm644 RPM-GPG-KEY-ckoomen %{buildroot}%{_sysconfdir}/pki/rpm-gpg/

%files
#%defattr(-,root,root,-)
/etc/yum.repos.d/ckoomen.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-ckoomen
