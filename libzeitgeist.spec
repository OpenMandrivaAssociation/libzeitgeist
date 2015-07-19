%define api 1.0
%define major 1
%define libname %mklibname zeitgeist %{api} %{major}
%define devname %mklibname -d zeitgeist

Summary:	Client library for applications that want to interact with the Zeitgeist daemon
Name:		libzeitgeist
Version:	0.3.18
Release:	10
Group:		System/Libraries
License:	LGPLv3 and GPLv3
Url:		https://launchpad.net/libzeitgeist
Source0:	http://launchpad.net/%{name}/0.3/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(glib-2.0)
# zeitgeist is just a runtime and the reason to install libzeitgeist
Requires:	zeitgeist

%description
This project provides a client library for applications that want to interact
with the Zeitgeist daemon. The library is written in C using glib and provides
an asynchronous GObject oriented API.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
This project provides a client library for applications that want to interact
with the Zeitgeist daemon. The library is written in C using glib and provides
an asynchronous GObject oriented API.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	zeitgeist-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

install -d -p -m 755 %{buildroot}%{_datadir}/vala/vapi
install -D -p -m 644 bindings/zeitgeist-1.0.{vapi,deps} %{buildroot}%{_datadir}/vala/vapi

# remove duplicate documentation
rm -fr %{buildroot}%{_defaultdocdir}/%{name}

%files -n %{libname}
%{_libdir}/libzeitgeist-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog COPYING COPYING.GPL MAINTAINERS NEWS README
%doc examples/*.vala examples/*.c
%{_datadir}/gtk-doc/html/zeitgeist-1.0/
%{_includedir}/zeitgeist-1.0/
%{_libdir}/pkgconfig/zeitgeist-1.0.pc
%{_libdir}/*.so
%{_datadir}/vala/vapi/

