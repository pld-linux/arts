#
# _with_nas		- enable NAS audio support
# _without_alsa		- disable ALSA support
#

%define		_state		snapshots
%define		_ver		1.2
%define		_snap		030525

Summary:	aRts sound server
Summary(pl):	Serwer d¼wiêku
Summary(pt_BR):	Servidor de sons usado pelo KDE
Name:		arts
Version:	1.2
Release:	0.%{_snap}.1
Epoch:		12
License:	LGPL
Group:		Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_ver}.tar.bz2
Source0:	http://team.pld.org.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	c7d05f6ce74f0a2105c4a0be1b826f8b
#Patch0:	http://rambo.its.tudelft.nl/~ewald/xine/arts-1.1.1-video-20030314.patch
#Patch1:	http://rambo.its.tudelft.nl/~ewald/xine/arts-1.1.1-streaming-20030317.patch
Patch0:		%{name}-modules.patch
%ifnarch sparc sparcv9 sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
BuildRequires:	audiofile-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
%{?_with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3.2-0.030428.1
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_chrpath		1

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
Requires:	qt-devel >= 3.1
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-X11 = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}

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

%description X11
X11 dependent part of aRts.

%description X11 -l pl
Czê¶æ aRts wymagaj±ca X11.

%package glib
Summary:	GLib dependend part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca GLib
Group:		X11/Libraries
Requires:	glib >= 1.2.6

%description glib
GLib dependend part of aRts.

%description glib -l pl
Czê¶æ aRts wymagaj±ca GLib.

%package qt
Summary:	QT dependend part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca QT
Group:		X11/Libraries
Requires:	%{name} >= %{version}
Requires:	qt >= 3.1

%description qt
QT dependend part of aRts.

%description qt -l pl
Czê¶æ aRts wymagaj±ca QT.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
#%patch1 -p1

%build

%{__make} -f Makefile.cvs

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final \
	--with%{?_without_alsa:out}-alsa

%if %{!?_with_nas:1}0
# Cannot patch configure.in because it does not rebuild correctly on ac25
sed -e 's@#define HAVE_LIBAUDIONAS 1@/* #undef HAVE_LIBAUDIONAS */@' \
	< config.h \
	> config.h.tmp
mv -f config.h{.tmp,}
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   	-p /sbin/ldconfig
%postun 	-p /sbin/ldconfig

#%post	X11	-p /sbin/ldconfig
#%postun X11	-p /sbin/ldconfig

%post	glib	-p /sbin/ldconfig
%postun	glib	-p /sbin/ldconfig

%post	qt	-p /sbin/ldconfig
%postun	qt	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artscat
%attr(755,root,root) %{_bindir}/artsd
%attr(755,root,root) %{_bindir}/artsdsp
%attr(755,root,root) %{_bindir}/artsplay
%attr(755,root,root) %{_bindir}/artsrec
%attr(755,root,root) %{_bindir}/artsshell
%attr(755,root,root) %{_bindir}/artswrapper
%{_libdir}/libartsc.la
%attr(755,root,root) %{_libdir}/libartsc.so.*.*.*
%{_libdir}/libartscbackend.la
#%attr(755,root,root) %{_libdir}/libartscbackend.so.*.*.*
%attr(755,root,root) %{_libdir}/libartscbackend.so
%{_libdir}/libartsdsp.la
#%attr(755,root,root) %{_libdir}/libartsdsp.so.*.*.*
%attr(755,root,root) %{_libdir}/libartsdsp.so
%{_libdir}/libartsdsp_st.la
#%attr(755,root,root) %{_libdir}/libartsdsp_st.so.*.*.*
%attr(755,root,root) %{_libdir}/libartsdsp_st.so
%{_libdir}/libartsflow.la
%attr(755,root,root) %{_libdir}/libartsflow.so.*.*.*
%{_libdir}/libartsflow_idl.la
%attr(755,root,root) %{_libdir}/libartsflow_idl.so.*.*.*
%{_libdir}/libartsgslplayobject.la
#%attr(755,root,root) %{_libdir}/libartsgslplayobject.so.*.*.*
%attr(755,root,root) %{_libdir}/libartsgslplayobject.so
%{_libdir}/libartswavplayobject.la
#%attr(755,root,root) %{_libdir}/libartswavplayobject.so.*.*.*
%attr(755,root,root) %{_libdir}/libartswavplayobject.so
%{_libdir}/libkmedia2.la
%attr(755,root,root) %{_libdir}/libkmedia2.so.*.*.*
%{_libdir}/libkmedia2_idl.la
%attr(755,root,root) %{_libdir}/libkmedia2_idl.so.*.*.*
%{_libdir}/libmcop.la
%attr(755,root,root) %{_libdir}/libmcop.so.*.*.*
%{_libdir}/libmcop_mt.la
%attr(755,root,root) %{_libdir}/libmcop_mt.so.*.*.*
%{_libdir}/libsoundserver_idl.la
%attr(755,root,root) %{_libdir}/libsoundserver_idl.so.*.*.*
%{_libdir}/mcop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsc-config
%attr(755,root,root) %{_bindir}/mcopidl
%{_libdir}/libartsc.so
#%{_libdir}/libartscbackend.so
#%{_libdir}/libartsdsp.so
#%{_libdir}/libartsdsp_st.so
%{_libdir}/libartsflow.so
%{_libdir}/libartsflow_idl.so
#%{_libdir}/libartsgslplayobject.so
#%{_libdir}/libartswavplayobject.so
%{_libdir}/libkmedia2.so
%{_libdir}/libkmedia2_idl.so
%{_libdir}/libgmcop.so
%{_libdir}/libmcop.so
%{_libdir}/libmcop_mt.so
%{_libdir}/libqtmcop.so
%{_libdir}/libsoundserver_idl.so
#%{_libdir}/libx11globalcomm.so
%{_includedir}/arts
%{_includedir}/artsc

%files X11
%defattr(644,root,root,755)
%{_libdir}/libx11globalcomm.la
#%attr(755,root,root) %{_libdir}/libx11globalcomm.so.*.*.*
%attr(755,root,root) %{_libdir}/libx11globalcomm.so

%files glib
%defattr(644,root,root,755)
%{_libdir}/libgmcop.la
%attr(755,root,root) %{_libdir}/libgmcop.so.*.*.*

%files qt
%defattr(644,root,root,755)
%{_libdir}/libqtmcop.la
%attr(755,root,root) %{_libdir}/libqtmcop.so.*.*.*
