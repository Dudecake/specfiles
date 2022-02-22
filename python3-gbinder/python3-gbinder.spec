Name:           python3-gbinder
Version:        1.0.0
Release:        1%{?dist}
Summary:        Python bindings for libgbinder

License:        GPLv3
URL:            https://github.com/erfanoabdi/gbinder-python
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Patch0:         %{url}/commit/79d40e9e564772973f7f085ed5c48e3fc625e0f5.patch

BuildRequires:  python3-devel
BuildRequires:  python3-cython
BuildRequires:  python3-setuptools
Requires:       libgbinder

%description
%{summary}

%prep
%autosetup -n gbinder-python-%{version}

%build
%python3 setup.py build --cython

%install
%python3 setup.py install --prefix="%{_prefix}" --root="%{buildroot}"

%files
%license LICENSE
%doc README.md
%{python3_sitearch}/gbinder*
