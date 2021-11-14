%define githash 7d43285a5054e4b2b18dbba771b57d365943a0f7
%define module_name vendor-reset

Name:               %{module_name}-dkms
Version:            0.1.1
Release:            1.git7d43285%{?dist}
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
