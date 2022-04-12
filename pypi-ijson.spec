#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ijson
Version  : 3.1.4
Release  : 5
URL      : https://files.pythonhosted.org/packages/a8/da/f4b5fda308b60c6c31aa4203f20133a3b5b472e41c0907bc14b7c555cde2/ijson-3.1.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/a8/da/f4b5fda308b60c6c31aa4203f20133a3b5b472e41c0907bc14b7c555cde2/ijson-3.1.4.tar.gz
Summary  : Iterative JSON parser with standard Python iterator interfaces
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-ijson-license = %{version}-%{release}
Requires: pypi-ijson-python = %{version}-%{release}
Requires: pypi-ijson-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://travis-ci.com/ICRAR/ijson.svg?branch=master
:target: https://travis-ci.com/ICRAR/ijson

%package license
Summary: license components for the pypi-ijson package.
Group: Default

%description license
license components for the pypi-ijson package.


%package python
Summary: python components for the pypi-ijson package.
Group: Default
Requires: pypi-ijson-python3 = %{version}-%{release}

%description python
python components for the pypi-ijson package.


%package python3
Summary: python3 components for the pypi-ijson package.
Group: Default
Requires: python3-core
Provides: pypi(ijson)

%description python3
python3 components for the pypi-ijson package.


%prep
%setup -q -n ijson-3.1.4
cd %{_builddir}/ijson-3.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649762216
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ijson
cp %{_builddir}/ijson-3.1.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-ijson/91f7eb83fb202d517c05fcf21dd0d84371570495
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ijson/91f7eb83fb202d517c05fcf21dd0d84371570495

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
