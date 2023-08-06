Name: libfcrypto
Version: 20221229
Release: 1
Summary: Library to support encryption formats
Group: System Environment/Libraries
License: LGPLv3+
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libfcrypto
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
 
BuildRequires: gcc 

%description -n libfcrypto
Library to support encryption formats

%package -n libfcrypto-static
Summary: Library to support encryption formats
Group: Development/Libraries
Requires: libfcrypto = %{version}-%{release}

%description -n libfcrypto-static
Static library version of libfcrypto.

%package -n libfcrypto-devel
Summary: Header files and libraries for developing applications for libfcrypto
Group: Development/Libraries
Requires: libfcrypto = %{version}-%{release}

%description -n libfcrypto-devel
Header files and libraries for developing applications for libfcrypto.

%package -n libfcrypto-python3
Summary: Python 3 bindings for libfcrypto
Group: System Environment/Libraries
Requires: libfcrypto = %{version}-%{release} python3
BuildRequires: python3-devel

%description -n libfcrypto-python3
Python 3 bindings for libfcrypto

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python3
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n libfcrypto
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.so.*

%files -n libfcrypto-static
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.a

%files -n libfcrypto-devel
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.so
%{_libdir}/pkgconfig/libfcrypto.pc
%{_includedir}/*
%{_mandir}/man3/*

%files -n libfcrypto-python3
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.so

%changelog
* Thu Dec 29 2022 Joachim Metz <joachim.metz@gmail.com> 20221229-1
- Auto-generated

