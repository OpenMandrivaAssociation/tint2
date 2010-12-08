%define name		tint2
%define version		0.11
%define release		%mkrel 2

Summary:	Tint2 - A Lightweight Panel and Taskbar
Name:		%{name}
Version:	%{version}
Release:	%{release}
License: 	GPLv2
Group:		Graphical desktop/Other
Url:		http://code.google.com/p/tint2/
Source0:	http://tint2.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	libgtk+-x11-2.0
BuildRequires:	cmake
BuildRequires:	cairo-devel
BuildRequires:	libx11-devel
BuildRequires:  libgtk+-x11-2.0
BuildRequires:	pango-devel
BuildRequires:	libxinerama-devel
BuildRequires:	imlib2-devel
BuildRequires:	glib2-devel
BuildRequires:	libxrandr-devel, libxcomposite-devel, libxdamage-devel

%description
Tint2 is a simple panel and taskbar intentionally made for
openbox3, but should also work with other window managers. The
goal is to keep a clean and unintrusive look with code
lightweight and compliance with freedesktop specifications.

%prep
%setup -q

%build
%cmake
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc AUTHORS COPYING README ChangeLog 
%config(noreplace) %{_sysconfdir}/xdg/tint2/tint2rc
%{_bindir}/tint*
%{_datadir}/tint2/*.png
%{_datadir}/applications/tint2*.desktop
%{_datadir}/pixmaps/tint2*
%{_mandir}/man1/*
