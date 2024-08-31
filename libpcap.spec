#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xE089DEF1D9C15D0D (release@tcpdump.org)
#
Name     : libpcap
Version  : 1.10.5
Release  : 36
URL      : https://www.tcpdump.org/release/libpcap-1.10.5.tar.gz
Source0  : https://www.tcpdump.org/release/libpcap-1.10.5.tar.gz
Source1  : https://www.tcpdump.org/release/libpcap-1.10.5.tar.gz.sig
Source2  : E089DEF1D9C15D0D.pkey
Summary  : Platform-independent network traffic capture library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libpcap-bin = %{version}-%{release}
Requires: libpcap-lib = %{version}-%{release}
Requires: libpcap-license = %{version}-%{release}
Requires: libpcap-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : dbus-dev
BuildRequires : flex
BuildRequires : gnupg
BuildRequires : libnl-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# LIBPCAP 1.x.y by [The Tcpdump Group](https://www.tcpdump.org)
**To report a security issue please send an e-mail to security@tcpdump.org.**

%package bin
Summary: bin components for the libpcap package.
Group: Binaries
Requires: libpcap-license = %{version}-%{release}

%description bin
bin components for the libpcap package.


%package dev
Summary: dev components for the libpcap package.
Group: Development
Requires: libpcap-lib = %{version}-%{release}
Requires: libpcap-bin = %{version}-%{release}
Provides: libpcap-devel = %{version}-%{release}
Requires: libpcap = %{version}-%{release}

%description dev
dev components for the libpcap package.


%package lib
Summary: lib components for the libpcap package.
Group: Libraries
Requires: libpcap-license = %{version}-%{release}

%description lib
lib components for the libpcap package.


%package license
Summary: license components for the libpcap package.
Group: Default

%description license
license components for the libpcap package.


%package man
Summary: man components for the libpcap package.
Group: Default

%description man
man components for the libpcap package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) E089DEF1D9C15D0D' gpg.status
%setup -q -n libpcap-1.10.5
cd %{_builddir}/libpcap-1.10.5
pushd ..
cp -a libpcap-1.10.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725068880
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --enable-ipv6
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --enable-ipv6
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1725068880
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libpcap
cp %{_builddir}/libpcap-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libpcap/bf0cb439d0ca55615b5060ee09d77af3ddc9518d || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pcap-config

