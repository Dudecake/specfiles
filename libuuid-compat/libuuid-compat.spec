%global libuuid_version 2.39.2

Name:       libuuid-compat
Version:    %{libuuid_version}
Release:    2%{?dist}
Summary:    Compatibility package for libuuid
License:    MIT
Requires:   libuuid1%{?_isa} >= %{libuuid_version}

Provides:   libuuid >= %{libuuid_version}
Provides:   libuuid%{?_isa} >= %{libuuid_version}

%description
%{summary}

%global debug_package %{nil}

%prep

%build

%install

%files

%changelog
