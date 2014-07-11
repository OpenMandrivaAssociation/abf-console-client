%define py2_puresitedir %(python2 -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_lib())')

Name:           abf-console-client
Version:        1.14.9
Release:        2
Summary:        Console client for ABF (https://abf.rosalinux.ru)
Group:          System/Configuration/Packaging
License:        GPLv2
URL:            http://wiki.rosalab.ru/en/index.php/ABF_Console_Client
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       python-abf >= %{version}-%{release}
Requires:       python-beaker
Requires:       python-rpm
Requires:       git
Requires:       python-yaml
Requires:       python-magic
Requires:       bsdtar
Suggests:       mock-urpm
Provides:       abf
Provides:       abfcc
Provides:       abf-c-c

%description
Console client for ABF (https://abf.rosalinux.ru). 


%package -n     python-abf
Summary:        Python API for ABF (https://abf.rosalinux.ru)
Group:          System/Configuration/Packaging
Requires:	python < 3.0

%description -n python-abf
%{name} is the python API to ABF (https://abf.rosalinux.ru).
It contains a set of basic operations, done with either HTML 
parsing or through ABF json API. It also provides datamodel to
operate with.

%prep
%setup -q -n %{name}

%install
make install DESTDIR=%{buildroot} PYTHON=python2
sed -i -e 's,#!%{_bindir}/python,#!%{_bindir}/python2,' %{buildroot}%{_bindir}/abf
ln -s %{_datadir}/bash-completion/abf %{buildroot}/%{_sysconfdir}/bash_completion.d/abf


%files
%dir %{py2_puresitedir}/abf/console
%{py2_puresitedir}/abf/console/*.py*
%{_bindir}/abf
#bash_completion files
%{_datadir}/bash-completion/abf 
%{_sysconfdir}/bash_completion.d/abf
%{_sysconfdir}/profile.d/abfcd.sh
%dir %{_sysconfdir}/abf/mock-urpm/configs/
%{_sysconfdir}/abf/mock-urpm/configs/*
%dir /var/cache/abf/
%dir /var/cache/abf/mock-urpm/
%dir /var/lib/abf/mock-urpm/src
%dir /var/lib/abf/
%dir /var/lib/abf/mock-urpm

%files -n python-abf
%dir %{py2_puresitedir}/abf
%dir %{py2_puresitedir}/abf/api
%{py2_puresitedir}/abf/*.py*
%{py2_puresitedir}/abf/api/*.py*
