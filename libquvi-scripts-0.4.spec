Summary:	Embedded lua scripts that libquvi 0.4.x uses for parsing the media details
Summary(pl.UTF-8):	Skrypty osadzonego lua wykorzystywane przez libquvi 0.4.x do analizy multimediów
Name:		libquvi-scripts-0.4
Version:	0.4.21
Release:	2
License:	LGPL v2.1+
Group:		Applications
Source0:	http://downloads.sourceforge.net/quvi/libquvi-scripts-%{version}.tar.xz
# Source0-md5:	2690c995b7cd6193cbc774a7d89a885c
Patch0:		%{name}-scriptsdir.patch
URL:		http://quvi.sourceforge.net/
BuildRequires:	autoconf >= 2.67
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	libquvi-scripts < 0.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains embedded lua scripts that libquvi 0.4.x uses for
parsing the media details.

%description -l pl.UTF-8
Ten pakiet zawiera skrypty osadzonego lua, wykorzystywane przez
libquvi 0.4.x przy analizie szczegółów danych multimedialnych.

%prep
%setup -q -n libquvi-scripts-%{version}
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-nsfw \
	--with-nlfy
#%if "%{_gnu}" != "-gnux32"
#	--build=%{_host} \
#	--host=%{_host} \
#%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_npkgconfigdir}

# packaged in libquvi-scripts 0.9
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man7/libquvi-scripts.7

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/libquvi-scripts
%{_datadir}/libquvi-scripts/0.4
%{_npkgconfigdir}/libquvi-scripts.pc
