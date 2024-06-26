Name:       java-17-compat
Version:    1
Release:    3%{?dist}
Summary:    Compatibility package for Java
License:    GPLv3
Requires:   java-17
Requires:   %{name}-headless

BuildArch:  noarch

Provides:   java = 1.8.0
Provides:   java = 11
Provides:   java-1.8.0
Provides:   java-1.8.0-openjdk
Provides:   java-11
Provides:   java-11-openjdk
Provides:   java-openjdk
Provides:   jre = 1.8.0
Provides:   jre = 11
Provides:   jre-1.8.0
Provides:   jre-1.8.0-openjdk
Provides:   jre-11
Provides:   jre-11-openjdk
Provides:   jre-openjdk = 1.8.0
Provides:   jre-openjdk = 11
Provides:   libjawt.so(SUNWprivate_1.1)(64bit)

%description
%{summary}

%global debug_package %{nil}

%package headless
Summary:    Compatibility package for Java
Requires:   java-17-headless

Provides:   /usr/bin/jjs
Provides:   java-1.8.0-headless
Provides:   java-1.8.0-openjdk-headless
Provides:   java-11-headless
Provides:   java-11-openjdk-headless
Provides:   java-headless = 1.8.0
Provides:   java-openjdk-headless = 1.8.0
Provides:   java-headless = 11
Provides:   java-openjdk-headless = 11
Provides:   jre-1.8.0-headless
Provides:   jre-1.8.0-openjdk-headless
Provides:   jre-11-headless
Provides:   jre-11-openjdk-headless
Provides:   jre-headless = 1.8.0
Provides:   jre-openjdk-headless = 1.8.0
Provides:   jre-headless = 11
Provides:   jre-openjdk-headless = 11
Provides:   libjava.so(SUNWprivate_1.1)(64bit)
Provides:   libverify.so(SUNWprivate_1.1)(64bit)

%description headless
%{summary}

%prep

%build

%install

%files

%files headless

%changelog
