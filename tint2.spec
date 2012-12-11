%define name tint2
%define version 0.11
%define release %mkrel 2

Summary: Tint2 - A Lightweight Panel and Taskbar
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2
Group: Graphical desktop/Other
Url: http://code.google.com/p/tint2/
Source0: http://tint2.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires: cmake
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(x11)
BuildRequires: libgtk+2.0-devel
BuildRequires: pango-devel
BuildRequires: pkgconfig(pangoxft)
BuildRequires: pkgconfig(xinerama)
BuildRequires: imlib2-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(xrandr), libxcomposite-devel, libxdamage-devel

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
%makeinstall_std -C build

%files
%doc AUTHORS COPYING README ChangeLog
%config(noreplace) %{_sysconfdir}/xdg/tint2/tint2rc
%{_bindir}/tint*
%{_datadir}/tint2/*.png
%{_datadir}/applications/tint2*.desktop
%{_datadir}/pixmaps/tint2*
%{_mandir}/man1/* 
