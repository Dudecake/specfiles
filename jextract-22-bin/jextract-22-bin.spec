%define jdk_version 22

Name:               jextract
Version:            %{jdk_version}
Release:            4_30.0%{?dist}
Summary:            Native library binding extraction tool.
URL:                https://github.com/openjdk/%{name}
License:            GPLv2

Source0:            https://download.java.net/java/early_access/%{name}/%{jdk_version}/4/openjdk-%{jdk_version}-%{name}+4-30_linux-x64_bin.tar.gz
ExclusiveArch:      x86_64

Requires:           java-%{jdk_version}-openjdk

%description
%{summary}

%global debug_package %{nil}

%prep

%build

%install
%{__tar} -C /opt -xzf %{source0}

%files
/opt/%{name}-%{jdk_version}
