Summary:	GNUbik - an interactive, graphical, single player puzzle
Summary(pl.UTF-8):	GNUbik - interaktywna, graficzna układanka dla jednego gracza
Name:		gnubik
Version:	2.4
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnu.org/gnu/gnubik/%{name}-%{version}.tar.gz
# Source0-md5:	cbafcd93d9ab31695d18358b68cd72c9
URL:		http://www.gnu.org/software/gnubik/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	gtk+2-devel >= 2.20
BuildRequires:	gtkglext-devel
BuildRequires:	guile-devel >= 5:1.8.0
BuildRequires:	pkgconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUbik is an interactive, graphical, single player puzzle. This free
program renders an image of a cube, like that invented by Erno Rubik.
You have to manipulate the cube using the mouse. When each face shows
only one colour, the game is solved.

%description -l pl.UTF-8
GNUbik jest interaktywną, graficzną układanką dla jednego gracza. Ten
wolnodostępny program renderuje obraz kostki, takiej jak wynaleziona
przez Erno Rubika. Trzeba manipulować kostką przy użyciu myszy. Kiedy
każda ściana zawiera tylko jeden kolor, układanka jest rozwiązana.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
%update_icon_cache hicolor

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/gnubik.desktop
%{_datadir}/%{name}
%{_infodir}/*.info*
%{_iconsdir}/hicolor/*/apps/gnubik.png
