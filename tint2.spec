%define name	tint2
%define version	snapshot
%define release	r69

Name:		%{name}
Summary:	Tint2 - A Lightweight Panel and Taskbar
Version:	%{version}
Release:	%{release}
License: 	GPL2
Vendor:		Mandriva
Packager:	Caio Begotti <caio@mandriva.com>
Group:		Desktop
Url:		http://code.google.com/p/tint2/

BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libcairo-devel
BuildRequires:	libxorg-x11-devel
BuildRequires:	libxinerama1-devel
BuildRequires:	libimlib2-devel
Source0:	tint2-%{release}.tar.bz2
Patch0:		set_net_wm_icon_geometry.patch

%description
Tint2 is a simple panel and taskbar intentionally made for
openbox3, but should also work with other window managers. The
goal is to keep a clean and unintrusive look with code
lightweight and compliance with freedesktop specifications.

%prep
%setup -q -n %{name}-%{release}
%patch0 -p1

%build
cd src/
%make

%install
cd src/
%makeinstall_std

%clean
cd src/
%make clean

%files
%defattr (-,root,root)
%doc AUTHORS COPYING README ChangeLog tintrc*
%{_sysconfdir}/xdg/tint2/tint2rc
%{_bindir}/*
%{_mandir}/man1/*
