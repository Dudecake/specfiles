Name:           libgbinder
Version:        1.1.26
Release:        1%{?dist}
Summary:        GLib-style interface to binder

License:        BSD
URL:            https://github.com/mer-hybris/%{name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libglibutil-devel

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
%{__mkdir} %{buildroot}%{_sysconfdir}
%{__cat} > %{buildroot}%{_sysconfdir}/gbinder.conf <<-EOF
[General]
ApiLevel = 29
EOF

%files
%license LICENSE
%doc README
%{_libdir}/%{name}.so*
%config %{_sysconfdir}/gbinder.conf

%files devel
%{_prefix}/include/gbinder
%{_libdir}/pkgconfig/%{name}.pc
