Summary:	LDP Linux Programmer's Guide
Summary(de):	LDP-Programmerierhandbuch
Summary(fr):	Le guide du programmeur LDP
Summary(pl):	Podr�cznik LDP Linuksowego Programisty
Summary(tr):	LDP Programc� k�lavuzu
Name:		lpg
Version:	0.4
Release:	5
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/%{name}.html.tar.gz
# Source0-md5:	d0127c91aeb39d4008e9abd8a518254c
URL:		http://www.tldp.org/LDP/lpg/index.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Linux Programmer's Guide is meant to do what the name implies --
It is to help Linux programmers understand the peculiarities of Linux.
By its nature, this also means that it should be useful when porting
programs from other operating systems to Linux. Therefore, this guide
must describe the system calls and the major kernel changes which have
effects on older programs like serial I/O and networking.

%description -l de
Dies ist eine allgemeine Einf�hrung in die Programmierung auf
Linux-Systemen. Unter der Adresse http://www.tldp.org/ finden Sie
weitere Infos zum Linux-Dokumentationsprojekt und eventuelle Updates
zu dieser Version.

%description -l fr
Ceci est un guide g�n�rique � la programmation sur les syst�mes Linux.
Allez sur http://www.tldp.org/ pour plus d'informations sur le Projet
de Documentation Linux (LDP) et les mises � jour �ventuelles de cette
version.

%description -l pl
Podr�cznik Linuksowego Programisty jest, jak wskazuje nazwa,
podr�cznikiem programowania w Linuksie. Zosta� napisany po to by pom�c
programistom zrozumie� w�a�ciwo�ci Linuksa. Przez swoj� natur� jest
tak�e przydatny przy przenoszeniu program�w z innych system�w
operacyjnych do Linuksa. Dlatego, ten podr�cznik opisuje wywo�ania
systemowe i najwa�niejsze zmiany w kernelu wp�ywaj�ce na starsze
programy do obs�ugi ��cza szeregowego i sieci.

%description -l tr
Linux sistemleri i�in programlama k�lavuzu. Linux Belgeleme Projesi
(Linux Documentation Project) ile ilgili daha fazla bilgi ve yeni
s�r�mler i�in http://www.tldp.org/ adresine bak�n.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

cp -ar * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
