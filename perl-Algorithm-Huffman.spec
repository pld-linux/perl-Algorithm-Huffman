#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Algorithm
%define	pnam	Huffman
Summary:	Algorithm::Huffman - Implementation of the Huffman algorithm
Summary(pl):	Algorithm::Huffman - Implementacja algorytmu Huffmana
Name:		perl-Algorithm-Huffman
Version:	0.09
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Heap
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-String-Random
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-ManyParams
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Tree-DAG_Node
%endif
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
