%define githash   33a9af7e326aa2544364a9b79a16570570f1934f
%define shorthash 33a9af7

Name:           x11spice
Version:        1.2
Release:        4.git%{shorthash}%{?dist}
Summary:        x11spice connects a running X server as a Spice server.
URL:            https://gitlab.freedesktop.org/spice/%{name}
License:        GPLv3
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  xorg-x11-util-macros
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(spice-server)
BuildRequires:  pkgconfig(spice-protocol)
BuildRequires:  pkgconfig(pixman-1)

Source0: %{url}/-/archive/%{githash}/%{name}-%{githash}.tar.gz

%description
Connects a running X server as a Spice server.

%prep
%autosetup -n %{name}-%{githash}
./autogen.sh
%configure

%build
%make_build

%install
%make_install

%files
%doc README
%{_bindir}/x11spice*
%{_mandir}/man1/x11spice.1.*
%{_datadir}/applications/x11spice.desktop
%{_datadir}/icons/hicolor/scalable/apps/x11spice.svg
%dir /etc/xdg/x11spice
%config /etc/xdg/x11spice/x11spice.conf
