%define py2_puresitedir %(python2 -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_lib())')

Name:		abf-console-client
Version:	2.7
Release:	3
Summary:	Console client for ABF (https://abf.openmandriva.org)
Group:		System/Configuration/Packaging
License:	GPLv2
URL:		http://wiki.rosalab.ru/en/index.php/ABF_Console_Client
Source0:	https://abf.io/soft/abf-console-client/archive/%{name}-v%{version}.tar.gz
Source1:	cooker-aarch64-main.cfg
Source2:	cooker-armv7hl-main.cfg
Source3:	cooker-x86_64-main.cfg
Patch0:		abf.oma.patch
Patch1:		abf_defaults.patch
Patch2:		abf_git.patch
Patch3:		missing_fields.patch
Patch4:		abf-console-client-v2.7-use-cached-chroot-by-default-fix-extra-tests.patch
Patch5:		abf-console-client-v2.7-i686-for-cooker-and-4.0.patch
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
Provides:	abf = %{EVRD}
Provides:	abfcc = %{EVRD}
Provides:	abf-c-c = %{EVRD}

%description
Console client for ABF (https://abf.openmandriva.org).

%package -n python-abf
Summary:	Python API for ABF (https://abf.openmandriva.org)
Group:		System/Configuration/Packaging
Requires:	python < 3.0

%description -n python-abf
%{name} is the python API to ABF (https://abf.openmandriva.org).
It contains a set of basic operations, done with either HTML
parsing or through ABF json API. It also provides datamodel to
operate with.

%prep
%setup -qn %{name}-v%{version}
%apply_patches

%build
cd po
%make
cd ..

%install
make install DESTDIR=%{buildroot} PYTHON=python2

sed -i -e 's,#!%{_bindir}/python,#!%{_bindir}/python2,' %{buildroot}%{_bindir}/abf
install -m 0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{buildroot}%{_sysconfdir}/abf/mock-urpm/configs/

ln -s %{_datadir}/bash-completion/abf %{buildroot}/%{_sysconfdir}/bash_completion.d/abf
cd po
%makeinstall_std
cd ..

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
