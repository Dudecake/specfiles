Name:           helvum
Version:        0.3.2
Release:        1%{?dist}
Summary:        GTK-based patchbay for pipewire, inspired by the JACK tool catia

License:        GPLv3
URL:            https://gitlab.freedesktop.org/pipewire/%{name}
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  rust
BuildRequires:  gtk4-devel
BuildRequires:  pipewire-devel

%description
%{summary}

%prep
%autosetup -c

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.*
