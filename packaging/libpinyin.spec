Name:           libpinyin
Version:        1.0.0
Release:        0
Summary:        Library to deal with pinyin
License:        GPL-2.0+
Group:          System/Libraries
URL:            https://github.com/libpinyin/libpinyin
Source0:        http://downloads.sourceforge.net/libpinyin/libpinyin/%{name}-%{version}.tar.gz
Source1001:     libpinyin.manifest

BuildRequires:  db4-devel
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig

%description
The libpinyin project aims to provide the algorithms core
for intelligent sentence-based Chinese pinyin input methods.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name} = %{version}-%{release}

%description tools
The %{name}-tools package contains tools.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure --disable-static
%__make %{?_smp_mflags}

%install
%make_install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license COPYING
%doc AUTHORS README
%{_libdir}/*.so.*
%dir %{_libdir}/libpinyin
%{_libdir}/libpinyin/data

%files devel
%manifest %{name}.manifest
%dir %{_includedir}/libpinyin-1.0.0
%{_includedir}/libpinyin-1.0.0/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libpinyin.pc

%files tools
%manifest %{name}.manifest
%{_bindir}/gen_binary_files
%{_bindir}/import_interpolation
%{_bindir}/gen_unigram
%{_mandir}/man1/*.1.*
