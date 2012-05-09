Name:           ocaml-curl
Version:        0.5.3
Release:        4
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

