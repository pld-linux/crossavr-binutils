Summary:	Cross AVR GNU binary utility development utilities - binutils
Summary(es.UTF-8):	Utilitarios para desarrollo de binarios de la GNU - AVR binutils
Summary(fr.UTF-8):	Utilitaires de développement binaire de GNU - AVR binutils
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla AVR - binutils
Summary(pt_BR.UTF-8):	Utilitários para desenvolvimento de binários da GNU - AVR binutils
Summary(tr.UTF-8):	GNU geliştirme araçları - AVR binutils
Name:		crossavr-binutils
Version:	2.23.1
Release:	1
Epoch:		1
Patch0:		am.patch
# Patches 1xx are taken form Atmel official AVR8-GNU toolchain version 3.4.2
# http://distribute.atmel.no/tools/opensource/Atmel-AVR-Toolchain-3.4.2/avr/avr-patches.tar.gz
Patch100:	001-xmega-Makefile_am-typo.patch
Patch101:	002-tinycore-support.patch
Patch102:	003-RMW-insn-constriant.patch
Patch103:	004-new-part-supports.patch
Patch104:	005-additional-part-supports.patch
Patch105:	006-xmega-showuage-typo.patch
Patch106:	007-ata6289-architecture-correction.patch
Patch107:	008-add-usersig-section.patch
Patch108:	009-dwarf-relax-fix.patch
Patch109:	010-disable-demand-paging.patch
Patch110:	200-binutils-avr-size.patch
Patch111:	201-binutils-dwarf2-AVRStudio-workaround.patch
Patch112:	202-binutils-bug13113.patch
Patch113:	400-binutils-atmxt336s.patch
Patch114:	401-binutils-atmega48hvf.patch
Patch115:	402-binutils-atmega26hvg.patch
Patch116:	403-binutils-atmxt224_224e.patch
Patch117:	404-binutils-atmxt112sl.patch
Patch118:	405-binutils-atmxt540s.patch
Patch119:	406-binutils-ata5831.patch
Patch120:	407-binutils-attiny841.patch
Patch121:	408-binutils-atmegarfa2.patch
Patch122:	409-binutils-ata5790n.patch
Patch123:	410-binutils-atmega64hve2.patch
Patch124:	411-binutils-attiny474.patch
Patch125:	412-binutils-atmxts200.patch
Patch126:	500-binutils-avrtc530-backported.patch
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
# Source0-md5:	33adb18c3048d057ac58d07a3f1adb38
URL:		http://sources.redhat.com/binutils/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.9
BuildRequires:	bash
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-tools
BuildRequires:	gcc-c++
BuildRequires:	perl-tools-pod
BuildRequires:	texinfo
%ifarch sparc sparc32
BuildRequires:	sparc32
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		avr
%define		archprefix	%{_prefix}/%{target}
%define		archbindir	%{archprefix}/bin
%define		archlibdir	%{archprefix}/lib

%description
Binutils is a collection of binary utilities, including:
- ar - create, modify and extract from archives,
- nm - lists symbols from object files,
- objcopy - copy and translate object files,
- objdump - display information from object files,
- ranlib - generate an index for the contents of an archive,
- size - list the section sizes of an object or archive file,
- strings - list printable strings from files,
- strip - discard symbols,
- c++filt - a filter for demangling encoded C++ symbols,
- addr2line - convert addresses to file and line.

This package contains the cross version for Atmel AVR.

%description -l pl.UTF-8
Pakiet binutils zawiera zestaw narzędzi umożliwiających kompilację
programów. Znajdują się tutaj między innymi assembler, konsolidator
(linker), a także inne narzędzia do manipulowania binarnymi plikami
programów i bibliotek.

Ten pakiet zawiera wersję skrośną generującą kod dla Atmel AVR.

%prep
%setup -q -n binutils-%{version}
%patch0 -p1
%patch100 -p0
%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch104 -p0
%patch105 -p0
%patch106 -p0
%patch107 -p0
%patch108 -p0
%patch109 -p0
%patch110 -p0
%patch111 -p0
%patch112 -p0
%patch113 -p0
%patch114 -p0
%patch115 -p0
%patch116 -p0
%patch117 -p0
%patch118 -p0
%patch119 -p0
%patch120 -p0
%patch121 -p0
%patch122 -p0
%patch123 -p0
%patch124 -p0
%patch125 -p0
%patch126 -p0

