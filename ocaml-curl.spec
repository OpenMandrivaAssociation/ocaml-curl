Name:           ocaml-curl
Version:        0.5.0
Release:        %mkrel 1
Summary:        OCaml Curl library (ocurl)
Group:          Development/Other
License:        MIT
URL:            http://sourceforge.net/projects/ocurl
Source0:        http://downloads.sourceforge.net/ocurl/ocurl-%{version}.tgz
Requires:       ocaml
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  findlib
BuildRequires:  curl-devel >= 7.9.8
BuildRequires:  gawk
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
The Ocaml Curl Library (Ocurl) is an interface library for the
programming language Ocaml to the networking library libcurl.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocurl

# Files in the archive have spurious +x mode.
find -type f | xargs chmod 0644
chmod 0755 configure install-sh

%build
%configure --libdir=%{_libdir} --with-findlib
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
%{_libdir}/ocaml/curl
%exclude %{_libdir}/ocaml/curl/*.a
%exclude %{_libdir}/ocaml/curl/*.cmxa
%exclude %{_libdir}/ocaml/curl/*.mli

%files devel
%defattr(-,root,root,-)
%doc examples/*
%{_libdir}/ocaml/curl/*.a
%{_libdir}/ocaml/curl/*.cmxa
%{_libdir}/ocaml/curl/*.mli

