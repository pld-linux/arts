%define		_kde_ver	3.0
%define		_ver		1.0.0
# Set this to rc3 and such.
# define		_sub_ver
%define		_rel		2

# Set up version, release and FTP directory.
%{?_sub_ver:	%define	_version	%{_ver}%{_sub_ver}}
%{!?_sub_ver:	%define	_version	%{_ver}}
%{?_sub_ver:	%define	_release	0.%{_sub_ver}.%{_rel}}
%{!?_sub_ver:	%define	_release	%{_rel}}
%{!?_sub_ver:	%define	_ftpdir	stable}
%{?_sub_ver:	%define	_ftpdir	unstable/kde-%{version}%{_sub_ver}}

Summary:	aRts sound server
Summary(es):	Sound server used by KDE
Summary(pl):	Serwer dºwiÍku
Summary(pt_BR):	Servidor de sons usado pelo KDE
Name:		arts
Version:	%{_version}
Release:	%{_release}
Epoch:		8
License:	LGPL
Vendor:		The KDE Team
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_ftpdir}/%{_kde_ver}/src/%{name}-%{version}.tar.bz2
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2.2-2
# not needed, only ./configure check for this
#BuildRequires:	libvorbis-devel
#BuildRequires:	mad-devel
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3.0.3
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
Requires:	qt >= 3.0.3
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
aRts sound server.

%description -l es
Sound server and analog analyzer/synthetizer used by KDE.

%description -l pl
Serwer dºwiÍku aRts.

%description -l pt_BR
O aRts È um sintetizador analÛgico em tempo real que È completamente
modular. VocÍ pode criar sons e m˙sicas (sÌntese em tempo real de
midi) usando pequenos mÛdulos como oscilador para criar waveforms,
v·rios filtros, mixers, faders, etc. VocÍ pode configurar tudo atravÈs
de uma interface no KDE. O Servidor aRts È controlado via CORBA. Este
design foi escolhido para permitir que outras aplicaÁıes usem o aRts
como um sintetizador (ou fornecedor de filtros). Usado pelo KDE, entre
outros.

%package X11
Summary:	X11 dependent part of aRts
Summary(pl):	CzÍ∂Ê aRts wymagaj±ca X11
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…

%description X11
X11 dependent part of aRts.

%description X11 -l pl
CzÍ∂Ê aRts wymagaj±ca X11.

%package qt
Summary:	QT dependend part of aRts
Summary(pl):	CzÍ∂Ê aRts wymagaj±ca QT
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…

%description qt
QT dependend part of aRts.

%description qt -l pl
CzÍ∂Ê aRts wymagaj±ca QT.

%package devel
Summary:	Sound server - header files
Summary(es):	Header files for compiling aRtsd applications
Summary(pl):	Serwer dºwiÍku - pliki nag≥Ûwkowe
Summary(pt_BR):	Arquivos para desenvolvimento com o o aRts
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…

%description devel
Header files required to compile programs using arts.

%description devel -l es
This package includes the header files you will need to compile
applications for aRtsd.

%description devel -l pl
Pliki nag≥Ûwkowe niezbÍdne do budowania aplikacji korzystaj±cych z
arts.

%description devel -l pt_BR
Arquivos para desenvolvimento com o o aRts.

%package glib
Summary:	GLib dependend part of aRts
Summary(pl):	CzÍ∂Ê aRts wymagaj±ca GLib
Group:		X11/Libraries

%description glib
GLib dependend part of aRts.

%description glib -l pl
CzÍ∂Ê aRts wymagaj±ca GLib.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

#%{__make} -f Makefile.cvs

CFLAGS="%{rpmcflags} `pkg-config libpng12 --cflags`"; export CFLAGS
CXXFLAGS="%{rpmcflags}"; export CXXFLAGS
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final \
	--with-xinerama	\
	--with-alsa 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artscat
%attr(755,root,root) %{_bindir}/artsd
%attr(755,root,root) %{_bindir}/artsdsp
%attr(755,root,root) %{_bindir}/artsplay
%attr(755,root,root) %{_bindir}/artsrec
%attr(755,root,root) %{_bindir}/artsshell
%attr(755,root,root) %{_bindir}/artswrapper
%attr(755,root,root) %{_libdir}/lib[am]*.so.*.*
%attr(755,root,root) %{_libdir}/libs[!h]*.so.*.*
%attr(755,root,root) %{_libdir}/lib[ams]*.la
%attr(755,root,root) %{_libdir}/libkmedia*.so.*.*
%attr(755,root,root) %{_libdir}/libkmedia*.la
%{_libdir}/mcop

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libx11globalcomm.so.*.*.*
%attr(755,root,root) %{_libdir}/libx11globalcomm.la

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqtmcop.so.*.*.*
%attr(755,root,root) %{_libdir}/libqtmcop.la

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmcop.so.*.*.*
%attr(755,root,root) %{_libdir}/libgmcop.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsc-config
%attr(755,root,root) %{_bindir}/mcopidl
%{_libdir}/lib[mqsxg]*.so
%{_libdir}/libarts[!k]*.so
%{_libdir}/libkmedia*.so
%{_includedir}/arts
%{_includedir}/artsc
