%define githash 594d19220b679105ba7fd34bf17da98b652050a7
%define dracutlibdir %{_prefix}/lib/dracut

Name:       glusterfs-dracut
Version:    0.0.1
Release:    3.git594d192%{?dist}
Summary:    GlusterFS Client Dracut Module
URL:        https://github.com/stracy-esu/dracut-glusterfs
License:    MIT
Requires:   dracut-network
Requires:   glusterfs-fuse
Requires:   gawk
Requires:   which

Source0:    %{url}/archive/%{githash}.tar.gz

BuildArch:      noarch

%description
Dracut module to mount GlusterFS volumes during early boot

%global debug_package %{nil}

%prep
%autosetup -n dracut-glusterfs-%{githash}

%install
%__install -Dm755 99glusterfs/module-setup.sh %{?buildroot}%{dracutlibdir}/modules.d/99glusterfs/module-setup.sh

%files
%license LICENSE
%doc README.md
%{dracutlibdir}/modules.d/99glusterfs
