#
#Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Warn
Summary:	Test::Warn - Perl extension to test methods for warnings
Summary(pl):	Test::Warn - rozszerzenie Perla do testowania metod pod k±tem ostrze¿eñ
Name:		perl-Test-Warn
Version:	0.08
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	95fa7fa694f00ec414a877ae4ef65d7b
URL:		http://search.cpan.org/dist/Test-Warn/
%if %{with tests}
BuildRequires:	perl-Array-Compare
BuildRequires:	perl-Sub-Uplevel
BuildRequires:	perl(Test::Builder) => 0.13
BuildRequires:	perl-Test-Builder-Tester
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Tree-DAG_Node
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Tree-DAG_Node
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a few convenience methods for testing warning
based code.

%description -l pl
Ten modu³ udostêpnia kilka wygodnych metod, przydatnych przy
testowaniu kodu, opartego na ostrze¿eniach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/Warn.pm
%{_mandir}/man3/*
