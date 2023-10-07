Name:           ckoomen-utils
Version:        0.0.4
Release:        3%{?dist}
Summary:        Utils for CKoomen

License:        EUPL-1.2
URL:            https://repo.ckoomen.eu/
Source0:        generate-ganesha.sh
Source1:        ls-iommu.sh
Source2:        ls-reset.sh
Source3:        generate-extlinuxconf.sh
Source4:        generate-ipxe.sh
Source5:        generate-cephconf.sh
Source6:        init-ceph.sh
Requires:       findutils
Requires:       pciutils

BuildArch:      noarch

%description
%{summary}

%install
%{__install} -Dm755 -t %{buildroot}%{_bindir} %{_sourcedir}/{generate-{cephconf,extlinuxconf,ganesha,ipxe},ls-{iommu,reset},init-ceph}.sh

%files
%{_bindir}/generate-cephconf.sh
%{_bindir}/generate-extlinuxconf.sh
%{_bindir}/generate-ganesha.sh
%{_bindir}/generate-ipxe.sh
%{_bindir}/init-ceph.sh
%{_bindir}/ls-iommu.sh
%{_bindir}/ls-reset.sh
