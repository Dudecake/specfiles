%define githash 225a49a40941e350899e456366265cf82b87ad25
%define module_name v4l2loopback

Name:               %{module_name}-dkms
Version:            0.12.5
Release:            1%{?dist}
Summary:            Linux kernel module to create V4L2 loopback devices
URL:                https://github.com/umlaeute/%{module_name}
License:            GPLv2
Requires:           dkms
Requires(post):     dkms
Requires(preun):    dkms

Source0:    %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}

%global debug_package %{nil}

%prep
%autosetup -n %{module_name}-%{version}

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
