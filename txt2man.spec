Summary:	Converts flat ASCII text to man page format
Name:     	txt2man
Version:	1.5.6
Release:	2
License:	GPLv2+
Group:		Text tools
Source0: 	http://mvertes.free.fr/download/%{name}-%{version}.tar.gz
URL:		http://mvertes.free.fr/download/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch:	noarch
Requires:	gawk

%description
It is a shell script using gnu awk, that should run on any Unix-like
system. The syntax of the ASCII text is very straightforward and looks
very much like the output of the man(1) program.

%prep
%setup -q

%install
rm -rf %buildroot

mkdir -p %buildroot%_bindir
install -m0755 *man %buildroot%_bindir/

mkdir -p %buildroot%_mandir/man1
install -m0644 *.1 %buildroot%{_mandir}/man1/

%clean
rm -rf %buildroot

%files
%defattr(-, root, root)
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.5.5-2mdv2010.0
+ Revision: 445595
- rebuild

* Mon Dec 01 2008 Funda Wang <fundawang@mandriva.org> 1.5.5-1mdv2009.1
+ Revision: 308737
- import txt2man



