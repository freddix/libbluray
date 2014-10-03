Summary:	Library to access Blu-Ray disks for video playback
Name:		libbluray
Version:	0.6.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	ftp://ftp.videolan.org/pub/videolan/libbluray/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	f4d2f2cab53f976cbb22cbae069057bd
URL:		http://www.videolan.org/developers/libbluray.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is aiming to provide a full portable free open source
bluray library, which can be plugged into popular media players to
allow full bluray navigation and playback on Linux. It will eventually
be compatible with all current titles, and will be easily portable and
embeddable in standard players such as mplayer and vlc.

%package devel
Summary:	Header files for libbluray library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2-devel

%description devel
Header files for libbluray library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/bd_info
%attr(755,root,root) %ghost %{_libdir}/libbluray.so.?
%attr(755,root,root) %{_libdir}/libbluray.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbluray.so
%{_includedir}/libbluray
%{_pkgconfigdir}/libbluray.pc

