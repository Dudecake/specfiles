Name:       libostree-compat
Version:    2024.6
Release:    1.1%{?dist}
Summary:    Compatibility package for libostree
License:    GPLv2

Requires:   libostree = %{version}

BuildArch:  noarch

Provides:   ostree

%description
%{summary}

%global debug_package %{nil}

%package devel
Summary:    Compatibility package for libostree
Requires:   libostree-devel = %{version}
Requires:   libostree-compat

Provides:   ostree-devel

%description devel
%{summary}

%prep

%build

%install

%files

%files devel

%changelog
