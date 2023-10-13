#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-llfuse
Version  : 1.5.0
Release  : 45
URL      : https://files.pythonhosted.org/packages/d2/2c/64f01042d1ed08725342c85ddb48a29d2a4f8712d27f22f66f28a67a079c/llfuse-1.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d2/2c/64f01042d1ed08725342c85ddb48a29d2a4f8712d27f22f66f28a67a079c/llfuse-1.5.0.tar.gz
Summary  : Python bindings for the low-level FUSE API
Group    : Development/Tools
License  : LGPL-2.0
Requires: pypi-llfuse-license = %{version}-%{release}
Requires: pypi-llfuse-python = %{version}-%{release}
Requires: pypi-llfuse-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pkgconfig(fuse)
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
..
NOTE: We cannot use sophisticated ReST syntax (like
e.g. :file:`foo`) here because this isn't rendered correctly
by PyPi.

%package license
Summary: license components for the pypi-llfuse package.
Group: Default

%description license
license components for the pypi-llfuse package.


%package python
Summary: python components for the pypi-llfuse package.
Group: Default
Requires: pypi-llfuse-python3 = %{version}-%{release}

%description python
python components for the pypi-llfuse package.


%package python3
Summary: python3 components for the pypi-llfuse package.
Group: Default
Requires: python3-core
Provides: pypi(llfuse)

%description python3
python3 components for the pypi-llfuse package.


%prep
%setup -q -n llfuse-1.5.0
cd %{_builddir}/llfuse-1.5.0
pushd ..
cp -a llfuse-1.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1691449655
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-llfuse
cp %{_builddir}/llfuse-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-llfuse/a942fd86faab764d64db3aacfdc7af285c7d15ba || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-llfuse/a942fd86faab764d64db3aacfdc7af285c7d15ba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
