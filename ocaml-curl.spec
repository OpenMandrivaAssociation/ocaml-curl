Name:           ocaml-curl
Version:        0.5.3
Release:        6
Summary:        OCaml Curl library (ocurl)
Group:          Development/Other
License:        MIT
URL:            http://sourceforge.net/projects/ocurl
Source0:        http://downloads.sourceforge.net/ocurl/ocurl-%{version}.tgz
Patch0:         Makefile.in-dllib.patch
Requires:       ocaml
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  curl-devel >= 7.9.8
BuildRequires:  ncurses-devel
BuildRequires:  gawk
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
The Ocaml Curl Library (Ocurl) is an interface library for the
programming language Ocaml to the networking library libcurl.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       curl-devel
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocurl
%patch0 -p0

# Files in the archive have spurious +x mode.
find -type f | xargs chmod 0644
chmod 0755 configure install-sh

%build
%configure2_5x --libdir=%{_libdir} --with-findlib
make all

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

# Install curl.mli
cp curl.mli $OCAMLFIND_DESTDIR/curl

# Make clean in the examples dir so our docs don't contain binaries.
make -C examples clean

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%dir %{_libdir}/ocaml/curl
%{_libdir}/ocaml/curl/META
%{_libdir}/ocaml/curl/*.cmi
%{_libdir}/ocaml/curl/*.cma
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root,-)
%doc examples/
%{_libdir}/ocaml/curl/*.a
%{_libdir}/ocaml/curl/*.cmxa
%{_libdir}/ocaml/curl/*.mli



%changelog
* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 0.5.3-4
+ Revision: 797740
- Rebuild

* Thu Oct 07 2010 Funda Wang <fwang@mandriva.org> 0.5.3-3mdv2011.0
+ Revision: 583990
- rebuild

* Mon Aug 23 2010 Florent Monnier <blue_prawn@mandriva.org> 0.5.3-2mdv2011.0
+ Revision: 572420
- fixed the patch
- patched to compile the .so file

* Wed Apr 07 2010 Florent Monnier <blue_prawn@mandriva.org> 0.5.3-1mdv2010.1
+ Revision: 532793
- updated to version 0.5.3

* Wed Mar 17 2010 Florent Monnier <blue_prawn@mandriva.org> 0.5.2-1mdv2010.1
+ Revision: 522776
- update to new version 0.5.2

* Sun Feb 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.1-3mdv2010.1
+ Revision: 512689
- devel package requires curl-devel

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.1-2mdv2010.0
+ Revision: 389932
- rebuild

* Thu Jun 11 2009 Florent Monnier <blue_prawn@mandriva.org> 0.5.1-1mdv2010.0
+ Revision: 385091
- updated version

* Wed Dec 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-1mdv2009.1
+ Revision: 318154
- import ocaml-curl

