Summary:	LDP Programmer's Guide
Summary(fr):	Le guide du programmeur LDP.
Summary(de):	LDP-Programmerierhandbuch
Summary(pl):	Podrêcznik Programisty LDP
Summary(tr):	LDP Programcý kýlavuzu
Name:		lpg
Version:	0.4
Release:	3
Group:		Documentation
Group(pl):	Dokumentacja
Source:		http://sunsite.unc.edu/LDP/lpg-0.4.html.tar.gz
Copyright:	distributable
BuildArch:	noarch
Buildroot:	/tmp/buildroot-%{name}-%{version}

%description
This is a generic guide to the Programming on Linux systems.
Check http://sunsite.unc.edu/LDP for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l fr
Ceci est un guide générique à la programmation sur les systèmes Linux.
Allez sur http://sunsite.unc.edu/LDP pour plus d'informations sur le
Projet de Documentation Linux (LDP) et les mises à jour éventuelles
de cette version.

%description -l de
Dies ist eine allgemeine Einführung in die Programmierung auf 
Linux-Systemen. Unter der Adresse http://sunsite.unc.edu/LDP finden 
Sie weitere Infos zum Linux-Dokumentationsprojekt und eventuelle 
Updates zu dieser Version. 

%description -l pl
To jest ogólny przewodnik do programowania w systemie Linux. Wiêcej
informacji na temat Projektu Dokumentacji Linuxa (LDP) oraz uaktualnienia
tego dokumentu mo¿esz znale¼æ pod adresem http://sunsite.unc.edu/LDP

%description -l tr
Linux sistemleri için programlama kýlavuzu. Linux Belgeleme Projesi (Linux
Documentation Project) ile ilgili daha fazla bilgi ve yeni sürümler için
http://sunsite.unc.edu/LDP adresine bakýn.

%prep
%setup -q -n lpg

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/doc/LDP/lpg

cp -ar * $RPM_BUILD_ROOT/usr/doc/LDP/lpg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)

%dir /usr/doc/LDP/lpg
/usr/doc/LDP/lpg/*

%changelog
* Sat Feb  6 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [0.4-3]
- added pl translations
- replaced "mkdir -p" with "install -d"
- rewrote %files section
- changed BuildRoot
- simplification in %install
- moved %changelog to the end of spec
- cosmetic changes

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- created the package


* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- created the package
