Summary: A Lightweight Panel and Taskbar
Name:    tint2
Version: 17.1.3
Release: 3
License: GPLv2
Group: Graphical desktop/Other
Url: http://code.google.com/p/tint2/
#Source0: http://tint2.googlecode.com/files/%{name}-%{version}.tar.bz2
# New source
Source0:  https://www.opencode.net/nick87720z/tint2/-/archive/%{version}/tint2-%{version}.tar.bz2
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangoxft)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(imlib2)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)

%description
Tint2 is a simple panel and taskbar intentionally made for
openbox3, but should also work with other window managers. The
goal is to keep a clean and unintrusive look with code
lightweight and compliance with freedesktop specifications.

%prep
%setup -q

%build
%cmake
%make_build

%install
%make_install -C build

%find_lang tint2conf

%files -f tint2conf.lang
%doc AUTHORS COPYING README* ChangeLog
%doc %{_datadir}/doc/tint2/html/
%doc %{_datadir}/doc/tint2/tint2.md
%config(noreplace) %{_sysconfdir}/xdg/tint2/tint2rc
%{_bindir}/tint*
%{_datadir}/tint2/*.png
%{_datadir}/icons/hicolor/scalable/apps/tint2.svg
%{_datadir}/icons/hicolor/scalable/apps/tint2conf.svg
%{_datadir}/applications/tint2*.desktop
%{_datadir}/tint2/horizontal*
%{_datadir}/tint2/vertical*
%{_datadir}/mime/packages/tint2conf.xml
%{_mandir}/man1/* 
