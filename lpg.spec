Summary:	LDP Linux Programmer's Guide
Summary(pl):	Podr�cznik Linuksowego Programisty LDP
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
Podr�cznik Linuksowego Programisty jest, jak wskazuje nazwa,
podr�cznikiem programowania w Linuksie. Zosta� napisany po to by pom�c
programistom zrozumie� w�a�ciwo�ci Linuksa. Przez swoj� natur� jest
tak�e przydatny przy przenoszeniu program�w z innych system�w
operacyjnych do Linuksa. Dlatego, ten podr�cznik opisuje wywo�ania
systemowe i najwa�niejsze zmiany w kernelu wp�ywaj�ce na starsze
programy do obs�ugi ��cza szeregowego i sieci.

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
