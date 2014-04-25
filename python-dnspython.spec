Name:		python-dnspython
Version:	1.11.1
Release:	1
Source0:	http://www.dnspython.org/kits/1.11.1/dnspython-%{version}.tar.gz
Source1:	http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz.asc
License:	MIT
URL:		http://www.dnspython.org/
Summary:	DNS toolkit for Python

Group:		System/Libraries
BuildArch:	noarch
Provides:	dnspython = %{version}-%{release}
BuildRequires:	python-devel
Requires:	python
%description
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic updates.
It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high level
classes perform queries for data of a given name, type, and class, and
return an answer set. The low level classes allow direct manipulation
of DNS zones, messages, names, and records.

%prep
%setup -q -n dnspython-%{version}

%build
%__python setup.py build
%__python -O -c "import compileall; compileall.compile_dir('build')"
%__python -c "import compileall; compileall.compile_dir('build')"

%install
rm -Rf %{buildroot}
%__python setup.py install --prefix %{buildroot}%{_prefix}

%files
%doc LICENSE ChangeLog README PKG-INFO TODO examples
%{py_puresitedir}/dns/*
%{py_puresitedir}/dnspython-%{version}-*



