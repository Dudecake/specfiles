%define vertex_commit  31e46d7297a3bc729fbe4f40e75692fe764aed27
%define gnomever       3.22

Name:       vertex-maia-icon-theme
Version:    20180118
Release:    1%{?dist}
Summary:    menda-maia-theme
URL:        https://github.com/manjaro/vertex-maia-icon-themes
License:    GPL
Requires:   hicolor-icon-theme
BuildArch:  noarch

Source0:    https://github.com/manjaro/vertex-maia-icon-themes/archive/%{vertex_commit}.tar.gz

%description
Icons matching Vertex Maia themes, based on Menda Circle

%global debug_package %{nil}

%prep
%autosetup -c

%install
cd %{_builddir}/%{name}-%{version}/vertex-maia-icon-themes-%{vertex_commit}
%{__install} -dm 755 %{buildroot}%{_datadir}/icons

cp -r Vertex-Maia %{buildroot}%{_datadir}/icons/

%files
%{_datadir}/icons/Vertex-Maia

%changelog
