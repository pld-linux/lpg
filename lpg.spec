Summary:	LDP Linux Programmer's Guide
Summary(pl):	Podrêcznik Linuksowego Programisty LDP
Name:		lpg
Version:	0.4
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/%{name}.html.tar.gz
URL:		http://www.tldp.org/LDP/%{name}/index.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Linux Programmer's Guide is meant to do what the name implies --
It is to help Linux programmers understand the peculiarities of Linux.
By its nature, this also means that it should be useful when porting
programs from other operating systems to Linux. Therefore, this guide
must describe the system calls and the major kernel changes which have
effects on older programs like serial I/O and networking.

%description -l pl
Podrêcznik Linuksowego Programisty jest, jak wskazuje nazwa,
podrêcznikiem programowania w Linuksie. Zosta³ napisany po to by pomóc
programistom zrozumieæ w³a¶ciwo¶ci Linuksa. Przez swoj± naturê jest
tak¿e przydatny przy przenoszeniu programów z innych systemów
operacyjnych do Linuksa. Dlatego, ten podrêcznik opisuje wywo³ania
systemowe i najwa¿niejsze zmiany w kernelu wp³ywaj±ce na starsze
programy do obs³ugi ³±cza szeregowego i sieci.

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
