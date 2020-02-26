%undefine py2dir
%define py2dir %{_builddir}/dnspython/dnspython2-%{version}
%undefine py3dir
%define py3dir %{_builddir}/dnspython/dnspython-%{version}

Name:          python-dnspython
Version:       1.16.0
Release:       2
Source0:       http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz
Source1:       http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz.asc
License:       MIT
URL:           http://www.dnspython.org/
Summary:       DNS toolkit for Python
Group:         Development/Python
BuildArch:     noarch
Provides:      dnspython = %{EVRD}
Provides:      dnspython3 = %{EVRD}
BuildRequires: pkgconfig(python3)
BuildRequires: python-setuptools
%rename python3-dnspython3
%rename python-dnspython3

%description
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic updates.
It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high level
classes perform queries for data of a given name, type, and class, and
return an answer set. The low level classes allow direct manipulation
of DNS zones, messages, names, and records.

%package -n python2-dnspython
Summary:       DNS toolkit for Python 2
Group:         Development/Python
BuildRequires: pkgconfig(python2)
BuildRequires: python2-setuptools
# For %%check
BuildRequires: python2dist(typing)

%description -n python2-dnspython
dnspython is a DNS toolkit for Python 2. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.


%prep
%setup -q -T -c -n dnspython -a 0
cp -a dnspython-%{version} dnspython2-%{version}

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
PYTHONPATH=%{buildroot}%{py2_puresitedir} %{__python2} utest.py
popd

pushd %{py3dir}/tests
PYTHONPATH=%{buildroot}%{py3_puresitedir} %{__python3} utest.py
popd

%files -n python2-dnspython
%doc dnspython2-%{version}/{LICENSE,examples}
%{py2_puresitedir}/*egg-info
%{py2_puresitedir}/dns

%files
%doc dnspython-%{version}/{LICENSE,examples}
%{py3_puresitedir}/*egg-info
%{py3_puresitedir}/dns
