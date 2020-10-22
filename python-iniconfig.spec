# Created by pyp2rpm-3.3.4
%global pypi_name iniconfig

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        11
Summary:        iniconfig: brain-dead simple config-ini parsing
Group:          Development/Python
License:        MIT
URL:            http://github.com/RonnyPfannschmidt/iniconfig
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(py)
BuildRequires:  python3dist(pytest)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
iniconfig: brain-dead simple parsing of ini files iniconfig is a small and
simple INI-file parser module having a unique set of features:* tested against
Python2.4 across to Python3.2, Jython, PyPy * maintains order of sections and
entries * supports multi-line values with or without line-continuations *
supports "" comments everywhere * raises errors with proper line-numbers * no
bells and...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.txt
%{python_sitelib}/__pycache__/*
%{python_sitelib}/%{pypi_name}.py
%{python_sitelib}/%{pypi_name}-*-py%{python_version}.egg-info
