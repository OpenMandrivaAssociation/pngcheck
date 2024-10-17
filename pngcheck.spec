Summary:	PNG tester and debugger
Name:		pngcheck
Version:	2.3.0
Release:	3
License:	BSD
Group:		Graphics
URL:		https://www.libpng.org/pub/png/apps/pngcheck.html
Source0:	http://dl.sf.net/png-mng/pngcheck-%{version}.tar.gz
Patch0:		pngcheck-2.3.0-ldflags_fix.diff
Patch1:		pngcheck-2.3.0-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
pngcheck is the official PNG tester and debugger. Originally designed simply
to test the CRCs within a PNG image file (e.g., to check for ASCII rather
than binary transfer), it has since been extended to check and optionally
print almost all the information about a PNG image and to verify that it
conforms to the PNG specification. It also includes partial support for MNG
animations.

%prep

%setup -q
%patch0 -p0
%patch1 -p0

%build
%make -f Makefile.unx CFLAGS="%{optflags} -DUSE_ZLIB" LDFLAGS="%{ldflags}" LIBS="-lz"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 png-fix-IDAT-windowsize %{buildroot}%{_bindir}/
install -m0755 pngcheck %{buildroot}%{_bindir}/
install -m0755 pngsplit %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc CHANGELOG README
%{_bindir}/png-fix-IDAT-windowsize
%{_bindir}/pngcheck
%{_bindir}/pngsplit



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.3.0-2mdv2010.0
+ Revision: 441881
- rebuild

* Thu Feb 19 2009 Oden Eriksson <oeriksson@mandriva.com> 2.3.0-1mdv2009.1
+ Revision: 342876
- import pngcheck


* Thu Feb 19 2009 Oden Eriksson <oeriksson@mandriva.org> 2.3.0-1mdv2009.1
- initial Mandriva package

* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 2.3.0-1 - 5592/dries
- Updated to release 2.3.0.

* Tue Dec 05 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.0-1
- Updated to release 2.2.0.

* Tue Aug 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.1.0-1
- Updated to release 2.1.0.

* Mon Jul 18 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.0-1
- Initial package.

