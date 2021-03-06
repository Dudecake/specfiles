Name:       java-11-compat
Version:    1
Release:    1%{?dist}
Summary:    Compatibility package for Java
License:    GPLv3
Requires:   java-11
Requires:   java-11-headless
BuildArch:  noarch

# provides from java-1.8.0
Provides:   java
Provides:   java-1.8.0
Provides:   java-1.8.0-openjdk
Provides:   java-openjdk
Provides:   jre
Provides:   jre-1.8.0
Provides:   jre-1.8.0-openjdk
Provides:   jre-openjdk
Provides:   libjawt.so()(64bit)
Provides:   libjawt.so(SUNWprivate_1.1)(64bit)
# provides from java-1.8.0-headless
Provides:   /usr/bin/jjs
Provides:   java-1.8.0-headless
Provides:   java-1.8.0-openjdk-headless
Provides:   java-headless
Provides:   java-openjdk-headless
Provides:   jre-1.8.0-headless
Provides:   jre-1.8.0-openjdk-headless
Provides:   jre-headless
Provides:   jre-openjdk-headless
Provides:   libjava.so()(64bit)
Provides:   libjava.so(SUNWprivate_1.1)(64bit)
Provides:   libjsig.so()(64bit)
Provides:   libjvm.so()(64bit)
Provides:   libjvm.so(SUNWprivate_1.1)(64bit)
Provides:   libverify.so()(64bit)
Provides:   libverify.so(SUNWprivate_1.1)(64bit)

%description
%{summary}

%global debug_package %{nil}

%prep

%build

%install

%files

%changelog
