#
# _with_nas		- enable NAS audio support
# _without_alsa		- disable ALSA support
#
%ifarch sparc sparcv9 sparc64
%define		_without_alsa	1
%endif
Summary:	aRts sound server
Summary(pl):	Serwer d�wi�ku
Summary(pt_BR):	Servidor de sons usado pelo KDE
Name:		arts
Version:	1.1.5
Release:	1
Epoch:		12
License:	LGPL
Vendor:		The KDE Team
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/3.1.5/src/%{name}-%{version}.tar.bz2
# Source0-md5:	1d34348e805715559fcd0d978272f031
URL:		http://www.kde.org/
Patch0:		%{name}-nas.patch
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	mad-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5-2
BuildRequires:	libvorbis-devel
%{?_with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

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
Requires:	%{name} = %{epoch}:%{version}

%description X11
X11 dependent part of aRts.

%description X11 -l pl
Cz�� aRts wymagaj�ca X11.

%package qt
Summary:	QT dependend part of aRts
Summary(pl):	Cz�� aRts wymagaj�ca QT
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}
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
Requires:	%{name} = %{epoch}:%{version}
%{?_with_nas:Requires:	nas-devel}

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
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	glib >= 1.2.6

%description glib
GLib dependend part of aRts.

%description glib -l pl
Cz�� aRts wymagaj�ca GLib.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{__perl} admin/am_edit

kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--disable-rpath \
	--enable-final \
	--with-xinerama	\
	--with%{?_without_alsa:out}-alsa \
	--with%{!?_with_nas:out}-nas

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	X11 -p /sbin/ldconfig
%postun	X11 -p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artscat
%attr(755,root,root) %{_bindir}/artsd
%attr(755,root,root) %{_bindir}/artsdsp
%attr(755,root,root) %{_bindir}/artsplay
%attr(755,root,root) %{_bindir}/artsrec
%attr(755,root,root) %{_bindir}/artsshell
%attr(755,root,root) %{_bindir}/artswrapper
%attr(755,root,root) %{_bindir}/testdhandle
# shared libraries
%attr(755,root,root) %{_libdir}/libartsc.so.*.*.*
%attr(755,root,root) %{_libdir}/libartsflow*.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmedia2*.so.*.*.*
%attr(755,root,root) %{_libdir}/libmcop*.so.*.*.*
%attr(755,root,root) %{_libdir}/libsoundserver_idl.so.*.*.*
# lt_dlopened modules (*.la needed)
%attr(755,root,root) %{_libdir}/libarts*playobject.so.*.*.*
%{_libdir}/libarts*playobject.la
%attr(755,root,root) %{_libdir}/libartscbackend.so.*.*.*
%{_libdir}/libartscbackend.la
%attr(755,root,root) %{_libdir}/libartsdsp*.so.*.*.*
%{_libdir}/libartsdsp*.la
%{_libdir}/mcop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsc-config
%attr(755,root,root) %{_bindir}/mcopidl
%attr(755,root,root) %{_libdir}/libartsc.so
%attr(755,root,root) %{_libdir}/libartsflow*.so
%attr(755,root,root) %{_libdir}/libkmedia2*.so
%attr(755,root,root) %{_libdir}/libmcop*.so
%attr(755,root,root) %{_libdir}/libsoundserver_idl.so
%attr(755,root,root) %{_libdir}/libgmcop.so
%attr(755,root,root) %{_libdir}/libqtmcop.so
# some apps (incorrectly?) link with libarts*playobject (gg with -lartswavplayobject only?)
%attr(755,root,root) %{_libdir}/libarts*playobject.so
%{_libdir}/libartsc.la
%{_libdir}/libartsflow*.la
%{_libdir}/libkmedia2*.la
%{_libdir}/libmcop*.la
%{_libdir}/libsoundserver_idl.la
%{_libdir}/libgmcop.la
%{_libdir}/libqtmcop.la
%{_includedir}/arts
%{_includedir}/artsc

%files X11
%defattr(644,root,root,755)
# lt_dlopened module (.la needed)
%attr(755,root,root) %{_libdir}/libx11globalcomm.so.*.*.*
%{_libdir}/libx11globalcomm.la

%files glib
%defattr(644,root,root,755)
# shared library
%attr(755,root,root) %{_libdir}/libgmcop.so.*.*.*

%files qt
%defattr(644,root,root,755)
# shared library
%attr(755,root,root) %{_libdir}/libqtmcop.so.*.*.*
