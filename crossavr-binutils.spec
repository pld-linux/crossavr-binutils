Summary:	Cross AVR GNU binary utility development utilities - binutils
Summary(es.UTF-8):	Utilitarios para desarrollo de binarios de la GNU - AVR binutils
Summary(fr.UTF-8):	Utilitaires de développement binaire de GNU - AVR binutils
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla AVR - binutils
Summary(pt_BR.UTF-8):	Utilitários para desenvolvimento de binários da GNU - AVR binutils
Summary(tr.UTF-8):	GNU geliştirme araçları - AVR binutils
Name:		crossavr-binutils
Version:	2.20.1
Release:	1
Epoch:		1
# Patches 1xx are taken form Atmel official AVR8-GNU toolchain version 3.3.1.481.
Patch100:	300-binutils-2.20.1-avr-size.patch
Patch101:	301-binutils-2.20.1-avr-coff.patch
Patch102:	302-binutils-2.20.1-new-sections.patch
Patch103:	303-binutils-2.20.1-as-dwarf.patch
Patch104:	304-binutils-2.20.1-dwarf2-AVRStudio-workaround.patch
Patch105:	305-binutils-2.20.1-assembler-options.patch
Patch106:	400-binutils-2.20.1-xmega.patch
Patch107:	401-binutils-2.20.1-new-devices.patch
Patch108:	402-binutils-2.20.1-avrtiny10.patch
Patch109:	403-binutils-2.20.1-xmega128a1u-64a1u.patch
Patch110:	404-binutils-2.20.1-atxmega32x1.patch
Patch111:	405-binutils-2.20.1-atxmega128b1.patch
Patch112:	406-binutils-2.20.1-atxmega256a3bu.patch
Patch113:	407-binutils-2.20.1-at90pwm161.patch
Patch114:	408-binutils-2.20.1-atmega16hvb-32hvb.patch
Patch115:	409-binutils-2.20.1-atmega32_5_50_90_pa.patch
Patch116:	410-binutils-2.20.1-attiny1634.patch
Patch117:	411-binutils-2.20.1-atmega48pa.patch
Patch118:	412-binutils-2.20.1-atxmega_16_32_a4u.patch
Patch119:	413-binutils-2.20.1-atxmega64_128_192_256a3u.patch
Patch120:	414-binutils-2.20.1-atmegarfr2_a2.patch
Patch121:	415-binutils-2.20.1-atmega165pa.patch
Patch122:	416-binutils-2.20.1-atxmega384c3.patch
Patch123:	417-binutils-2.20.1-attiny80.patch
Patch124:	418-binutils-2.20.1-atxmega128a4u.patch
Patch125:	419-binutils-2.20.1-atxmega64d4.patch
Patch126:	420-binutils-2.20.1-atmega164pa_168pa_32a_64a.patch
Patch127:	421-binutils-2.20.1-atxmega64_128_b3.patch
Patch128:	422-binutils-2.20.1-atxmega64b1.patch
Patch129:	423-binutils-2.20.1-atmega_8a_128a_1284.patch
Patch130:	424-binutils-2.20.1-atxmega64a4u.patch
Patch131:	425-binutils-2.20.1-atxmega128d4.patch
Patch132:	426-binutils-2.20.1-atmxt336s.patch
Patch133:	427-binutils-2.20.1-atxmega16c4_32c4_128c3_256c3.patch
Patch134:	428-binutils-2.20.1-atxmega384d3.patch
Patch135:	429-binutils-2.20.1-atmega48hvf.patch
Patch136:	430-binutils-2.20.1-atmega26hvg.patch
Patch137:	431-binutils-2.20.1-atmxt224_224e.patch
Patch138:	431-binutils-2.20.1-atxmega192c3.patch
Patch139:	500-binutils-2.20.1-bug13789.patch
Patch140:	501-binutils-2.20.1-bug13113.patch
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
# Source0-md5:	2b9dc8f2b7dbd5ec5992c6e29de0b764
URL:		http://sources.redhat.com/binutils/
BuildRequires:	automake
BuildRequires:	bash
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	perl-tools-pod
BuildRequires:	texinfo
%ifarch sparc sparc32
BuildRequires:	sparc32
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		avr
%define		arch		%{_prefix}/%{target}

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
- addr2line - convert addresses to file and line,
- nlmconv - convert object code into an NLM.

This package contains the cross version for Atmel AVR.

%description -l pl.UTF-8
Pakiet binutils zawiera zestaw narzędzi umożliwiających kompilację
programów. Znajdują się tutaj między innymi assembler, konsolidator
(linker), a także inne narzędzia do manipulowania binarnymi plikami
programów i bibliotek.

Ten pakiet zawiera wersję skrośną generującą kod dla Atmel AVR.

%prep
%setup -q -n binutils-%{version}
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
%patch127 -p0
%patch128 -p0
%patch129 -p0
%patch130 -p0
%patch131 -p0
%patch132 -p0
%patch133 -p0
%patch134 -p0
%patch135 -p0
%patch136 -p0
%patch137 -p0
%patch138 -p0
%patch139 -p0
%patch140 -p0

%build
cp /usr/share/automake/config.sub .

# ldscripts won't be generated properly if SHELL is not bash...
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
CONFIG_SHELL="/bin/bash" \
%ifarch sparc
sparc32 \
%endif
./configure \
	--disable-shared \
	--disable-werror \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--host=%{_target_platform} \
	--build=%{_target_platform} \
	--target=%{target}

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
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	libdir=$RPM_BUILD_ROOT%{_libdir}

# remove these man pages unless we cross-build for win*/netware platforms.
# however, this should be done in Makefiles.
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{*dlltool,*nlmconv,*windres}.1

rm -f $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a
rm -rf $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{target}-*
%dir %{arch}
%dir %{arch}/bin
%attr(755,root,root) %{arch}/bin/*
%dir %{arch}/lib
%dir %{arch}/lib/*
%{arch}/lib/*/*
%{_mandir}/man?/%{target}-*
