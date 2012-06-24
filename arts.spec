#
# _with_nas		- enable NAS audio support
# _without_alsa		- disable ALSA support
#

%define		_state		snapshots
%define		_ver		1.2
%define		_snap		030423

Summary:	aRts sound server
Summary(pl):	Serwer d�wi�ku
Summary(pt_BR):	Servidor de sons usado pelo KDE
Name:		arts
Version:	1.2
Release:	0.%{_snap}.1
Epoch:		12
License:	LGPL
Group:		Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_ver}.tar.bz2
Source0:	http://team.pld.org.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
Patch0:		http://rambo.its.tudelft.nl/~ewald/xine/arts-1.1.1-video-20030314.patch
Patch1:		http://rambo.its.tudelft.nl/~ewald/xine/arts-1.1.1-streaming-20030317.patch
%ifnarch sparc sparcv9 sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
BuildRequires:	audiofile-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
# not needed, only ./configure check for this
#BuildRequires:	libvorbis-devel
#BuildRequires:	mad-devel
%{?_with_nas:BuildRequires:	nas-devel}
%{!?_with_nas:BuildConflicts:	nas-devel}
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3.1
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%define		no_install_post_chrpath		1

%description
aRts sound server.

%description -l pl
Serwer d�wi�ku aRts.

%description -l pt_BR
O aRts � um sintetizador anal�gico em tempo real que � completamente
modular. Voc� pode criar sons e m�sicas (s�ntese em tempo real de
midi) usando pequenos m�dulos como oscilador para criar waveforms,
v�rios filtros, mixers, faders, etc. Voc� pode configurar tudo atrav�s
de uma interface no KDE. O Servidor aRts � controlado via CORBA. Este
design foi escolhido para permitir que outras aplica��es usem o aRts
como um sintetizador (ou fornecedor de filtros). Usado pelo KDE, entre
outros.

%package X11
Summary:	X11 dependent part of aRts
Summary(pl):	Cz�� aRts wymagaj�ca X11
Group:		X11/Libraries

%description X11
X11 dependent part of aRts.

%description X11 -l pl
Cz�� aRts wymagaj�ca X11.

%package qt
Summary:	QT dependend part of aRts
Summary(pl):	Cz�� aRts wymagaj�ca QT
Group:		X11/Libraries
Requires:	%{name} >= %{version}
Requires:	qt >= 3.1

%description qt
QT dependend part of aRts.

%description qt -l pl
Cz�� aRts wymagaj�ca QT.

%package devel
Summary:	Sound server - header files
Summary(pl):	Serwer d�wi�ku - pliki nag��wkowe
Summary(pt_BR):	Arquivos para desenvolvimento com o o aRts
Group:		Development/Libraries
Requires:	qt-devel >= 3.1
Requires:	%{name} >= %{version}

%description devel
Header files required to compile programs using arts.

%description devel -l pl
Pliki nag��wkowe niezb�dne do budowania aplikacji korzystaj�cych z
arts.

%description devel -l pt_BR
Arquivos para desenvolvimento com o o aRts.

%package glib
Summary:	GLib dependend part of aRts
Summary(pl):	Cz�� aRts wymagaj�ca GLib
Group:		X11/Libraries
Requires:	glib >= 1.2.6

%description glib
GLib dependend part of aRts.

%description glib -l pl
Cz�� aRts wymagaj�ca GLib.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1
%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final \
	--with-xinerama	\
	--with%{?_without_alsa:out}-alsa

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
##%attr(755,root,root) %{_bindir}/testdhandle
%{_libdir}/lib[!gqx]*.la
%attr(755,root,root) %{_libdir}/lib[!gqx]*.so.*
%{_libdir}/mcop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsc-config
%attr(755,root,root) %{_bindir}/mcopidl
%{_libdir}/*.so
%{_includedir}/arts
%{_includedir}/artsc

%files X11
%defattr(644,root,root,755)
%{_libdir}/libx11globalcomm.la
%attr(755,root,root) %{_libdir}/libx11globalcomm.so.*

%files glib
%defattr(644,root,root,755)
%{_libdir}/libgmcop.la
%attr(755,root,root) %{_libdir}/libgmcop.so.*

%files qt
%defattr(644,root,root,755)
%{_libdir}/libqtmcop.la
%attr(755,root,root) %{_libdir}/libqtmcop.so.*
