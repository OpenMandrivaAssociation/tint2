%define name		tint2
%define version		0.9
%define release		%mkrel 1

Summary:	Tint2 - A Lightweight Panel and Taskbar
Name:		%{name}
Version:	%{version}
Release:	%{release}
License: 	GPLv2
Group:		Graphical desktop/Other
Url:		http://code.google.com/p/tint2/
Source0:	http://tint2.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	cairo-devel
BuildRequires:	libx11-devel
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
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc AUTHORS COPYING README ChangeLog 
%config(noreplace) %{_sysconfdir}/xdg/tint2/tint2rc
%{_bindir}/tint2
%{_datadir}/tint2/*.png
%{_mandir}/man1/*
