%if 0%{?centos}
%global with_debug 0
%else
%global with_debug 1
%endif
%global with_check 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%if ! 0%{?gobuild:1} || 0%{?centos}
%define gobuild(o:) GO111MODULE=off go build -trimpath -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '-Wl,-z,relro -Wl,--as-needed  -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld '" -a -v -x %{?**};
%endif

# Global vars
%global provider github
%global provider_tld com
%global project kubernetes-sigs
%global repo %{name}
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}

%global commit0 a12c2d088df8bea138eaeb5a0217d98b6cf93a44
%global git0 https://%{import_path}

%define built_tag 1.25.0
%define download_url %{git0}/archive/v%{built_tag}.tar.gz

Name: cri-tools
Version: 1.25.0
Release: 1%{?dist}
Summary: CLI and validation tools for Container Runtime Interface
License: ASL 2.0
URL: %{git0}
Source0: %{download_url}
ExcludeArch: ppc64
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
%if 0%{?fedora}
BuildRequires: go-rpm-macros
%endif
BuildRequires: golang
BuildRequires: git
BuildRequires: glib2-devel
BuildRequires: glibc-static
%if 0%{?fedora}
BuildRequires: golang-github-cpuguy83-md2man
%else
BuildRequires: go-md2man
%endif
Provides: crictl = %{version}-%{release}

%description
%{summary}

%prep
%autosetup -Sgit -n %{repo}-%{built_tag}

%build
mkdir _build
pushd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../../ src/%{import_path}
popd
ln -s vendor src
export GOPATH=$(pwd)/_build:$(pwd):$(pwd):%{gopath}

export LDFLAGS="-X %{import_path}/pkg/version.Version=%{built_tag}"
export BUILDTAGS="selinux"
GOPATH=$GOPATH %gobuild -o bin/crictl %{import_path}/cmd/crictl
go-md2man -in docs/crictl.md -out docs/crictl.1

%install
# install binaries
install -dp %{buildroot}%{_bindir}
install -p -m 755 ./bin/crictl %{buildroot}%{_bindir}

# install manpage
install -dp %{buildroot}%{_mandir}/man1
install -p -m 644 docs/crictl.1 %{buildroot}%{_mandir}/man1

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md OWNERS README.md RELEASE.md code-of-conduct.md
%doc docs/{benchmark.md,roadmap.md,validation.md}
%{_bindir}/crictl
%{_mandir}/man1/crictl*
