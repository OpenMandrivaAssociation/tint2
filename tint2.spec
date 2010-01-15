%define name		tint2
#define revision	svn69
%define ver		0.8
%define rel		%mkrel 1

Name:		%{name}
Summary:	Tint2 - A Lightweight Panel and Taskbar
Version:	%{ver}
Release:	%{rel}
License: 	GPLv2
Group:		Graphical desktop/Other
Url:		http://code.google.com/p/tint2/

BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	cairo-devel
BuildRequires:	libx11-devel
BuildRequires:	pango-devel
BuildRequires:	libxinerama-devel
BuildRequires:	imlib2-devel
BuildRequires:	glib2-devel
BuildRequires:	libxrandr-devel
Source0:	tint2-%{ver}.tar.gz
#Patch0:		set_net_wm_icon_geometry.patch

%description
Tint2 is a simple panel and taskbar intentionally made for
openbox3, but should also work with other window managers. The
goal is to keep a clean and unintrusive look with code
lightweight and compliance with freedesktop specifications.

%prep
%setup -q
#%patch0 -p1

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
