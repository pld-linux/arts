#
# Conditional build:
%bcond_without	alsa	# disable ALSA support
%bcond_with	nas	# enable NAS support
#
Summary:	aRts sound server
Summary(pl):	Serwer d¼wiêku
Summary(pt_BR):	Servidor de sons usado pelo KDE
Name:		arts
Version:	1.1.4
Release:	1
Epoch:		12
License:	LGPL
Vendor:		The KDE Team
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/3.1.4/src/%{name}-%{version}.tar.bz2
# Source0-md5:	aa4bef1e80cd3795e3fd832471e348e9
URL:		http://www.kde.org/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool >= 2:1.5-2
BuildRequires:	libvorbis-devel
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package devel
Summary:	Sound server - header files
Summary(pl):	Serwer d¼wiêku - pliki nag³ówkowe
Summary(pt_BR):	Arquivos para desenvolvimento com o o aRts
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	qt-devel >= 3.1

%description devel
Header files required to compile programs using arts.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do budowania aplikacji korzystaj±cych z
arts.

%description devel -l pt_BR
Arquivos para desenvolvimento com o o aRts.

%package X11
Summary:	X11 dependent part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca X11
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description X11
X11 dependent part of aRts.

%description X11 -l pl
Czê¶æ aRts wymagaj±ca X11.

%package glib
Summary:	GLib dependend part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca GLib
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	glib >= 2.0.0

%description glib
GLib dependend part of aRts.

%description glib -l pl
Czê¶æ aRts wymagaj±ca GLib.

%package qt
Summary:	QT dependend part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca QT
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	qt >= 3.1

%description qt
QT dependend part of aRts.

%description qt -l pl
Czê¶æ aRts wymagaj±ca QT.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{__perl} admin/am_edit

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--disable-rpath \
	--enable-final \
	--with%{!?with_alsa:out}-alsa

%if %{without nas}
# Cannot patch configure.in because it does not rebuild correctly on ac25
sed -e 's@#define HAVE_LIBAUDIONAS 1@/* #undef HAVE_LIBAUDIONAS */@' \
	< config.h \
	> config.h.tmp
mv -f config.h{.tmp,}
%endif

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

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

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
%attr(755,root,root) %{_libdir}/libartsflow.so.*.*.*
%attr(755,root,root) %{_libdir}/libartsflow_idl.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmedia2.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmedia2_idl.so.*.*.*
%attr(755,root,root) %{_libdir}/libmcop.so.*.*.*
%attr(755,root,root) %{_libdir}/libmcop_mt.so.*.*.*
%attr(755,root,root) %{_libdir}/libsoundserver_idl.so.*.*.*
# lt_dlopened modules (*.la needed)
%attr(755,root,root) %{_libdir}/libartscbackend.so.*.*.*
%{_libdir}/libartscbackend.la
%attr(755,root,root) %{_libdir}/libartsdsp.so.*.*.*
%{_libdir}/libartsdsp.la
%attr(755,root,root) %{_libdir}/libartsdsp_st.so.*.*.*
%{_libdir}/libartsdsp_st.la
%attr(755,root,root) %{_libdir}/libartsgslplayobject.so.*.*.*
%{_libdir}/libartsgslplayobject.la
%attr(755,root,root) %{_libdir}/libartswavplayobject.so.*.*.*
%{_libdir}/libartswavplayobject.la
#
%{_libdir}/mcop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsc-config
%attr(755,root,root) %{_bindir}/mcopidl
%attr(755,root,root) %{_libdir}/libartsc.so
%attr(755,root,root) %{_libdir}/libartsflow.so
%attr(755,root,root) %{_libdir}/libartsflow_idl.so
# some apps (incorrectly?) link with libarts*playobject (gg with -lartswavplayobject only?)
%attr(755,root,root) %{_libdir}/libartsgslplayobject.so
%attr(755,root,root) %{_libdir}/libartswavplayobject.so
%attr(755,root,root) %{_libdir}/libkmedia2.so
%attr(755,root,root) %{_libdir}/libkmedia2_idl.so
%attr(755,root,root) %{_libdir}/libmcop.so
%attr(755,root,root) %{_libdir}/libmcop_mt.so
%attr(755,root,root) %{_libdir}/libsoundserver_idl.so
# shared libraries
%{_libdir}/libartsc.la
%{_libdir}/libartsflow.la
%{_libdir}/libartsflow_idl.la
%{_libdir}/libkmedia2.la
%{_libdir}/libkmedia2_idl.la
%{_libdir}/libmcop.la
%{_libdir}/libmcop_mt.la
%{_libdir}/libsoundserver_idl.la
# devel for -glib and -qt
%attr(755,root,root) %{_libdir}/libgmcop.so
%attr(755,root,root) %{_libdir}/libqtmcop.so
%{_libdir}/libgmcop.la
%{_libdir}/libqtmcop.la
#
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
