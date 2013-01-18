Summary:	Cross AVR GNU binary utility development utilities - binutils
Summary(es.UTF-8):	Utilitarios para desarrollo de binarios de la GNU - AVR binutils
Summary(fr.UTF-8):	Utilitaires de développement binaire de GNU - AVR binutils
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla AVR - binutils
Summary(pt_BR.UTF-8):	Utilitários para desenvolvimento de binários da GNU - AVR binutils
Summary(tr.UTF-8):	GNU geliştirme araçları - AVR binutils
Name:		crossavr-binutils
Version:	2.22
Release:	2
Epoch:		1
# Patches 1xx are taken form Atmel official AVR8-GNU toolchain version 3.4.1.830
Patch100:	300-binutils-avr-size.patch
Patch101:	301-binutils-avr-coff.patch
Patch102:	302-binutils-as-dwarf.patch
Patch103:	303-binutils-dwarf2-AVRStudio-workaround.patch
Patch104:	304-binutils-bug13113.patch
Patch105:	305-binutils-new-usb-insns.patch
Patch106:	306-binutils-bug15573-AVRTC-419.patch
Patch107:	307-binutils-fix-AVRTC-424.patch
Patch108:	400-binutils-xmega.patch
Patch109:	401-binutils-avrtiny10.patch
Patch110:	402-binutils-at90pwm161.patch
Patch111:	403-binutils-new-devices.patch
Patch112:	404-binutils-attiny1634.patch
Patch113:	405-binutils-atmega48pa.patch
Patch114:	406-binutils-atxmega_16_32_a4u.patch
Patch115:	407-binutils-atxmega64_128_192_256a3u.patch
Patch116:	408-binutils-atmegarfr2_a2.patch
Patch117:	409-binutils-atmega165pa.patch
Patch118:	410-binutils-atxmega384c3.patch
Patch119:	412-binutils-atxmega128a4u.patch
Patch120:	413-binutils-atxmega64d4.patch
Patch121:	414-binutils-atmega164pa_168pa_32a_64a.patch
Patch122:	415-binutils-atxmega64_128_b3.patch
Patch123:	416-binutils-atxmega64b1.patch
Patch124:	417-binutils-atmega_8a_128a_1284.patch
Patch125:	418-binutils-atxmega64a4u.patch
Patch126:	419-binutils-atxmega128d4.patch
Patch127:	420-binutils-atmxt336s.patch
Patch128:	421-binutils-atxmega16c4_32c4_128c3_256c3.patch
Patch129:	422-binutils-atxmega384d3.patch
Patch130:	423-binutils-atmega48hvf.patch
Patch131:	424-binutils-atmega26hvg.patch
Patch132:	425-binutils-atmxt224_224e.patch
Patch133:	426-binutils-atxmega192c3.patch
Patch134:	427-binutils-atmxt112sl.patch
Patch135:	428-binutils-atxmega64c3.patch
Patch136:	429-binutils-ata6285_6286.patch
Patch137:	430-binutils-attiny828.patch
Patch138:	431-binutils-ata5790_5790N_5795.patch
Patch139:	432-binutils-ata5272_5505.patch
Patch140:	433-binutils-atmxt540s.patch
Patch141:	434-binutils-ata5831.patch
Patch142:	435-binutils-attiny841.patch
Patch143:	436-binutils-atxmega32_16_8e5.patch
Patch144:	500-binutils-bug13789.patch
Patch145:	501-binutils-modify-usb-xmega-isa.patch
Patch146:	502-binutils-add-config-section-tiny.patch
Patch147:	503-binutils-avrtc193-tiny.patch
Patch148:	504-binutils-avrtc530-backported.patch
Patch149:	505-binutils-avrtc446.patch
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
# Source0-md5:	ee0f10756c84979622b992a4a61ea3f5
URL:		http://sources.redhat.com/binutils/
BuildRequires:	automake
BuildRequires:	bash
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gcc-c++
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
%patch141 -p0
%patch142 -p0
%patch143 -p0
%patch144 -p0
%patch145 -p0
%patch146 -p0
%patch147 -p0
%patch148 -p0
%patch149 -p0

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
%ifarch sparc
sparc32 \
%endif
./configure \
	--enable-gold \
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
