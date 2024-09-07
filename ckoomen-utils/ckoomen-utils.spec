Name:           ckoomen-utils
Version:        0.0.7
Release:        1%{?dist}
Summary:        Utils for CKoomen

License:        EUPL-1.2
URL:            https://repo.ckoomen.eu/
Source1:        ls-iommu.sh
Source2:        ls-reset.sh
Source3:        generate-extlinuxconf.sh
Source4:        generate-ipxe.sh
Source5:        targetcli-add-isos.sh
Requires:       findutils
Requires:       pciutils

BuildArch:      noarch

%description
%{summary}

%package virt
Summary:        Virt utils for CKoomen
Requires:       cloud-hypervisor
Requires:       kernel-cloud-hypervisor-guest
Requires:       podman

%description virt
%{summary}

%package targetcli
Summary:        Targetcli utils for CKoomen

%description targetcli
%{summary}

%package jetson
Summary:        Jetson utils for CKoomen

%description jetson
%{summary}

%install
%{__install} -Dm755 -t %{buildroot}%{_bindir} %{_sourcedir}/{cloud-hypervisor-{container,virtiofs},generate-{extlinuxconf,ipxe},ls-{iommu,reset},targetcli-add-isos}.sh

%files
%{_bindir}/generate-ipxe.sh
%{_bindir}/ls-iommu.sh
%{_bindir}/ls-reset.sh

%files virt
%{_bindir}/cloud-hypervisor-container.sh
%{_bindir}/cloud-hypervisor-virtiofs.sh

%files targetcli
%{_bindir}/targetcli-add-isos.sh

%files jetson
%{_bindir}/generate-extlinuxconf.sh
