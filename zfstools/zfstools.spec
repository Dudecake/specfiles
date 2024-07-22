# Generated from zfstools-0.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name zfstools
%define mod_name zfstools
%define mod_full_name %{mod_name}-%{version}
%if 0%{?suse_version}
%define gem_instdir %{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}
%define gem_docdir %{_defaultdocdir}/%{rb_default_ruby_suffix}-rubygem-%{mod_name}
%define gem_spec %{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_full_name}.gemspec
%define gem_libdir %{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/lib
%define gem_cache %{_libdir}/ruby/gems/%{rb_ver}/cache
%endif

Name: rubygem-%{gem_name}
Version: 0.3.2
Release: 2%{?dist}
Summary: ZFSTools
License: BSD
URL: https://github.com/bdrewery/%{gem_name}
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?suse_version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  update-alternatives
Group:          Development/Languages/Ruby
PreReq:         update-alternatives
%endif
%if 0%{?fedora} || 0%{?centos}
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(rspec) >= 2.8.0
# BuildRequires: rubygem(rspec) < 2.9
# BuildRequires: rubygem(yard) >= 0.7
# BuildRequires: rubygem(yard) < 1
# BuildRequires: rubygem(cucumber)
# BuildRequires: rubygem(jeweler) >= 1.8.3
# BuildRequires: rubygem(jeweler) < 1.9
# BuildRequires: rubygem(simplecov)
%endif
Provides: %{mod_name}
BuildArch: noarch

%description
ZFS admin scripts, such as automatic snapshots, mysql snapshotting, scrubbing,
etc.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%if 0%{?fedora} || 0%{?centos}
%setup -q -n %{gem_name}-%{version}
%endif

%build
%if 0%{?fedora} || 0%{?centos}
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install
%endif

%install
%if 0%{?fedora} || 0%{?centos}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%endif
%if 0%{?suse_version}
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE.txt README.md README.rdoc" \
  -f

%gem_packages
%endif
%if 0%{?fedora} || 0%{?centos}
%check
pushd .%{gem_instdir}
# cucumber
# rspec spec
popd
%endif

%files
%dir %{gem_instdir}
%{_bindir}/zfs-auto-snapshot*
%{_bindir}/zfs-cleanup-snapshots*
%{_bindir}/zfs-snapshot-mysql*
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/VERSION
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%exclude %{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/features
%{gem_instdir}/spec
%{gem_instdir}/zfstools.gemspec

%changelog
* Mon Nov 16 2020 Dudecake <coen_koomen@hotmail.com> - 0.3.2-1
- Initial package
