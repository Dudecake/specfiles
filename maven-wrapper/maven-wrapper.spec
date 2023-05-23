Name:           maven-wrapper
Version:        0.0.1
Release:        1%{?dist}
Summary:        Maven wrapper installer script

License:        EUPL-1.2
URL:            https://repo.ckoomen.eu/
Source0:        maven-wrapper.sh

BuildArch:      noarch

%description
%{summary}

%install
install -Dm755 %{_sourcedir}/maven-wrapper.sh %{buildroot}%{_bindir}/maven-wrapper

%files
%{_bindir}/maven-wrapper
