Summary:	LDP Programmer's Guide
Summary(fr):	Le guide du programmeur LDP.
Summary(de):	LDP-Programmerierhandbuch
Summary(pl):	Podr�cznik Programisty LDP
Summary(tr):	LDP Programc� k�lavuzu
Name:		lpg
Version:	0.4
Release:	4
Group:		Documentation
Group(pl):	Dokumentacja
Source:		http://sunsite.unc.edu/LDP/lpg-0.4.html.tar.gz
Copyright:	distributable
BuildArch:	noarch
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is a generic guide to the Programming on Linux systems.
Check http://sunsite.unc.edu/LDP for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l fr
Ceci est un guide g�n�rique � la programmation sur les syst�mes Linux.
Allez sur http://sunsite.unc.edu/LDP pour plus d'informations sur le
Projet de Documentation Linux (LDP) et les mises � jour �ventuelles
de cette version.

%description -l de
Dies ist eine allgemeine Einf�hrung in die Programmierung auf 
Linux-Systemen. Unter der Adresse http://sunsite.unc.edu/LDP finden 
Sie weitere Infos zum Linux-Dokumentationsprojekt und eventuelle 
Updates zu dieser Version. 

%description -l pl
To jest og�lny przewodnik do programowania w systemie Linux. Wi�cej
informacji na temat Projektu Dokumentacji Linuxa (LDP) oraz uaktualnienia
tego dokumentu mo�esz znale�� pod adresem http://sunsite.unc.edu/LDP

%description -l tr
Linux sistemleri i�in programlama k�lavuzu. Linux Belgeleme Projesi (Linux
Documentation Project) ile ilgili daha fazla bilgi ve yeni s�r�mler i�in
http://sunsite.unc.edu/LDP adresine bak�n.

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
%defattr(644,root,root,755)

/usr/doc/LDP/lpg

%changelog
* Mon Feb  8 1999 Micha� Kuratczyk <kurkens@polbox.com>
  [0.4-4]
- sloted BuildRoot into PLD standard
- simplification in %files

* Sat Feb  6 1999 Micha� Kuratczyk <kurkens@polbox.com>
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