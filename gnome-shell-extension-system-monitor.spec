# TODO
# - do something not to pull NM-devel to get *.gir?
%define		extname		system-monitor
Summary:	Display system informations in gnome shell status bar
Name:		gnome-shell-extension-%{extname}
Version:	20121027
Release:	2
License:	GPL v3
Group:		X11/Applications
# $ git clone git://github.com/paradoxxxzero/gnome-shell-system-monitor-applet.git
# $ cd gnome-shell-system-monitor-applet/system-monitor@paradoxxx.zero.gmail.com/
# $ git archive --format=tar --prefix=%{extname}-%{version}/ master | xz > ../../%{extname}-%{version}.tar.xz
Source0:	%{extname}-%{version}.tar.xz
# Source0-md5:	246e68ef905a9bfa4fd924040f6e271d
URL:		https://github.com/paradoxxxzero/gnome-shell-system-monitor-applet/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gnome-shell >= 3.6.0
# This is no mistake, this extensions requires *.gir files from those packages
Requires:	NetworkManager-devel
Requires:	libgtop-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Display system informations in gnome shell status bar, such as memory
usage, cpu usage, network rates.

%prep
%setup -q -n %{extname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{glib-2.0/schemas,locale} \
	$RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/system-monitor@paradoxxx.zero.gmail.com

cp -p schemas/org.gnome.shell.extensions.system-monitor.gschema.xml $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
cp -p *.js* $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/system-monitor@paradoxxx.zero.gmail.com
cp -p *.css $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/system-monitor@paradoxxx.zero.gmail.com

cp -a locale/* $RPM_BUILD_ROOT%{_localedir}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/es{_ES,}

%find_lang %{extname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{extname}.lang
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.system-monitor.gschema.xml
%{_datadir}/gnome-shell/extensions/system-monitor*
