Summary:	LDP Programmer's Guide
Summary(fr):	Le guide du programmeur LDP
Summary(de):	LDP-Programmerierhandbuch
Summary(pl):	Podrêcznik Programisty LDP
Summary(tr):	LDP Programcý kýlavuzu
Name:		lpg
Version:	0.4
Release:	4
License:	distributable
Group:		Documentation
Source0:	http://www.linuxdoc.org/LDP/%{name}-%{version}.html.tar.gz
URL:		http://www.linuxdoc.org/LDP/lpg/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a generic guide to the Programming on Linux systems. Check
http://www.linuxdoc.org/ for more information about the Linux
Documentation Project, and possible updates to this version.

%description -l fr
Ceci est un guide générique à la programmation sur les systèmes Linux.
Allez sur http://www.linuxdoc.org/ pour plus d'informations sur le
Projet de Documentation Linux (LDP) et les mises à jour éventuelles de
cette version.

%description -l de
Dies ist eine allgemeine Einführung in die Programmierung auf
Linux-Systemen. Unter der Adresse http://www.linuxdoc.org/ finden
Sie weitere Infos zum Linux-Dokumentationsprojekt und eventuelle
Updates zu dieser Version.

%description -l pl
To jest ogólny przewodnik do programowania w systemie Linux. Wiêcej
informacji na temat Projektu Dokumentacji Linuxa (LDP) oraz
uaktualnienia tego dokumentu mo¿esz znale¼æ pod adresem
http://www.linuxdoc.org/ .

%description -l tr
Linux sistemleri için programlama kýlavuzu. Linux Belgeleme Projesi
(Linux Documentation Project) ile ilgili daha fazla bilgi ve yeni
sürümler için http://www.linuxdoc.org/ adresine bakýn.

%prep
%setup -q -n lpg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/lpg

cp -ar * $RPM_BUILD_ROOT%{_docdir}/LDP/lpg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/lpg
