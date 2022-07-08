Name:		abf-console-client
Version:	3.0.3.9
Release:	1
Summary:	Console client for ABF (https://abf.openmandriva.org)
Group:		System/Configuration/Packaging
License:	GPLv2
URL:		http://wiki.rosalab.ru/en/index.php/ABF_Console_Client
Source0:	https://github.com/OpenMandrivaSoftware/abf-console-client/archive/v%{version}.tar.gz
Source1:	cooker-aarch64-main.cfg
Source2:	cooker-armv7hnl-main.cfg
Source3:	cooker-x86_64-main.cfg
Patch0:		abfcc-python-3.11.patch
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
Requires:	python-abf >= %{version}-%{release}
Requires:	python3dist(beaker)
Requires:	python3dist(rpm)
Requires:	git
Requires:	python3dist(pyyaml)
Requires:	python3dist(file-magic)
Requires:	bsdtar
Requires:	wget
Requires:	mock
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
%autosetup -n %{name}-%{version} -p1

%build
cd po
%make_build
cd ..

%install
%make_install \
	default_filestore_url="https://file-store.openmandriva.org" \
	PYTHON=%{__python3} \
	default_url=https://abf.openmandriva.org

install -d %{buildroot}%{_sysconfdir}/abf/mock/configs
install -m 0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{buildroot}%{_sysconfdir}/abf/mock/configs/

ln -s %{_datadir}/bash-completion/abf %{buildroot}/%{_sysconfdir}/bash_completion.d/abf
ln -s %{py_puresitedir}/abf/console/download.py %{buildroot}/%{_bindir}/dw
cd po
%make_install
cd ..

%find_lang %{name}

%files -f %{name}.lang
%dir %{py3_puresitedir}/abf/console
%{py3_puresitedir}/abf/console/*.py*
%{_bindir}/abf
%{_bindir}/dw
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
%dir %{py3_puresitedir}/abf
%dir %{py3_puresitedir}/abf/api
%{py3_puresitedir}/abf/*.py*
%{py3_puresitedir}/abf/api/*.py*
