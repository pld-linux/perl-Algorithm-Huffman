#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Algorithm
%define	pnam	Huffman
Summary:	Algorithm::Huffman - implementation of the Huffman algorithm
Summary(pl):	Algorithm::Huffman - implementacja algorytmu Huffmana
Name:		perl-Algorithm-Huffman
Version:	0.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dd5c0360357dcb0807e9ac2e49b2e746
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Heap
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-String-Random
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-ManyParams
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Tree-DAG_Node
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modules implements the huffman algorithm.  The aim is to create
a good coding scheme for a given list of different characters (or even
strings) and their occurence numbers.

%description -l pl
Ten modu³ jest implementacj± algorytmu Huffmana. Celem jest stworzenie
dobrze koduj±cego schematu dla danej listy ró¿nych znaków (lub nawet
ci±gów) i liczby ich wyst±pieñ.

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
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
