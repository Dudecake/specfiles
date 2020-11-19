Name:           joystickwake
Version:        0.2.4
Release:        1%{?dist}
Summary:        A joystick-aware screen waker

License:        GPLv3+
URL:            https://github.com/foresto/joystickwake
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  python
Requires:       python
Requires:       xorg-x11-server-utils
Requires:       python3-pyudev

BuildArch:      noarch

%description
%{summary}

%prep
%setup -q

%build
python -m compileall joystickwake

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}

%files
%{_bindir}/%{name}
