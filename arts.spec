#

%bcond_without alsa	# disables ALSA support
%bcond_with nas		# enables NAS support 

%ifarch	sparc sparcv9 sparc64
%undefine with_alsa
%endif

%define		_state		snapshots
%define		_ver		1.2.0
%define		_snap		031024

Summary:	aRts sound server
Summary(pl):	Serwer d¼wiêku
Summary(pt_BR):	Servidor de sons usado pelo KDE
Name:		arts
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		12
License:	LGPL
Group:		Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_ver}.tar.bz2
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	a3cbe385442102fcda85f2d68938c7d3
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:  libtool >= 2:1.5-2
BuildRequires:	libvorbis-devel
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 6:3.2.1-4
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
Requires:	qt-devel >= 6:3.2.1-4
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-X11 = %{epoch}:%{version}-%{release}
Requires:	%{name}-glib = %{epoch}:%{version}-%{release}
Requires:	%{name}-qt = %{epoch}:%{version}-%{release}

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
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description X11
X11 dependent part of aRts.

%description X11 -l pl
Czê¶æ aRts wymagaj±ca X11.

%package glib
Summary:	GLib dependend part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca GLib
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib >= 1.2.6

%description glib
GLib dependend part of aRts.

%description glib -l pl
Czê¶æ aRts wymagaj±ca GLib.

%package qt
Summary:	QT dependend part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca QT
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	qt >= 6:3.2.1-4

%description qt
QT dependend part of aRts.

%description qt -l pl
Czê¶æ aRts wymagaj±ca QT.

%prep
%setup -q -n %{name}-%{_snap}

%build

%{__make} -f admin/Makefile.common cvs

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final \
	--with%{?without_alsa:out}-alsa

%if %{without nas}
echo "#undef HAVE_LIBAUDIONAS" >> config.h
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   	-p /sbin/ldconfig
%postun 	-p /sbin/ldconfig

%post	X11	-p /sbin/ldconfig
%postun X11	-p /sbin/ldconfig

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
# shared libraries
%attr(755,root,root) %{_libdir}/libartsc.so.*.*.*
%attr(755,root,root) %{_libdir}/libartsflow.so.*.*.*
%attr(755,root,root) %{_libdir}/libartsflow_idl.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmedia2.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmedia2_idl.so.*.*.*
%attr(755,root,root) %{_libdir}/libmcop.so.*.*.*
%attr(755,root,root) %{_libdir}/libmcop_mt.so.*.*.*
%attr(755,root,root) %{_libdir}/libsoundserver_idl.so.*.*.*
# ltdl modules
%{_libdir}/libartscbackend.la
%attr(755,root,root) %{_libdir}/libartscbackend.so.*.*.*
%{_libdir}/libartsdsp.la
%attr(755,root,root) %{_libdir}/libartsdsp.so.*.*.*
%{_libdir}/libartsdsp_st.la
%attr(755,root,root) %{_libdir}/libartsdsp_st.so.*.*.*
%{_libdir}/libartsgslplayobject.la
%attr(755,root,root) %{_libdir}/libartsgslplayobject.so.*.*.*
%{_libdir}/libartswavplayobject.la
%attr(755,root,root) %{_libdir}/libartswavplayobject.so.*.*.*
#
%{_libdir}/mcop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsc-config
%attr(755,root,root) %{_bindir}/mcopidl
%{_libdir}/libartsc.so
%{_libdir}/libartscbackend.so
%{_libdir}/libartsdsp.so
%{_libdir}/libartsdsp_st.so
%{_libdir}/libartsflow.so
%{_libdir}/libartsflow_idl.so
%{_libdir}/libartsgslplayobject.so
%{_libdir}/libartswavplayobject.so
%{_libdir}/libkmedia2.so
%{_libdir}/libkmedia2_idl.so
%{_libdir}/libgmcop.so
%{_libdir}/libmcop.so
%{_libdir}/libmcop_mt.so
%{_libdir}/libqtmcop.so
%{_libdir}/libsoundserver_idl.so
%{_libdir}/libx11globalcomm.so
#
%{_libdir}/libartsc.la
%{_libdir}/libartsflow.la
%{_libdir}/libartsflow_idl.la
%{_libdir}/libkmedia2.la
%{_libdir}/libkmedia2_idl.la
%{_libdir}/libmcop.la
%{_libdir}/libmcop_mt.la
%{_libdir}/libsoundserver_idl.la
#
%{_libdir}/libgmcop.la
%{_libdir}/libqtmcop.la
#
%{_includedir}/arts
%{_includedir}/artsc

%files X11
%defattr(644,root,root,755)
# ltdl module
%{_libdir}/libx11globalcomm.la
%attr(755,root,root) %{_libdir}/libx11globalcomm.so.*.*.*

%files glib
%defattr(644,root,root,755)
# shared library
%attr(755,root,root) %{_libdir}/libgmcop.so.*.*.*

%files qt
%defattr(644,root,root,755)
# shared library
%attr(755,root,root) %{_libdir}/libqtmcop.so.*.*.*
