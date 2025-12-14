%global pypi_name iniconfig

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        1
Summary:        iniconfig: brain-dead simple config-ini parsing
Group:          Development/Python
License:        MIT
URL:            https://github.com/RonnyPfannschmidt/iniconfig
Source0:        https://files.pythonhosted.org/packages/source/i/iniconfig/iniconfig-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools-scm)
BuildRequires:  python%{pyver}dist(py)
BuildRequires:	git-core

%description
iniconfig: brain-dead simple parsing of ini files iniconfig is a small and
simple INI-file parser module having a unique set of features:* tested against
Python2.4 across to Python3.2, Jython, PyPy * maintains order of sections and
entries * supports multi-line values with or without line-continuations *
supports "" comments everywhere * raises errors with proper line-numbers * no
bells and...

%prep -a
# Make setuptools-scm happy
git init
git add .
git commit -am "Import %{version}"
git tag -a %{version} -m %{version}

%files
%license LICENSE
%{python_sitelib}/iniconfig/*
%{python_sitelib}/iniconfig-%{version}.dist-info
