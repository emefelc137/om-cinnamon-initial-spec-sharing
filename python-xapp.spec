%define module xapp

Name:		python-xapp
Version:	3.0.3
Release:	2
Summary:	Python bindings for xapps
License:	GPLv2
Group:		Development/Python
URL:		https://github.com/linuxmint/python-xapp
Source0:	https://github.com/linuxmint/python3-xapp/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	meson
BuildArch:	noarch
BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(psutil)

%description
Python bindings for xapps.

%install -a
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{python_sitelib}/%{module}
