Name:           libglibutil
Version:        1.0.71
Release:        1%{?dist}
Summary:        Library of glib utilities

License:        BSD
URL:            https://github.com/sailfishos/%{name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  glib2-devel
%if 0%{?suse_version}
BuildRequires:  linux-glibc-devel
%endif
Requires:       glib2

%description
%{summary}

%package devel
Summary:        Python bindings for libgbinder
Requires:       libglibutil = %{version}-%{release}
Requires:       glib2-devel
Requires:       pkgconfig

%description devel
%{summary}

%prep
%autosetup

%build
%make_build KEEP_SYMBOLS=1 LIBDIR=%{_libdir} release pkgconfig

%install
%make_install install-dev
%{__mv} %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}

%files
%license LICENSE
%doc README
%{_libdir}/%{name}.so*

%files devel
%{_prefix}/include/gutil
%{_libdir}/pkgconfig/%{name}.pc
