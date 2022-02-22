Name:           libgbinder
Version:        1.1.19
Release:        1%{?dist}
Summary:        GLib-style interface to binder

License:        BSD
URL:            https://github.com/mer-hybris/%{name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
Requires:       libglibutil

%description
%{summary}

%package devel
Summary:        GLib-style interface to binder
Requires:       libgbinder = %{version}-%{release}
Requires:       libglibutil-devel
Requires:       pkgconfig

%description devel
%{summary}

%prep
%autosetup

%build
%make_build KEEP_SYMBOLS=1 release pkgconfig

%install
%make_install install-dev
%{__mv} %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}

%files
%license LICENSE
%doc README
%{_libdir}/%{name}.so*

%files devel
%{_prefix}/include/gbinder
%{_libdir}/pkgconfig/%{name}.pc
