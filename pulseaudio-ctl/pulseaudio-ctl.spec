Name:       pulseaudio-ctl
Version:    1.66
Release:    2%{?dist}
Summary:    pulseaudio-ctl
URL:        https://github.com/graysky2/pulseaudio-ctl
License:    MIT
Requires:   bc
Requires:   pulseaudio-libs
Requires:   pulseaudio-utils
BuildArch:  noarch

Source0:    https://github.com/graysky2/pulseaudio-ctl/archive/v%{version}.tar.gz

%description
Control pulseaudio volume from the shell or mapped to keyboard shortcuts

%global debug_package %{nil}

%prep
%autosetup

%build
%make_build

%install
%make_install

%files
%{_bindir}/pulseaudio-ctl
%{_mandir}/man1/pulseaudio-ctl.1.gz
%{_datadir}/pulseaudio-ctl/config.skel
%{_datadir}/zsh/site-functions/_pulseaudio-ctl

%changelog
