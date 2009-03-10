%define name		tint2
%define revision	svn69
%define ver		0.6.0
%define rel		%mkrel 1

Name:		%{name}
Summary:	Tint2 - A Lightweight Panel and Taskbar
Version:	%{ver}
Release:	%{revision}.%{rel}
License: 	GPL2
Group:		Graphical desktop/Other
Url:		http://code.google.com/p/tint2/

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{revision}-buildroot
BuildRequires:	libcairo-devel
BuildRequires:	libxorg-x11-devel
BuildRequires:	libxinerama1-devel
BuildRequires:	libimlib2-devel
Source0:	tint2-%{ver}-%{revision}.tar.bz2
Patch0:		set_net_wm_icon_geometry.patch
Patch1:		tint2_makefilenostrip.patch

%description
Tint2 is a simple panel and taskbar intentionally made for
openbox3, but should also work with other window managers. The
goal is to keep a clean and unintrusive look with code
lightweight and compliance with freedesktop specifications.

%prep
%setup -q -n %{name}-%{version}-%{revision}
%patch0 -p1
%patch1 -p1

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
%config(noreplace) %{_sysconfdir}/xdg/tint2/tint2rc
%{_bindir}/tint2
%{_mandir}/man1/*
