%global librepo_version 1.13.1

Name:       librepo-compat
Version:    %{librepo_version}
Release:    1%{?dist}
Summary:    Compatibility package for librepo
License:    MIT
Requires:   lib64repo0%{?_isa} >= %{librepo_version}

Provides:   librepo%{?_isa} >= %{librepo_version}

%description
%{summary}

%global debug_package %{nil}

%prep

%build

%install

%files

%changelog
