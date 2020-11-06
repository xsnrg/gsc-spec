%define __cmake_in_source_build %{_vpath_builddir}

Name:       gsc
Version:    1.2
Release:    %(date -u +%%Y%%m%%d%%H%%M%%S)%{?dist}
Summary:    Hubble Guide Star Catalog (GSC)

License:    AURA
URL:        https://archive.stsci.edu/gsc/
Source0:    https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/tar.gz?bincats/GSC_1.2#/%{name}-%{version}.tar.gz
Patch0:     Makefile.patch

BuildRequires: cmake
BuildRequires: extra-cmake-modules

# I will solve this later
Conflicts:	gambit-c

%description
The GSC 1.2 catalog from u-strasbg.fr

%prep -v
%setup -c gsc-1.2

%patch0

%build
cd src
%make_build

%install
cd src
%make_install

%files
%doc readme
%{_datadir}/GSC/*
%{_bindir}/*


%changelog
* Thu Nov  5 2020 Jim Howard <jh.xsnrg@gmail.com>
- updated to build directly

* Sun Jul  6 2014 Christian Dersch <chrisdersch@gmail.com>
- initial build

