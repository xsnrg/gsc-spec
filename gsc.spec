Name:           gsc
Version:        1.0
Release:        1%{?dist}
Summary:        Hubble Guide Star Catalog (GSC)

License:        AURA
URL:            https://archive.stsci.edu/gsc/
Source0:        %{name}_%{version}.orig.tar.gz

BuildRequires:  cmake

# I will solve this later
Conflicts:	gambit-c


%description
The GSC-ACT is a recalibration of the Hubble Guide Star Catalog (GSC), 
version 1.1, using the ACT (Astrographic Catalog/Tycho) from
the US Naval Observatory.

%prep
%setup -q


%build
%cmake .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc readme
%{_datadir}/GSC/*
%{_bindir}/*



%changelog
* Sun Jul  6 2014 Christian Dersch <chrisdersch@gmail.com>
- initial build

