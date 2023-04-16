Name:           python3-gbinder
Version:        1.1.1
Release:        3%{?dist}
Summary:        Python bindings for libgbinder

License:        GPLv3
URL:            https://github.com/erfanoabdi/gbinder-python
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-cython
BuildRequires:  python3-setuptools
BuildRequires:  libgbinder-devel

%description
%{summary}

%prep
%autosetup -n gbinder-python-%{version}

%build
python3 setup.py build --cython

%install
python3 setup.py install --prefix="%{_prefix}" --root="%{buildroot}"

%files
%license LICENSE
%doc README.md
%{python3_sitearch}/gbinder*
