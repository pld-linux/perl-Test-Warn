#
# Conditional build:
%bcond_without	tests	# perform "make test"
#
%define		pdir	Test
%define		pnam	Warn
Summary:	Test::Warn - Perl extension to test methods for warnings
Summary(pl.UTF-8):	Test::Warn - rozszerzenie Perla do testowania metod pod kątem ostrzeżeń
Name:		perl-Test-Warn
Version:	0.32
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3210a070680ea24437ebfd2be26bbfcd
URL:		http://search.cpan.org/dist/Test-Warn/
%if %{with tests}
BuildRequires:	perl(Carp) >= 1.22
BuildRequires:	perl-Sub-Uplevel >= 0.12
BuildRequires:	perl(Test::Builder) >= 0.13
BuildRequires:	perl-Test-Builder-Tester >= 1.02
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(Test::Builder) >= 0.13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a few convenience methods for testing warning
based code.

%description -l pl.UTF-8
Ten moduł udostępnia kilka wygodnych metod, przydatnych przy
testowaniu kodu, opartego na ostrzeżeniach.

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
%{_mandir}/man3/Test::Warn.3pm*
