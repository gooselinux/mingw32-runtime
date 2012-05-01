%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}

Name:           mingw32-runtime
Version:        3.18
Release:        1%{?dist}.1
Summary:        MinGW Windows cross-compiler runtime

License:        Public Domain
Group:          Development/Libraries
URL:            http://www.mingw.org/
Source0:        http://downloads.sourceforge.net/mingw/mingwrt-%{version}-mingw32-src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 49
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc >= 4.4.0
BuildRequires:  mingw32-w32api

# Once this is installed, mingw32-bootstrap (binary bootstrapper) is no
# longer needed.
Obsoletes:      mingw32-runtime-bootstrap


%description
MinGW Windows cross-compiler runtime, base libraries.


%prep
%setup -q -n mingwrt-%{version}-mingw32


%build
MINGW32_CFLAGS="%{_mingw32_cflags} -I%{_mingw32_includedir}"
%{_mingw32_configure}
%{_mingw32_make}


%install
rm -rf $RPM_BUILD_ROOT

%{_mingw32_makeinstall}

# make install places these in nonstandard locations, so move them.
mkdir -p $RPM_BUILD_ROOT%{_mingw32_docdir}
mv $RPM_BUILD_ROOT%{_mingw32_prefix}/doc/* $RPM_BUILD_ROOT%{_mingw32_docdir}/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_mingw32_bindir}/*
%{_mingw32_docdir}/*
%{_mingw32_includedir}/*
%{_mingw32_libdir}/*
%{_mingw32_mandir}/man3/*


%changelog
* Mon Dec 27 2010 Andrew Beekhof <abeekhof@redhat.com> - 3.18-1.1
- Rebuild everything with gcc-4.4
  Related: rhbz#658833

* Fri Dec 24 2010 Andrew Beekhof <abeekhof@redhat.com> - 3.18-1
- Update to 3.18 due to problems described in rhbz#629209
  Related: rhbz#658833 

* Fri Dec 24 2010 Andrew Beekhof <abeekhof@redhat.com> - 3.15.2-5.3
- The use of ExclusiveArch conflicts with noarch, using an alternate COLLECTION to limit builds
  Related: rhbz#658833

* Wed Dec 22 2010 Andrew Beekhof <abeekhof@redhat.com> - 3.15.2-5.2
- Only build mingw packages on x86_64
  Related: rhbz#658833

* Wed Dec 22 2010 Andrew Beekhof <abeekhof@redhat.com> - 3.15.2-5.1
- Bump the revision to avoid tag collision
  Related: rhbz#658833

* Wed Jan 13 2010 Richard W.M. Jones <rjones@redhat.com> - 3.15.2-5
- Fix Source0 URL.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 3.15.2-2
- Rebuild for mingw32-gcc 4.4

* Tue Feb 10 2009 Richard W.M. Jones <rjones@redhat.com> - 3.15.2-1
- New upstream release 3.15.2.

* Tue Dec  9 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-10
- Force rebuild to get rid of the binary bootstrap package and replace
  with package built from source.

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-9
- No runtime dependency on binutils or gcc.
- But it DOES BR w32api.

* Mon Nov 24 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-8
- Rebuild against latest filesystem package.
- MINGW_CFLAGS -> MINGW32_CFLAGS.
- Rewrite the summary for accuracy and brevity.

* Fri Nov 21 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-6
- Remove obsoletes for a long dead package.
- Reenable (and fix) _mingw32_configure (Levente Farkas).

* Thu Nov 20 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-5
- Don't use _mingw32_configure macro - doesn't work here.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-4
- Rebuild against mingw32-filesystem 37

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-3
- Remove the useconds patch, which is no longer needed (Levente Farkas).
- Use _mingw32_configure macro.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-2
- Rebuild against mingw32-filesystem 36

* Thu Oct 16 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-1
- New upstream version 3.15.1.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 3.14-6
- Rename mingw -> mingw32.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 3.14-4
- Use RPM macros from mingw-filesystem.

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 3.14-2
- Initial RPM release, largely based on earlier work from several sources.
