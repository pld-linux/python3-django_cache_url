#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Use Cache URLs in your Django application
Summary(pl.UTF-8):	Wykorzystanie URL-i cache'a w aplikacjach Django
Name:		python-django_cache_url
# keep 3.0.x here for python2 support
Version:	3.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/django-cache-url/
Source0:	https://files.pythonhosted.org/packages/source/d/django-cache-url/django-cache-url-%{version}.tar.gz
# Source0-md5:	f982a26f03c43177317aa0b558d7985f
URL:		https://pypi.org/project/django-cache-url/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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

%package -n python3-django_cache_url
Summary:	Use Cache URLs in your Django application
Summary(pl.UTF-8):	Wykorzystanie URL-i cache'a w aplikacjach Django
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-django_cache_url
This simple Django utility allows you to utilize the 12factor
(<http://www.12factor.net/backing-services>) inspired CACHE_URL
environment variable to configure your Django application.

%description -n python3-django_cache_url -l pl.UTF-8
To proste narzędzie Django pozwala korzystać do konfiguracji aplikacji
Django ze zmiennej środowiskowej CACHE_URL, zainspirowanej przez
12factor (<http://www.12factor.net/backing-services>).

%prep
%setup -q -n django-cache-url-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/django_cache_url.py[co]
%{py_sitescriptdir}/django_cache_url-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-django_cache_url
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/django_cache_url.py
%{py3_sitescriptdir}/__pycache__/django_cache_url.cpython-*.py[co]
%{py3_sitescriptdir}/django_cache_url-%{version}-py*.egg-info
%endif
