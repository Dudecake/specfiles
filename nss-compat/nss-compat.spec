%global nss_version 3.94

Name:       nss-compat
Version:    %{nss_version}
Release:    1%{?dist}
Summary:    Compatibility package for nss
License:    MIT
Requires:   mozilla-nss%{?_isa} >= %{nss_version}

Provides:   nss >= %{nss_version}
Provides:   nss%{?_isa} >= %{nss_version}

%description
%{summary}

%global debug_package %{nil}

%prep

%build

%install

%files

%changelog
