#
# Conditional build:
%bcond_without	alsa	# disable ALSA support
%bcond_with	nas	# enable NAS support
%bcond_without	esd	# disable esound support
%bcond_without	hidden_visibility	# pass '--fvisibility=hidden' & '--fvisibility-inlines-hidden' to g++
#
%define		_state		stable
%define		_kdever		3.5.9

Summary:	aRts sound server
Summary(pl.UTF-8):	Serwer dźwięku
Summary(pt_BR.UTF-8):	Servidor de sons usado pelo KDE
Name:		arts
Version:	1.5.9
Release:	2
Epoch:		13
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	62a5e4d522314bab19288e4702480c93
#Patch100:	%{name}-branch.diff
Patch0:		%{name}-libs.patch
Patch1:		kde-ac260-lt.patch
Patch2:		%{name}-extension_loader.patch
URL:		http://www.arts-project.org/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-filesystem-devel
BuildRequires:	boost-regex-devel
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils >= 0.6.14
%{?with_esd:BuildRequires:	esound-devel}
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libmad-devel
BuildRequires:	libtool >= 2:1.5-2
BuildRequires:	libvorbis-devel
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
%{!?with_hidden_visibility:BuildRequires:	qt-devel >= 6:3.2.1-4}
%{?with_hidden_visibility:BuildRequires:	qt-devel >= 6:3.3.5.051113-1}
Obsoletes:	arts-glib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Analog Real-Time Synthesizer, or aRts, is a modular system for
synthesizing sound and music on a digital computer. Using small
building blocks called modules, the user can easily build complex
audio processing tools. Modules typically provide functions such as
sound waveform generators, filters, audio effects, mixing, and
playback of digital audio in different file formats. The artsd sound
server mixes audio from several sources in real time, allowing
multiple sound applications to transparently share access to sound
hardware.

%description -l pl.UTF-8
Analog Real-Time Synthesizer (w skrócie aRts) to modularny system do
obsługi dźwięku i muzyki na komputerze. Za pomocą modułów użytkownik
może z powodzeniem budować kompleksowe narzędzia przetwarzania
dźwięku. Moduły umożliwiają generację kształtu fali, filtrowanie,
efekty audio, miksowanie oraz odtwarzanie dźwięku cyfrowego w różnych
formatach. Serwer dźwięku artsd umożliwia również jednoczesne
odtwarzanie dźwięku z wielu źródeł.

%description -l pt_BR.UTF-8
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
Summary(pl.UTF-8):	Serwer dźwięku - pliki nagłówkowe
Summary(pt_BR.UTF-8):	Arquivos para desenvolvimento com o o aRts
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
# not necessary for all libs (e.g. mcop), but propagated by artsflow
%{?with_alsa:Requires:	alsa-lib-devel}
Requires:	audiofile-devel
Requires:	esound-devel
Requires:	glib2-devel >= 2.0.0
Requires:	jack-audio-connection-kit-devel
Requires:	libmad-devel
Requires:	libvorbis-devel
%{?with_nas:Requires:	nas-devel}

%description devel
Header files required to compile programs using arts.

%description devel -l pl.UTF-8
Pliki nagłówkowe niezbędne do budowania aplikacji korzystających z
arts.

%description devel -l pt_BR.UTF-8
Arquivos para desenvolvimento com o o aRts.

# separate from arts-devel because they are mostly independent and have very
# different deps
# there is no artsc base - it would be small and would require arts - so
# there is no reason to separate
%package -n artsc-devel
Summary:	Development files for artsc libraries
Summary(pl.UTF-8):	Pliki programistyczne bibliotek artsc
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 2.0.0
Conflicts:	arts-devel < 12:1.2.0.031126-2

%description -n artsc-devel
Development files for artsc libraries (C interface to aRts sound
system).

%description -n artsc-devel -l pl.UTF-8
Pliki programistyczne bibliotek artsc (interfejsu w C do systemu
dźwięku aRts).

%package X11
Summary:	X11 dependent part of aRts
Summary(pl.UTF-8):	Część aRts wymagająca X11
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description X11
X11 dependent part of aRts (x11globalcomm module).

%description X11 -l pl.UTF-8
Część aRts wymagająca X11 (moduł x11globalcomm).

%package qt
Summary:	Qt dependend part of aRts
Summary(pl.UTF-8):	Część aRts wymagająca Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	qt >= 6:3.2.1-4

%description qt
Qt dependend part of aRts (qtmcop library).

%description qt -l pl.UTF-8
Część aRts wymagająca Qt (biblioteka qtmcop).

%package qt-devel
Summary:	Development files for qtmcop library
Summary(pl.UTF-8):	Pliki programistyczne dla biblioteki qtmcop
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-qt = %{epoch}:%{version}-%{release}
Requires:	qt-devel >= 6:3.2.1-4

%description qt-devel
Development files for qtmcop library.

%description qt-devel -l pl.UTF-8
Pliki programistyczne dla biblioteki qtmcop.

%prep
%setup -q
#%patch100 -p1
%patch0 -p1
%patch1 -p1
%patch2 -p1

