
#Conditional build:
%bcond_with	tests	# perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Warn
Summary:	Perl extension to test methods for warnings
Name:		perl-Test-Warn
Version:	0.08
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	95fa7fa694f00ec414a877ae4ef65d7b
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Array-Compare
BuildRequires:	perl(Test::Builder) => 0.13
BuildRequires:	perl-Test-Builder-Tester
BuildRequires:	perl-Sub-Uplevel
BuildRequires:	perl-Tree-DAG_Node
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a few convenience methods for testing warning
based code.

%description -l pl
Ten modu³ udostêpnia kilka wygodnych metod, przydatnych przy testowaniu
kodu, opartego na ostrze¿eniach.

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
%doc Change*
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
