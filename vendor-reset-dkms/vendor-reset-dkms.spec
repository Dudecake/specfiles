%define githash 225a49a40941e350899e456366265cf82b87ad25
%define module_name vendor-reset

Name:               %{module_name}-dkms
Version:            0.1.1
Release:            1.git225a49a%{?dist}
Summary:            Linux kernel vendor specific hardware reset module
URL:                https://github.com/gnif/vendor-reset
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
%{_usrsrc}/%{module_name}-%{version}

%changelog
