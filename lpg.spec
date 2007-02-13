Summary:	LDP Linux Programmer's Guide
Summary(de.UTF-8):	LDP-Programmerierhandbuch
Summary(fr.UTF-8):	Le guide du programmeur LDP
Summary(pl.UTF-8):	Podręcznik LDP Linuksowego Programisty
Summary(tr.UTF-8):	LDP Programcı kılavuzu
Name:		lpg
Version:	0.4
Release:	5
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/%{name}.html.tar.gz
# Source0-md5:	d0127c91aeb39d4008e9abd8a518254c
URL:		http://www.tldp.org/LDP/lpg/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Linux Programmer's Guide is meant to do what the name implies --
It is to help Linux programmers understand the peculiarities of Linux.
By its nature, this also means that it should be useful when porting
programs from other operating systems to Linux. Therefore, this guide
must describe the system calls and the major kernel changes which have
effects on older programs like serial I/O and networking.

%description -l de.UTF-8
Dies ist eine allgemeine Einführung in die Programmierung auf
Linux-Systemen. Unter der Adresse http://www.tldp.org/ finden Sie
weitere Infos zum Linux-Dokumentationsprojekt und eventuelle Updates
zu dieser Version.

%description -l fr.UTF-8
Ceci est un guide générique à la programmation sur les systèmes Linux.
Allez sur http://www.tldp.org/ pour plus d'informations sur le Projet
de Documentation Linux (LDP) et les mises à jour éventuelles de cette
version.

%description -l pl.UTF-8
Podręcznik Linuksowego Programisty jest, jak wskazuje nazwa,
podręcznikiem programowania w Linuksie. Został napisany po to by pomóc
programistom zrozumieć właściwości Linuksa. Przez swoją naturę jest
także przydatny przy przenoszeniu programów z innych systemów
operacyjnych do Linuksa. Dlatego, ten podręcznik opisuje wywołania
systemowe i najważniejsze zmiany w kernelu wpływające na starsze
programy do obsługi łącza szeregowego i sieci.

%description -l tr.UTF-8
Linux sistemleri için programlama kılavuzu. Linux Belgeleme Projesi
(Linux Documentation Project) ile ilgili daha fazla bilgi ve yeni
sürümler için http://www.tldp.org/ adresine bakın.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
