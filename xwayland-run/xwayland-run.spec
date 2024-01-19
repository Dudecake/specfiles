%define githash c5846bed1d01497c75f8347e4d5dd1077cf171e9

Name:           xwayland-run
Version:        0.0.2
Release:        3gitc5846be%{?dist}
Summary:        xwayland-run contains a set of small utilities revolving around running Xwayland and various Wayland compositor headless.
URL:            https://gitlab.freedesktop.org/ofourdan/%{name}
License:        GPLv2+

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  cage

Requires:  cage

Source:         %{url}/-/archive/%{githash}/xwayland-run-%{githash}.tar.gz

%description
%{summary}

%prep
%autosetup -n %{name}-%{githash}

%build
%meson -Dcompositor=cage
%meson_build

%install
%meson_install

%files
%{_bindir}/xwayland-run
%{_bindir}/wlheadless-run
%{_bindir}/xwfb-run
%{python3_sitelib}/wlheadless
%{_mandir}/man1/wlheadless-run.1*
%{_mandir}/man1/xwayland-run.1*
%{_mandir}/man1/xwfb-run.1*
%{_datadir}/wlheadless/wlheadless.conf
