Summary:	GNUbik - an interactive, graphical, single player puzzle
Summary(pl):	GNUbik - interaktywna, graficzna uk³adanka dla jednego gracza
Name:		gnubik
Version:	2.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.gnu.org/gnu/gnubik/%{name}-%{version}.tar.gz
# Source0-md5:	156b2f58c2bbd32ec48085789699ed1d
URL:		http://www.gnu.org/software/gnubik/
BuildRequires:	gtkglext-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUbik is an interactive, graphical, single player puzzle. This free
program renders an image of a cube, like that invented by Erno Rubik.
You have to manipulate the cube using the mouse. When each face shows
only one colour, the game is solved.

%description -l pl
GNUbik jest interaktywn±, graficzn± uk³adank± dla jednego gracza. Ten
wolnodostêpny program renderuje obraz kostki, takiej jak wynaleziona
przez Erno Rubika. Trzeba manipulowaæ kostk± przy u¿yciu myszy. Kiedy
ka¿da ¶ciana zawiera tylko jeden kolor, uk³adanka jest rozwi±zana.

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

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man6/*
%{_infodir}/*.info*
