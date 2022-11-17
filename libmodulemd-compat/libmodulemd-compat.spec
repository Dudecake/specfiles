%global libmodulemd_version 2.13.0

Name:       libmodulemd-compat
Version:    %{libmodulemd_version}
Release:    1%{?dist}
Summary:    Compatibility package for libmodulemd
License:    MIT
Requires:   lib64modulemd2%{?_isa} >= %{libmodulemd_version}

Provides:   libmodulemd%{?_isa} >= %{libmodulemd_version}

%description
%{summary}

%global debug_package %{nil}

%prep

%build

%install

%files

%changelog
