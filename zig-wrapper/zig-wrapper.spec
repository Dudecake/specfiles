Name:           zig-wrapper
Version:        0.0.5
Release:        3%{?dist}
Summary:        Maven wrapper installer script

License:        EUPL-1.2
URL:            https://github.com/Dudecake/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}

%prep
%autosetup

%install
install -Dm755 zig-wrapper.sh %{buildroot}%{_bindir}/zig-wrapper

%files
%license LICENCE
%doc README.md
%{_bindir}/zig-wrapper
