Name:           ckoomen-utils
Version:        0.0.1
Release:        1%{?dist}
Summary:        Utils for CKoomen

License:        EUPL-1.2
URL:            https://repo.ckoomen.eu/
Source0:        generate-ganesha.sh
Source1:        ls-iommu.sh
Source2:        ls-reset.sh
Requires:       findutils
Requires:       pciutils

BuildArch:      noarch

%description
%{summary}

%install
%{__install} -Dm755 -t %{buildroot}%{_bindir} %{_sourcedir}/{generate-ganesha,ls-{iommu,reset}}.sh

%files
%{_bindir}/generate-ganesha.sh
%{_bindir}/ls-iommu.sh
%{_bindir}/ls-reset.sh
