Name:		python-dnspython
Version:	1.9.4
Release:	%mkrel 1
Source0:	http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz
Source1:	http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz.asc
License:	MIT
URL:		http://www.dnspython.org/
Summary:	DNS toolkit for Python
Group:		System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%{__rm} -Rf %{buildroot}
%__python setup.py install --prefix %{buildroot}%{_prefix}

%files
%doc LICENSE ChangeLog README PKG-INFO TODO examples
%{py_puresitedir}/dns/*
%{py_puresitedir}/dnspython-%{version}-*


%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.4-1mdv2011.0
+ Revision: 662530
- update to new version 1.9.4

* Thu Nov 25 2010 Funda Wang <fwang@mandriva.org> 1.9.2-1mdv2011.0
+ Revision: 600934
- update to new version 1.9.2

* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 1.8.0-2mdv2011.0
+ Revision: 598984
- rebuild for py2.7

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.0-1mdv2011.0
+ Revision: 569667
- update to new version 1.8.0

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.1-1mdv2010.0
+ Revision: 397063
- update to new version 1.7.1

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.0-1mdv2010.0
+ Revision: 384248
- update to new version 1.6.0

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.5.0-6mdv2009.1
+ Revision: 323622
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-5mdv2009.0
+ Revision: 259578
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-4mdv2009.0
+ Revision: 247405
- rebuild
- fix no-buildroot-tag

* Mon Nov 05 2007 Nicolas Vigier <nvigier@mandriva.com> 1.5.0-2mdv2008.1
+ Revision: 106164
- add provides on dnspython
- import python-dnspython


