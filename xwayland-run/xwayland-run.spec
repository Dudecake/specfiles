%define githash c5846bed1d01497c75f8347e4d5dd1077cf171e9

Name:           xwayland-run
Version:        0.0.2
Release:        6gitc5846be%{?dist}
Summary:        xwayland-run contains a set of small utilities revolving around running Xwayland and various Wayland compositor headless.
URL:            https://gitlab.freedesktop.org/ofourdan/%{name}
License:        GPLv2+

BuildRequires:  git-core
BuildRequires:  python3-devel
Requires:       (weston or cage or kwin6 or kwin5 or mutter or gnome-kiosk)
Requires:       xorg-x11-server-wayland

# Provide names of the other utilities included
Provides:       wlheadless-run = %{version}-%{release}
Provides:       xwfb-run = %{version}-%{release}

BuildArch:      noarch

Source:         %{url}/-/archive/%{githash}/xwayland-run-%{githash}.tar.gz

%description
%{summary}

%prep
%autosetup -n %{name}-%{githash}

%build
%meson -Dcompositor=kwin
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
