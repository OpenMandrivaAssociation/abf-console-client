%define py2_puresitedir %(python2 -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_lib())')

Name:		abf-console-client
Version:	2.4.9
Release:	2
Summary:	Console client for ABF (https://abf.io)
Group:		System/Configuration/Packaging
License:	GPLv2
URL:		http://wiki.rosalab.ru/en/index.php/ABF_Console_Client
Source0:	https://abf.io/soft/abf-console-client/archive/%{name}-v%{version}.tar.gz
Source1:	cooker-aarch64-main.cfg
Source2:	cooker-armv7hl-main.cfg
Source3:	cooker-x86_64-main.cfg
BuildArch:	noarch

Requires:	python-abf >= %{version}-%{release}
Requires:	python2-beaker
Requires:	python-rpm
Requires:	git
Requires:	python2-yaml
Requires:	python2-magic
%if %mdvver >= 201500
Requires:	bsdtar
%else
Requires:	tar
%endif
Requires:	wget
Suggests:	mock-urpm
Provides:	abf
Provides:	abfcc
Provides:	abf-c-c

%description
Console client for ABF (https://abf.io).


%package -n python-abf
Summary:	Python API for ABF (https://abf.io)
Group:		System/Configuration/Packaging
Requires:	python < 3.0

%description -n python-abf
%{name} is the python API to ABF (https://abf.io).
It contains a set of basic operations, done with either HTML
parsing or through ABF json API. It also provides datamodel to
operate with.

%prep
%setup -qn %{name}-v%{version}

%build
pushd po
%make
popd

%install
make install DESTDIR=%{buildroot} PYTHON=python2

sed -i -e 's,#!%{_bindir}/python,#!%{_bindir}/python2,' %{buildroot}%{_bindir}/abf
install -m 0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{buildroot}%{_sysconfdir}/abf/mock-urpm/configs/

ln -s %{_datadir}/bash-completion/abf %{buildroot}/%{_sysconfdir}/bash_completion.d/abf
pushd po
%makeinstall_std
popd

%find_lang %{name}

%files -f %{name}.lang
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
