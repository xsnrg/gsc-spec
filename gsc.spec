%define __cmake_in_source_build %{_vpath_builddir}

Name:           gsc
Version:        1.2
Release:	%(date -u +%%Y%%m%%d%%H%%M%%S)%{?dist}
Summary:        Hubble Guide Star Catalog (GSC)

License:        AURA
URL:            https://archive.stsci.edu/gsc/
Source0:	cdsarc.u-strasbg.fr/viz-bin/nph-Cat/tar.gz?bincats/GSC_1.2 

BuildRequires: cmake
BuildRequires: systemd
BuildRequires: extra-cmake-modules


# I will solve this later
Conflicts:	gambit-c


%description
The GSC 1.2 catalog from u-strasbg.fr

%prep
%setup -q


%build
%cmake .
%make_build


%install
%cmake_install


%files
%doc readme
%{_datadir}/GSC/*
%{_bindir}/*



%changelog
* Thu Nov  5 2020 Jim Howard <jh.xsnrg@gmail.com>
- updated to build directly

* Sun Jul  6 2014 Christian Dersch <chrisdersch@gmail.com>
- initial build