%files dev
%defattr(-,root,root,-)
/usr/include/pcap-bpf.h
/usr/include/pcap-namedb.h
/usr/include/pcap.h
/usr/include/pcap/bluetooth.h
/usr/include/pcap/bpf.h
/usr/include/pcap/can_socketcan.h
/usr/include/pcap/compiler-tests.h
/usr/include/pcap/dlt.h
/usr/include/pcap/funcattrs.h
/usr/include/pcap/ipnet.h
/usr/include/pcap/namedb.h
/usr/include/pcap/nflog.h
/usr/include/pcap/pcap-inttypes.h
/usr/include/pcap/pcap.h
/usr/include/pcap/sll.h
/usr/include/pcap/socket.h
/usr/include/pcap/usb.h
/usr/include/pcap/vlan.h
/usr/lib64/libpcap.so
/usr/lib64/pkgconfig/libpcap.pc
/usr/share/man/man3/pcap.3pcap
/usr/share/man/man3/pcap_activate.3pcap
/usr/share/man/man3/pcap_breakloop.3pcap
/usr/share/man/man3/pcap_can_set_rfmon.3pcap
/usr/share/man/man3/pcap_close.3pcap
/usr/share/man/man3/pcap_compile.3pcap
/usr/share/man/man3/pcap_create.3pcap
/usr/share/man/man3/pcap_datalink.3pcap
/usr/share/man/man3/pcap_datalink_name_to_val.3pcap
/usr/share/man/man3/pcap_datalink_val_to_description.3pcap
/usr/share/man/man3/pcap_datalink_val_to_description_or_dlt.3pcap
/usr/share/man/man3/pcap_datalink_val_to_name.3pcap
/usr/share/man/man3/pcap_dispatch.3pcap
/usr/share/man/man3/pcap_dump.3pcap
/usr/share/man/man3/pcap_dump_close.3pcap
/usr/share/man/man3/pcap_dump_file.3pcap
/usr/share/man/man3/pcap_dump_flush.3pcap
/usr/share/man/man3/pcap_dump_fopen.3pcap
/usr/share/man/man3/pcap_dump_ftell.3pcap
/usr/share/man/man3/pcap_dump_open.3pcap
/usr/share/man/man3/pcap_file.3pcap
/usr/share/man/man3/pcap_fileno.3pcap
/usr/share/man/man3/pcap_findalldevs.3pcap
/usr/share/man/man3/pcap_fopen_offline.3pcap
/usr/share/man/man3/pcap_fopen_offline_with_tstamp_precision.3pcap
/usr/share/man/man3/pcap_free_datalinks.3pcap
/usr/share/man/man3/pcap_free_tstamp_types.3pcap
/usr/share/man/man3/pcap_freealldevs.3pcap
/usr/share/man/man3/pcap_freecode.3pcap
/usr/share/man/man3/pcap_get_required_select_timeout.3pcap
/usr/share/man/man3/pcap_get_selectable_fd.3pcap
/usr/share/man/man3/pcap_get_tstamp_precision.3pcap
/usr/share/man/man3/pcap_geterr.3pcap
/usr/share/man/man3/pcap_getnonblock.3pcap
/usr/share/man/man3/pcap_init.3pcap
/usr/share/man/man3/pcap_inject.3pcap
/usr/share/man/man3/pcap_is_swapped.3pcap
/usr/share/man/man3/pcap_lib_version.3pcap
/usr/share/man/man3/pcap_list_datalinks.3pcap
/usr/share/man/man3/pcap_list_tstamp_types.3pcap
/usr/share/man/man3/pcap_lookupdev.3pcap
/usr/share/man/man3/pcap_lookupnet.3pcap
/usr/share/man/man3/pcap_loop.3pcap
/usr/share/man/man3/pcap_major_version.3pcap
/usr/share/man/man3/pcap_minor_version.3pcap
/usr/share/man/man3/pcap_next.3pcap
/usr/share/man/man3/pcap_next_ex.3pcap
/usr/share/man/man3/pcap_offline_filter.3pcap
/usr/share/man/man3/pcap_open_dead.3pcap
/usr/share/man/man3/pcap_open_dead_with_tstamp_precision.3pcap
/usr/share/man/man3/pcap_open_live.3pcap
/usr/share/man/man3/pcap_open_offline.3pcap
/usr/share/man/man3/pcap_open_offline_with_tstamp_precision.3pcap
/usr/share/man/man3/pcap_perror.3pcap
/usr/share/man/man3/pcap_sendpacket.3pcap
/usr/share/man/man3/pcap_set_buffer_size.3pcap
/usr/share/man/man3/pcap_set_datalink.3pcap
/usr/share/man/man3/pcap_set_immediate_mode.3pcap
/usr/share/man/man3/pcap_set_promisc.3pcap
/usr/share/man/man3/pcap_set_protocol_linux.3pcap
/usr/share/man/man3/pcap_set_rfmon.3pcap
/usr/share/man/man3/pcap_set_snaplen.3pcap
/usr/share/man/man3/pcap_set_timeout.3pcap
/usr/share/man/man3/pcap_set_tstamp_precision.3pcap
/usr/share/man/man3/pcap_set_tstamp_type.3pcap
/usr/share/man/man3/pcap_setdirection.3pcap
/usr/share/man/man3/pcap_setfilter.3pcap
/usr/share/man/man3/pcap_setnonblock.3pcap
/usr/share/man/man3/pcap_snapshot.3pcap
/usr/share/man/man3/pcap_stats.3pcap
/usr/share/man/man3/pcap_statustostr.3pcap
/usr/share/man/man3/pcap_strerror.3pcap
/usr/share/man/man3/pcap_tstamp_type_name_to_val.3pcap
/usr/share/man/man3/pcap_tstamp_type_val_to_description.3pcap
/usr/share/man/man3/pcap_tstamp_type_val_to_name.3pcap

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libpcap.so.1.10.5
/usr/lib64/libpcap.so.1
/usr/lib64/libpcap.so.1.10.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libpcap/bf0cb439d0ca55615b5060ee09d77af3ddc9518d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pcap-config.1
/usr/share/man/man5/pcap-savefile.5
/usr/share/man/man7/pcap-filter.7
/usr/share/man/man7/pcap-linktype.7
/usr/share/man/man7/pcap-tstamp.7
