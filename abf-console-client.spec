Name:		abf-console-client
Version:	3.0.2.1
Release:	1
Summary:	Console client for ABF (https://abf.openmandriva.org)
Group:		System/Configuration/Packaging
License:	GPLv2
URL:		http://wiki.rosalab.ru/en/index.php/ABF_Console_Client
Source0:	https://github.com/OpenMandrivaSoftware/abf-console-client/archive/v%{version}.tar.gz
Source1:	cooker-aarch64-main.cfg
Source2:	cooker-armv7hnl-main.cfg
Source3:	cooker-x86_64-main.cfg
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
Requires:	python-abf >= %{version}-%{release}
Requires:	python-beaker
Requires:	python-rpm
Requires:	git
Requires:	python-yaml
Requires:	python-magic
%if %mdvver >= 201500
Requires:	bsdtar
%else
Requires:	tar
%endif
Requires:	wget
Suggests:	mock
Provides:	abf = %{EVRD}
Provides:	abfcc = %{EVRD}
Provides:	abf-c-c = %{EVRD}

%description
Console client for ABF (https://abf.openmandriva.org).

%package -n python-abf
Summary:	Python API for ABF (https://abf.openmandriva.org)
Group:		System/Configuration/Packaging
Requires:	python

%description -n python-abf
%{name} is the python API to ABF (https://abf.openmandriva.org).
It contains a set of basic operations, done with either HTML
parsing or through ABF json API. It also provides datamodel to
operate with.

%prep
%setup -qn %{name}-%{version}
%apply_patches

%build
cd po
%make
cd ..

%install
make install DESTDIR=%{buildroot} PYTHON=python
install -d %{buildroot}%{_sysconfdir}/abf/mock/configs
install -m 0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{buildroot}%{_sysconfdir}/abf/mock/configs/

ln -s %{_datadir}/bash-completion/abf %{buildroot}/%{_sysconfdir}/bash_completion.d/abf
cd po
%makeinstall_std
cd ..

%find_lang %{name}

%files -f %{name}.lang
%dir %{py_puresitedir}/abf/console
%{py_puresitedir}/abf/console/*.py*
%{py_puresitedir}/abf/console/__pycache__/
%{_bindir}/abf
#bash_completion files
%{_datadir}/bash-completion/abf 
%{_sysconfdir}/bash_completion.d/abf
%{_sysconfdir}/profile.d/abfcd.sh
%dir %{_sysconfdir}/abf/mock/configs/
%{_sysconfdir}/abf/mock/configs/*
%dir /var/cache/abf/
%dir /var/cache/abf/mock/
%dir /var/lib/abf/mock/src
%dir /var/lib/abf/
%dir /var/lib/abf/mock

%files -n python-abf
%dir %{py_puresitedir}/abf
%dir %{py_puresitedir}/abf/api
%{py_puresitedir}/abf/*.py*
%{py_puresitedir}/abf/__pycache__/
%{py_puresitedir}/abf/api/*.py*
%{py_puresitedir}/abf/api/__pycache__/
