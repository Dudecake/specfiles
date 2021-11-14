# Generated from zfstools-0.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name zfstools

Name: rubygem-%{gem_name}
Version: 0.3.2
Release: 1%{?dist}
Summary: ZFSTools
License: BSD
URL: http://github.com/bdrewery/%{gem_name}
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
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
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# cucumber
# rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/zfs-auto-snapshot
%{_bindir}/zfs-cleanup-snapshots
%{_bindir}/zfs-snapshot-mysql
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
