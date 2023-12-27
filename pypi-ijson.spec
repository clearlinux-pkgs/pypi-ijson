#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-ijson
Version  : 3.2.3
Release  : 21
URL      : https://files.pythonhosted.org/packages/20/58/acdd87bd1b926fa2348a7f2ee5e1e7e2c9b808db78342317fc2474c87516/ijson-3.2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/20/58/acdd87bd1b926fa2348a7f2ee5e1e7e2c9b808db78342317fc2474c87516/ijson-3.2.3.tar.gz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://github.com/ICRAR/ijson/actions/workflows/deploy-to-pypi.yml/badge.svg
:target: https://github.com/ICRAR/ijson/actions/workflows/deploy-to-pypi.yml

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
%setup -q -n ijson-3.2.3
cd %{_builddir}/ijson-3.2.3
pushd ..
cp -a ijson-3.2.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690211020
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ijson
cp %{_builddir}/ijson-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-ijson/91f7eb83fb202d517c05fcf21dd0d84371570495 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
