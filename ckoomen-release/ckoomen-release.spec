Name:           ckoomen-release
Version:        0.0.1
Release:        1%{?dist}
Summary:        RPM Package containing my repository file and GPG Key

License:        EUPL-1.2
URL:            http://repo.ckoomen.eu
Source0:        http://repo.ckoomen.eu/fedora/ckoomen.repo
Source1:        http://repo.ckoomen.eu/fedora/RPM-GPG-KEY-ckoomen

%description
Installs my custom made repo configuration file and GPG key

%install
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d/
mkdir -p %{buildroot}%{_sysconfdir}/pki/rpm-gpg/
cp -p %{_sourcedir}/ckoomen.repo %{buildroot}%{_sysconfdir}/yum.repos.d/
cp -p %{_sourcedir}/RPM-GPG-KEY-ckoomen %{buildroot}%{_sysconfdir}/pki/rpm-gpg/

%files
#%defattr(-,root,root,-)
/etc/yum.repos.d/ckoomen.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-ckoomen
