Name:           zig-wrapper
Version:        0.0.2
Release:        1%{?dist}
Summary:        Maven wrapper installer script

License:        EUPL-1.2
URL:            https://repo.ckoomen.eu/
Source0:        zig-wrapper.sh

BuildArch:      noarch

%description
%{summary}

%install
install -Dm755 %{_sourcedir}/zig-wrapper.sh %{buildroot}%{_bindir}/zig-wrapper

%files
%{_bindir}/zig-wrapper
