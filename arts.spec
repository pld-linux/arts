#
# Conditional build:
%bcond_without	alsa	# disable ALSA support
%bcond_with	nas	# enable NAS support
%bcond_without	esd	# disable esound support
#
%define		_state		stable
%define		_kdever		3.4.3
%define		_ver		1.4.3
#
Summary:	aRts sound server
Summary(pl):	Serwer d�wi�ku
Summary(pt_BR):	Servidor de sons usado pelo KDE
Name:		arts
Version:	%{_ver}
Release:	0.1
Epoch:		13
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	58585969a9a33784601122c77bd15a1e
Patch100:	%{name}-branch.diff
URL:		http://www.arts-project.org/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils >= 0.6.14
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libmad-devel
BuildRequires:	libtool >= 2:1.5-2
BuildRequires:	libvorbis-devel
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 6:3.2.1-4
#BuildRequires:	unsermake >= 040805-1
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

%description -l pl
Analog Real-Time Synthesizer (w skr�cie aRts) to modularny system do
obs�ugi d�wi�ku i muzyki na komputerze. Za pomoc� modu��w u�ytkownik
mo�e z powodzeniem budowa� kompleksowe narz�dzia przetwarzania
d�wi�ku. Modu�y umo�liwiaj� generacj� kszta�tu fali, filtrowanie,
efekty audio, miksowanie oraz odtwarzanie d�wi�ku cyfrowego w r�nych
formatach. Serwer d�wi�ku artsd umo�liwia r�wnie� jednoczesne
odtwarzanie d�wi�ku z wielu �r�de�.

%description -l pt_BR
O aRts � um sintetizador anal�gico em tempo real que � completamente
modular. Voc� pode criar sons e m�sicas (s�ntese em tempo real de
midi) usando pequenos m�dulos como oscilador para criar waveforms,
v�rios filtros, mixers, faders, etc. Voc� pode configurar tudo atrav�s
de uma interface no KDE. O Servidor aRts � controlado via CORBA. Este
design foi escolhido para permitir que outras aplica��es usem o aRts
como um sintetizador (ou fornecedor de filtros). Usado pelo KDE, entre
outros.

%package devel
Summary:	Sound server - header files
Summary(pl):	Serwer d�wi�ku - pliki nag��wkowe
Summary(pt_BR):	Arquivos para desenvolvimento com o o aRts
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

%description devel -l pl
Pliki nag��wkowe niezb�dne do budowania aplikacji korzystaj�cych z
arts.

%description devel -l pt_BR
Arquivos para desenvolvimento com o o aRts.

# separate from arts-devel because they are mostly independent and have very
# different deps
# there is no artsc base - it would be small and would require arts - so
# there is no reason to separate
%package -n artsc-devel
Summary:	Development files for artsc libraries
Summary(pl):	Pliki programistyczne bibliotek artsc
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 2.0.0
Conflicts:	arts-devel < 12:1.2.0.031126-2

%description -n artsc-devel
Development files for artsc libraries (C interface to aRts sound
system).

%description -n artsc-devel -l pl
Pliki programistyczne bibliotek artsc (interfejsu w C do systemu
d�wi�ku aRts).

%package X11
Summary:	X11 dependent part of aRts
Summary(pl):	Cz�� aRts wymagaj�ca X11
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description X11
X11 dependent part of aRts (x11globalcomm module).

%description X11 -l pl
Cz�� aRts wymagaj�ca X11 (modu� x11globalcomm).

%package qt
Summary:	Qt dependend part of aRts
Summary(pl):	Cz�� aRts wymagaj�ca Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	qt >= 6:3.2.1-4

%description qt
Qt dependend part of aRts (qtmcop library).

%description qt -l pl
Cz�� aRts wymagaj�ca Qt (biblioteka qtmcop).

%package qt-devel
Summary:	Development files for qtmcop library
Summary(pl):	Pliki programistyczne dla biblioteki qtmcop
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-qt = %{epoch}:%{version}-%{release}
Requires:	qt-devel >= 6:3.2.1-4

%description qt-devel
Development files for qtmcop library.

%description qt-devel -l pl
Pliki programistyczne dla biblioteki qtmcop.

%prep
%setup -q
#%patch100 -p1

%build
cp -f /usr/share/automake/config.sub admin

#export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	%{!?with_nas:ac_cv_header_audio_audiolib_h=no} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--enable-final \
	--with-qt-libraries=%{_libdir} \
	--with%{!?with_alsa:out}-alsa

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cd debian/man
for f in *.sgml ; do
	base="$(basename $f .sgml)"
	upper="$(echo ${base} | tr a-z A-Z)"
	db2man $f
	install ${upper}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${base}.1
done

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
%attr(755,root,root) %{_libdir}/libartsflow.so.*.*.*
%attr(755,root,root) %{_libdir}/libartsflow_idl.so.*.*.*
%attr(755,root,root) %{_libdir}/libgmcop.so.*.*.*
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
%{_mandir}/man1/artscat.1*
%{_mandir}/man1/artsd.1*
%{_mandir}/man1/artsdsp.1*
%{_mandir}/man1/artsplay.1*
%{_mandir}/man1/artsrec.1*
%{_mandir}/man1/artsshell.1*
%{_mandir}/man1/artswrapper.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mcopidl
%attr(755,root,root) %{_libdir}/libartsflow.so
%attr(755,root,root) %{_libdir}/libartsflow_idl.so
%attr(755,root,root) %{_libdir}/libartsgslplayobject.so
%attr(755,root,root) %{_libdir}/libartswavplayobject.so
%attr(755,root,root) %{_libdir}/libgmcop.so
%attr(755,root,root) %{_libdir}/libkmedia2.so
%attr(755,root,root) %{_libdir}/libkmedia2_idl.so
%attr(755,root,root) %{_libdir}/libmcop.so
%attr(755,root,root) %{_libdir}/libmcop_mt.so
%attr(755,root,root) %{_libdir}/libsoundserver_idl.so
# it seems to be only (lt_)dlopened, nothing links with it - so not needed
# %attr(755,root,root) %{_libdir}/libx11globalcomm.so
# shared libraries
%{_libdir}/libartsflow.la
%{_libdir}/libartsflow_idl.la
%{_libdir}/libgmcop.la
%{_libdir}/libkmedia2.la
%{_libdir}/libkmedia2_idl.la
%{_libdir}/libmcop.la
%{_libdir}/libmcop_mt.la
%{_libdir}/libsoundserver_idl.la
#
%{_includedir}/arts
%exclude %{_includedir}/arts/qiomanager.h
%{_mandir}/man1/mcopidl.1*

%files -n artsc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsc-config
%attr(755,root,root) %{_libdir}/libartsc.so
%attr(755,root,root) %{_libdir}/libartscbackend.so
%attr(755,root,root) %{_libdir}/libartsdsp.so
%attr(755,root,root) %{_libdir}/libartsdsp_st.so
%{_libdir}/libartsc.la
%{_includedir}/artsc
%{_mandir}/man1/artsc-config.1*

%files X11
%defattr(644,root,root,755)
# lt_dlopened module (.la needed)
%attr(755,root,root) %{_libdir}/libx11globalcomm.so.*.*.*
%{_libdir}/libx11globalcomm.la

%files qt
%defattr(644,root,root,755)
# shared library
%attr(755,root,root) %{_libdir}/libqtmcop.so.*.*.*

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqtmcop.so
%{_libdir}/libqtmcop.la
%{_includedir}/arts/qiomanager.h