# Remove hacks for specific autoconf version.
echo > config/override.m4

%build
%{__aclocal}
%{__autoconf}
for subdir in bfd binutils ld; do
	cd $subdir
	%{__aclocal} -I.. -I../bfd -I../config
	%{__automake}
	%{__autoconf}
	cd -
done

# ldscripts won't be generated properly if SHELL is not bash...
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
CONFIG_SHELL="/bin/bash" \
./configure \
	MAKEINFO=/bin/true \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--host=%{_target_platform} \
	--build=%{_target_platform} \
	--target=%{target} \
	--enable-gold \
	--disable-shared \
	--disable-werror

# We have to regenerate headers after patching.
%{__make} configure-host \
	tooldir=%{_prefix} \
	EXEEXT=""

%{__make} -C bfd headers \
	tooldir=%{_prefix} \
	EXEEXT=""

%{__make} all \
	tooldir=%{_prefix} \
	EXEEXT=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install \
	MAKEINFO=/bin/true \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	libdir=$RPM_BUILD_ROOT%{_libdir}

# remove these man pages unless we cross-build for win*/netware platforms.
# however, this should be done in Makefiles.
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{*dlltool,*nlmconv,*windmc,*windres}.1

# rely on system locales and info documentation
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}
%{__rm} -r $RPM_BUILD_ROOT%{_infodir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libiberty.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{target}-addr2line
%attr(755,root,root) %{_bindir}/%{target}-ar
%attr(755,root,root) %{_bindir}/%{target}-as
%attr(755,root,root) %{_bindir}/%{target}-c++filt
%attr(755,root,root) %{_bindir}/%{target}-elfedit
%attr(755,root,root) %{_bindir}/%{target}-gprof
%attr(755,root,root) %{_bindir}/%{target}-ld
%attr(755,root,root) %{_bindir}/%{target}-ld.bfd
%attr(755,root,root) %{_bindir}/%{target}-nm
%attr(755,root,root) %{_bindir}/%{target}-objcopy
%attr(755,root,root) %{_bindir}/%{target}-objdump
%attr(755,root,root) %{_bindir}/%{target}-ranlib
%attr(755,root,root) %{_bindir}/%{target}-readelf
%attr(755,root,root) %{_bindir}/%{target}-size
%attr(755,root,root) %{_bindir}/%{target}-strings
%attr(755,root,root) %{_bindir}/%{target}-strip
%dir %{archprefix}
%dir %{archbindir}
%attr(755,root,root) %{archbindir}/ar
%attr(755,root,root) %{archbindir}/as
%attr(755,root,root) %{archbindir}/ld
%attr(755,root,root) %{archbindir}/ld.bfd
%attr(755,root,root) %{archbindir}/nm
%attr(755,root,root) %{archbindir}/objcopy
%attr(755,root,root) %{archbindir}/objdump
%attr(755,root,root) %{archbindir}/ranlib
%attr(755,root,root) %{archbindir}/strip
%dir %{archlibdir}
%{archlibdir}/ldscripts
%{_mandir}/man1/%{target}-addr2line.1*
%{_mandir}/man1/%{target}-ar.1*
%{_mandir}/man1/%{target}-as.1*
%{_mandir}/man1/%{target}-c++filt.1*
%{_mandir}/man1/%{target}-elfedit.1*
%{_mandir}/man1/%{target}-gprof.1*
%{_mandir}/man1/%{target}-ld.1*
%{_mandir}/man1/%{target}-nm.1*
%{_mandir}/man1/%{target}-objcopy.1*
%{_mandir}/man1/%{target}-objdump.1*
%{_mandir}/man1/%{target}-ranlib.1*
%{_mandir}/man1/%{target}-readelf.1*
%{_mandir}/man1/%{target}-size.1*
%{_mandir}/man1/%{target}-strings.1*
%{_mandir}/man1/%{target}-strip.1*
