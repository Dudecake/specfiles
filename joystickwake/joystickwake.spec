Name:           joystickwake
Version:        0.4.2
Release:        0%{?dist}
Summary:        A joystick-aware screen waker

License:        GPLv3+
URL:            https://github.com/foresto/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  python311
Requires:       python311
Requires:       python311-pyudev
Requires:       xset
Suggests:       xscreensaver-base
Suggests:       mate-screensaver
Suggests:       xfce4-screensaver


BuildArch:      noarch

%description
%{summary}

%prep
%setup -q

%build
python3 -m compileall joystickwake

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}

%files
%license LICENSE
%doc README.rst
%{_bindir}/%{name}
