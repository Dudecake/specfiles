#
# spec file for package cataclysm-dda
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           cataclysm-dda
Version:        0.F_3
Release:        0
Summary:        A roguelike set in a post-apocalyptic world
License:        CC-BY-SA-3.0
Group:          Amusements/Games/RPG
Url:            https://cataclysmdda.org/
Source0:        https://github.com/CleverRaven/Cataclysm-DDA/archive/refs/tags/%(echo "%{version}" | sed "s/_/-/").tar.gz#Cataclysm-DDA-%{version}.tar.gz
Patch0:         remove-github-action-escape.patch
Patch1:         ncursesw-error.patch
Patch2:         disable-werror.patch
Patch3:         https://github.com/CleverRaven/Cataclysm-DDA/commit/b7fe8091780e01143e21e11cb726473ff00f82f8.patch
ExclusiveArch:  x86_64 aarch64
BuildRequires:  astyle
BuildRequires:  gcc-c++ >= 5
BuildRequires:  binutils-gold
BuildRequires:  gettext-tools
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  update-desktop-files
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Cataclysm: Dark Days Ahead is a roguelike set in a post-apocalyptic world.
Struggle to survive in a harsh, persistent, procedurally generated environment.

%lang_package

%package data
Summary:        Cataclysm: DDA data
License:        CC-BY-SA-3.0
Group:          Amusements/Games/RPG
BuildArch:      noarch
Requires:       cataclysm-dda

%description data
Cataclysm: Dark Days Ahead is a roguelike set in a post-apocalyptic world.
Struggle to survive in a harsh, persistent, procedurally generated environment.

This package contains the data files for Cataclysm: Dark Days Ahead.

%prep
%autosetup -p1 -n Cataclysm-DDA-%(echo "%{version}" | sed "s/_/-/")

%define cataopts NATIVE=linux64 RELEASE=1 LTO=1 RUNTESTS=0 USE_XDG_DIR=1
#%%define cataopts NATIVE=linux64 RELEASE=1 USE_XDG_DIR=1

%build
#export CFLAGS="%{optflags}"
#export CXXFLAGS="%{optflags}"
%{make_build} PREFIX=%{_prefix} %{cataopts} PCH=0
%{make_build} PREFIX=%{_prefix} %{cataopts} TILES=1 SOUND=1

%install
#Graphic version of the main file, data file and language file
%{make_install} PREFIX=%{_prefix} %{cataopts} TILES=1 SOUND=1 LANGUAGES=all

#Command line main file
install -Dm755 cataclysm %{buildroot}%{_bindir}/cataclysm

#Document
mkdir -p %{buildroot}%{_docdir}/%{name}
mv .github/CONTRIBUTING.md doc/CONTRIBUTING.md
mv data/json/LOADING_ORDER.md doc/JSON_LOADING_ORDER.md
cp -r doc/* %{buildroot}%{_docdir}/%{name}

#xdg directory
install -D -m 0644 data/xdg/org.cataclysmdda.CataclysmDDA.svg \
            %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.cataclysmdda.CataclysmDDA.svg
install -D -m 0644 data/xdg/org.cataclysmdda.CataclysmDDA.desktop \
            %{buildroot}%{_datadir}/applications/org.cataclysmdda.CataclysmDDA.desktop
install -D -m 0644 data/xdg/org.cataclysmdda.CataclysmDDA.appdata.xml \
            %{buildroot}%{_datadir}/metainfo/org.cataclysmdda.CataclysmDDA.appdata.xml
#Duplicate files
%fdupes -s %{buildroot}%{_datadir}

%suse_update_desktop_file -i org.cataclysmdda.CataclysmDDA
%find_lang %{name}

%files
%defattr(-,root,root)
%license LICENSE.txt
%{_bindir}/cataclysm
%{_bindir}/cataclysm-tiles
%{_datadir}/applications/org.cataclysmdda.CataclysmDDA.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.cataclysmdda.CataclysmDDA.svg
%{_datadir}/metainfo/org.cataclysmdda.CataclysmDDA.appdata.xml

%files lang -f %{name}.lang
%defattr(-,root,root)

%files data
%defattr(644,root,root)
%{_datadir}/%{name}
%{_docdir}/%{name}

%changelog
