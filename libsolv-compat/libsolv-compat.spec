%global libsolv_version 0.7.21

Name:       libsolv-compat
Version:    %{libsolv_version}
Release:    1%{?dist}
Summary:    Compatibility package for libsolv
License:    MIT
Requires:   lib64solv1%{?_isa} >= %{libsolv_version}

Provides:   libsolv%{?_isa} >= %{libsolv_version}

%description
%{summary}

%global debug_package %{nil}

%prep

%build

%install

%files

%changelog
