Summary:	aRts sound server
Summary(pl):	Serwer d¼wiêku
Summary(pt_BR):	Servidor de sons usado pelo KDE
Name:		arts
%define	_kdever	3.0.3
Version:	1.0.3
Release:	2
Epoch:		11
License:	LGPL
Vendor:		The KDE Team
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/%{name}-%{version}.tar.bz2
%ifnarch sparc sparcv9 sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	audiofile-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
# not needed, only ./configure check for this
#BuildRequires:	libvorbis-devel
#BuildRequires:	mad-devel
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3.0.5
Requires:	qt >= 3.0.5
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
aRts sound server.

%description -l pl
Serwer d¼wiêku aRts.

%description -l pt_BR
O aRts é um sintetizador analógico em tempo real que é completamente
modular. Você pode criar sons e músicas (síntese em tempo real de
midi) usando pequenos módulos como oscilador para criar waveforms,
vários filtros, mixers, faders, etc. Você pode configurar tudo através
de uma interface no KDE. O Servidor aRts é controlado via CORBA. Este
design foi escolhido para permitir que outras aplicações usem o aRts
como um sintetizador (ou fornecedor de filtros). Usado pelo KDE, entre
outros.

%package X11
Summary:	X11 dependent part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca X11
Group:		X11/Libraries

%description X11
X11 dependent part of aRts.

%description X11 -l pl
Czê¶æ aRts wymagaj±ca X11.

%package qt
Summary:	QT dependend part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca QT
Group:		X11/Libraries
Requires:	%{name} >= %{version}

%description qt
QT dependend part of aRts.

%description qt -l pl
Czê¶æ aRts wymagaj±ca QT.

%package devel
Summary:	Sound server - header files
Summary(pl):	Serwer d¼wiêku - pliki nag³ówkowe
Summary(pt_BR):	Arquivos para desenvolvimento com o o aRts
Group:		Development/Libraries
Requires:	qt-devel >= 3.0.3
Requires:	%{name} >= %{version}

%description devel
Header files required to compile programs using arts.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do budowania aplikacji korzystaj±cych z
arts.

%description devel -l pt_BR
Arquivos para desenvolvimento com o o aRts.

%package glib
Summary:	GLib dependend part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca GLib
Group:		X11/Libraries

%description glib
GLib dependend part of aRts.

%description glib -l pl
Czê¶æ aRts wymagaj±ca GLib.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

#%{__make} -f Makefile.cvs

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final \
	--with-xinerama	\
	--with-alsa 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
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
