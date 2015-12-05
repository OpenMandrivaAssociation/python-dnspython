%undefine py2dir
%define py2dir %{_builddir}/dnspython/dnspython-%{version}
%undefine py3dir
%define py3dir %{_builddir}/dnspython/dnspython3-%{version}
%define py3unpack -a 2

Name:          python2-dnspython
Version:       1.12.0
Release:       1
Source0:       http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz
Source1:       http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz.asc
Source2:       http://www.dnspython.org/kits3/%{version}/dnspython3-%{version}.tar.gz
Source3:       http://www.dnspython.org/kits3/%{version}/dnspython3-%{version}.tar.gz.asc
License:       MIT
URL:           http://www.dnspython.org/
Summary:       DNS toolkit for Python
Group:         Development/Python
BuildArch:     noarch
Provides:      dnspython = %{version}-%{release}
BuildRequires: pkgconfig(python2)
%rename 	python-dnspython

%description
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic updates.
It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high level
classes perform queries for data of a given name, type, and class, and
return an answer set. The low level classes allow direct manipulation
of DNS zones, messages, names, and records.

%package -n python-dnspython3
Summary:       DNS toolkit for Python 3
Group:         Development/Python
Provides:      dnspython3 = %{version}-%{release}
%rename 	python3-dnspython3
BuildRequires: pkgconfig(python3)


%description -n python-dnspython3
dnspython3 is a DNS toolkit for Python 3. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython3 provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.


%prep
%setup -q -T -c -n dnspython -a 0 %{?py3unpack:%{py3unpack}}

# strip executable permissions so that we don't pick up dependencies
# from documentation
find %{py2dir}/examples -type f | xargs chmod a-x
find %{py3dir}/examples -type f | xargs chmod a-x


%build
pushd %{py2dir}
python2 setup.py build
popd

pushd %{py3dir}
python3 setup.py build
popd

%install
pushd %{py2dir}
python2 setup.py install --skip-build --root %{buildroot}
popd

pushd %{py3dir}
python3 setup.py install --skip-build --root %{buildroot}
popd

%check
pushd %{py2dir}/tests
# skip one test because it queries the network
for py in *.py
do
  if [ $py != resolver.py ]
  then
    PYTHONPATH=%{buildroot}%{py2_puresitedir} %{__python2} $py
  fi
done
popd

pushd %{py3dir}/tests
# skip one test because it queries the network
for py in *.py
do
  if [ $py != resolver.py ]
  then
    PYTHONPATH=%{buildroot}%{py3_puresitedir} %{__python3} $py
  fi
done
popd

%files
%doc dnspython-%{version}/{ChangeLog,LICENSE,README,examples}
%{py2_puresitedir}/*egg-info
%{py2_puresitedir}/dns

%files -n python-dnspython3
%doc dnspython3-%{version}/{ChangeLog,LICENSE,README,examples}
%{py3_puresitedir}/*egg-info
%{py3_puresitedir}/dns



