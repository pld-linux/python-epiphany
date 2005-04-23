%define		pname pyphany
Summary:	Python Epiphany bindings
Summary:	Dowi±zania Pythona dla Epiphany
Name:		python-epiphany
Version:	0.1.4
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pyphany/0.1/%{pname}-%{version}.tar.bz2
# Source0-md5:	9f9f4450671feae4a62dd793fa351fa4
BuildRequires:	epiphany-devel >= 1.6.3
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	intltool >= 0.33
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.3
BuildRequires:	python-gnome-devel >= 2.9.4
BuildRequires:	python-pygtk-devel >= 2.5.3
%pyrequires_eq	python-modules
Requires:	epiphany >= 1.6.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Epiphany bindings.

%description -l pl
Dowi±zania Pythona dla Epiphany.

%prep
%setup -q -n %{pname}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/*.la
rm $RPM_BUILD_ROOT%{_libdir}/epiphany-1.6/loaders/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/epiphany-1.6/loaders/lib*.so*
%{_libdir}/epiphany-1.6/extensions/*.py
%{_libdir}/epiphany-1.6/extensions/*.xml
%attr(755,root,root) %{py_sitedir}/gtk-2.0/*.so
%{_datadir}/pygtk/2.0/defs/*.defs
