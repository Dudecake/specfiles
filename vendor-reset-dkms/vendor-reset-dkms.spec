%define githash 4b466e92a2d9f76ce1082cde982c7be0be91e248
%define module_name vendor-reset

Name:               %{module_name}-dkms
Version:            0.1.1
Release:            3.git4b466e9%{?dist}
Summary:            Linux kernel vendor specific hardware reset module
URL:                https://github.com/gnif/%{module_name}
License:            GPLv2
Requires:           dkms
Requires(post):     dkms
Requires(preun):    dkms

Source0:    %{url}/archive/%{githash}.tar.gz

BuildArch:      noarch

%description
%{summary}

%global debug_package %{nil}

%prep
%autosetup -n %{module_name}-%{githash}

%build

%install
%{__mkdir} -p %{?buildroot}%{_usrsrc}/%{module_name}-%{version}
%{__cp} -r . %{?buildroot}%{_usrsrc}/%{module_name}-%{version}

%post -n %{name}
dkms add     -m %{module_name} -v %{version} --rpm_safe_upgrade &&
dkms build   -m %{module_name} -v %{version} --rpm_safe_upgrade &&
dkms install -m %{module_name} -v %{version} --rpm_safe_upgrade --force
true

%preun -n %{name}
dkms remove  -m %{module_name} -v %{version} --rpm_safe_upgrade --all
true

%files
%license LICENSE
%doc README.md
%{_usrsrc}/%{module_name}-%{version}

%changelog
