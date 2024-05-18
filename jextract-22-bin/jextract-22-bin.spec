%define jdk_version 22

Name:               jextract-%{jdk_version}-bin
Version:            %{jdk_version}
Release:            4_30.0%{?dist}
Summary:            Native library binding extraction tool.
URL:                https://github.com/openjdk/jextract
License:            GPLv2

Source0:            https://download.java.net/java/early_access/jextract/%{jdk_version}/4/openjdk-%{jdk_version}-jextract+4-30_linux-x64_bin.tar.gz
ExclusiveArch:      x86_64

Requires:           java-%{jdk_version}-openjdk

%description
%{summary}

%global debug_package %{nil}

%prep

%build

%install
mkdir -p %{?buildroot}/opt
%{__tar} -C %{?buildroot}/opt -xzf %{SOURCE0}

%files
/opt/jextract-%{jdk_version}
