Summary:	Converts flat ASCII text to man page format
Name:     	txt2man
Version:	1.6.0
Release:	1
License:	GPLv2+
Group:		Text tools
Source0: 	https://github.com/mvertes/txt2man/archive/%{name}-%{version}.tar.gz
URL:		http://mvertes.free.fr/download/
Buildarch:	noarch
Requires:	gawk

%description
It is a shell script using gnu awk, that should run on any Unix-like
system. The syntax of the ASCII text is very straightforward and looks
very much like the output of the man(1) program.

%prep
%setup -q

%install

mkdir -p %{buildroot}%{_bindir}
install -m0755 *man %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man1
install -m0644 *.1 %{buildroot}%{_mandir}/man1/

%clean

%files
%defattr(-, root, root)
%{_bindir}/*
%{_mandir}/man1/*
