#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	HTTP
%define		pnam	Daemon
Summary:	HTTP::Daemon - a simple HTTP server class
Summary(pl.UTF-8):	HTTP::Daemon - klasa prostego serwera HTTP
Name:		perl-HTTP-Daemon
Version:	6.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/HTTP/OALDERS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	14f98fd61159ec4740a21781b787944e
URL:		https://metacpan.org/dist/HTTP-Daemon
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-Module-Build-Tiny >= 0.034
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(IO::Socket::IP) >= 0.32
BuildRequires:	perl-HTTP-Date >= 6
BuildRequires:	perl-HTTP-Message >= 6
BuildRequires:	perl-LWP-MediaTypes >= 6
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-Test-Needs
BuildRequires:	perl-Test-Simple >= 0.98
BuildRequires:	perl-URI
%endif
Requires:	perl-HTTP-Date >= 6
Requires:	perl-HTTP-Message >= 6
Requires:	perl-LWP-MediaTypes >= 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Instances of the HTTP::Daemon class are HTTP/1.1 servers that
listen on a socket for incoming requests. The HTTP::Daemon is a
subclass of IO::Socket::INET, so you can perform socket operations
directly on it too.

%description -l pl.UTF-8
Instancje klasy HTTP::Daemon są serwerami HTTP/1.1 nasłuchującymi
na gnieździe. HTTP::Daemon to podklasa IO::Socket::INET, więc można
na niej wykonywać bezpośrednio także operacje typowe dla gniazd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--destdir=$RPM_BUILD_ROOT \
	--installdirs=vendor

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTTP/Daemon.pm
%{_mandir}/man3/HTTP::Daemon.3pm*
