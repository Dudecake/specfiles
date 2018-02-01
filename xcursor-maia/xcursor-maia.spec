%define maia_commit    45be28a035dfb282879f9ca97a31a7bc2c52e6cd

Name:       xcursor-maia
Version:    20160417
Release:    1%{?dist}
Summary:    Cursor theme - part of the Manjaro Maia set
URL:        https://github.com/manjaro/maia-cursor
License:    GPLv3
Requires:   libXcursor
BuildArch:  noarch

Source0:    https://github.com/manjaro/maia-cursor/archive/%{maia_commit}.tar.gz
Source1:    https://raw.githubusercontent.com/manjaro/packages-community/master/xcursor-maia/thumbnail.png

%description
%{summary}

%global debug_package %{nil}

%prep
%autosetup -c

%install
cd %{_builddir}/%{name}-%{version}/xcursor-maia-%{maia_commit}
%{__install} -dm 755 %{buildroot}%{_datadir}/icons

cp -r Maia-Cursor %{buildroot}%{_datadir}/icons/
cp %{_sourcedir}/thumbnail.png %{buildroot}%{_datadir}/icons/Maia-Cursor/cursors/

%files
%{_datadir}/icons/Maia-Cursor

%changelog
