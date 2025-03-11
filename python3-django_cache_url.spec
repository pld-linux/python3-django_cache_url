Summary:	Use Cache URLs in your Django application
Summary(pl.UTF-8):	Wykorzystanie URL-i cache'a w aplikacjach Django
Name:		python3-django_cache_url
Version:	3.4.4
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/django-cache-url/
Source0:	https://files.pythonhosted.org/packages/source/d/django-cache-url/django-cache-url-%{version}.tar.gz
# Source0-md5:	764e80a7a88e2ce83e8e9e19e8d69a0c
URL:		https://pypi.org/project/django-cache-url/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This simple Django utility allows you to utilize the 12factor
(<http://www.12factor.net/backing-services>) inspired CACHE_URL
environment variable to configure your Django application.

%description -l pl.UTF-8
To proste narzędzie Django pozwala korzystać do konfiguracji aplikacji
Django ze zmiennej środowiskowej CACHE_URL, zainspirowanej przez
12factor (<http://www.12factor.net/backing-services>).

%prep
%setup -q -n django-cache-url-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/django_cache_url
%{py3_sitescriptdir}/django_cache_url-%{version}-py*.egg-info