find . -type f -name '*.mcopclass' | xargs %{__sed} -i -e 's:\.la::'

%build
cp -f /usr/share/automake/config.sub admin

%{__make} -f admin/Makefile.common cvs

%configure \
	%{!?with_nas:ac_cv_header_audio_audiolib_h=no} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--disable-final \
	%{?with_hidden_visibility:--enable-gcc-hidden-visibility} \
	--with-qt-libraries=%{_libdir} \
	--with%{!?with_alsa:out}-alsa

%{__make} \
	CXXLD=%{_host_cpu}-%{_vendor}-%{_os}-g++ \
	CCLD=%{_host_cpu}-%{_vendor}-%{_os}-gcc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# it seems to be only (lt_)dlopened, nothing links with it - so not needed
rm -f $RPM_BUILD_ROOT%{_libdir}/libx11globalcomm.{la,so}

# remove unwanted boost deps from .la
sed -i 's:-lboost_filesystem -lboost_regex::' $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	X11 -p /sbin/ldconfig
%postun	X11 -p /sbin/ldconfig

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
# shared libraries
%attr(755,root,root) %{_libdir}/libartsc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsc.so.0
%attr(755,root,root) %{_libdir}/libartsflow.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsflow.so.1
%attr(755,root,root) %{_libdir}/libartsflow_idl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsflow_idl.so.1
%attr(755,root,root) %{_libdir}/libgmcop.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgmcop.so.1
%attr(755,root,root) %{_libdir}/libkmedia2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmedia2.so.1
%attr(755,root,root) %{_libdir}/libkmedia2_idl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmedia2_idl.so.1
%attr(755,root,root) %{_libdir}/libmcop.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmcop.so.1
%attr(755,root,root) %{_libdir}/libmcop_mt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmcop_mt.so.1
%attr(755,root,root) %{_libdir}/libsoundserver_idl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoundserver_idl.so.1
%attr(755,root,root) %{_libdir}/libartscbackend.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartscbackend.so.0
%attr(755,root,root) %{_libdir}/libartsdsp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsdsp.so.0
%attr(755,root,root) %{_libdir}/libartsdsp_st.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsdsp_st.so.0
%attr(755,root,root) %{_libdir}/libartsgslplayobject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsgslplayobject.so.0
%attr(755,root,root) %{_libdir}/libartswavplayobject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartswavplayobject.so.0
#
%{_libdir}/mcop
#%{_mandir}/man1/artscat.1*
#%{_mandir}/man1/artsd.1*
#%{_mandir}/man1/artsdsp.1*
#%{_mandir}/man1/artsplay.1*
#%{_mandir}/man1/artsrec.1*
#%{_mandir}/man1/artsshell.1*
#%{_mandir}/man1/artswrapper.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mcopidl
%{_includedir}/arts
%exclude %{_includedir}/arts/qiomanager.h
%{_libdir}/libartsflow.la
%attr(755,root,root) %{_libdir}/libartsflow.so
%{_libdir}/libartsflow_idl.la
%attr(755,root,root) %{_libdir}/libartsflow_idl.so
%{_libdir}/libartsgslplayobject.la
%attr(755,root,root) %{_libdir}/libartsgslplayobject.so
%{_libdir}/libartswavplayobject.la
%attr(755,root,root) %{_libdir}/libartswavplayobject.so
%{_libdir}/libgmcop.la
%attr(755,root,root) %{_libdir}/libgmcop.so
%{_libdir}/libkmedia2.la
%attr(755,root,root) %{_libdir}/libkmedia2.so
%{_libdir}/libkmedia2_idl.la
%attr(755,root,root) %{_libdir}/libkmedia2_idl.so
%{_libdir}/libmcop.la
%attr(755,root,root) %{_libdir}/libmcop.so
%{_libdir}/libmcop_mt.la
%attr(755,root,root) %{_libdir}/libmcop_mt.so
%{_libdir}/libsoundserver_idl.la
%attr(755,root,root) %{_libdir}/libsoundserver_idl.so
#%{_mandir}/man1/mcopidl.1*

%files -n artsc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsc-config
%{_includedir}/artsc
%{_libdir}/libartsc.la
%attr(755,root,root) %{_libdir}/libartsc.so
%{_libdir}/libartscbackend.la
%attr(755,root,root) %{_libdir}/libartscbackend.so
%{_libdir}/libartsdsp.la
%attr(755,root,root) %{_libdir}/libartsdsp.so
%{_libdir}/libartsdsp_st.la
%attr(755,root,root) %{_libdir}/libartsdsp_st.so
#%{_mandir}/man1/artsc-config.1*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libx11globalcomm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libx11globalcomm.so.1

%files qt
%defattr(644,root,root,755)
# shared library
%attr(755,root,root) %{_libdir}/libqtmcop.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqtmcop.so.1

%files qt-devel
%defattr(644,root,root,755)
%{_includedir}/arts/qiomanager.h
%{_libdir}/libqtmcop.la
%attr(755,root,root) %{_libdir}/libqtmcop.so
