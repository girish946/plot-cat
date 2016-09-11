# Created by pyp2rpm-3.1.3
%global pypi_name plotcat

%if 0%{?fedora}
%global with_python3 1
%endif



Name:           python-%{pypi_name}
Version:        1.0.0
Release:        2%{?dist}
Summary:        Tool to plot live serial input

License:        GPLv3
URL:            https://github.com/girish946/plot-cat
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
Tool to plot live serial input. plotcat works on python 2.7 and later.
plotcat comes handy when you want to plot live data that is coming form
different sensors over the serial port. For example you have to plot the output
of a temperature sensor that is coming from an Arduino or any other
micro controller for that matter; plotcat comes handy for such tasks. plotcat
sits on the top of Matplotlib and does all the initialization and drawing stuff
itself. you just have to provide the list of values to be plotted.

%package -n     python2-%{pypi_name}
Summary:        Tool to plot live serial input
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-matplotlib
Requires:       pyserial
%description -n python2-%{pypi_name}
Tool to plot live serial input

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Tool to plot live serial input
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-matplotlib
Requires:       python3-pyserial
%description -n python3-%{pypi_name}
Tool to plot live serial input
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' *.py

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%if 0%{?with_python3}
%py3_install
cp %{buildroot}/%{_bindir}/live_plot.py %{buildroot}/%{_bindir}/live_plot.py-3
ln -sf %{_bindir}/live_plot.py-3 %{buildroot}/%{_bindir}/live_plot.py-%{python3_version}
%endif

%py2_install
cp %{buildroot}/%{_bindir}/live_plot.py %{buildroot}/%{_bindir}/live_plot.py-2
ln -sf %{_bindir}/live_plot.py-2 %{buildroot}/%{_bindir}/live_plot.py-%{python2_version}


%files -n python2-%{pypi_name}
%license LICENSE
%doc 
%{_bindir}/live_plot.py
%{_bindir}/live_plot.py-2
%{_bindir}/live_plot.py-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}

%files -n python3-%{pypi_name}
%license LICENSE
%doc 
%{_bindir}/live_plot.py-3
%{_bindir}/live_plot.py-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Sun Aug 28 2016 girish joshi <girish946@gmail.com> - 1.0.0-2
- Initial package.
- Builds for python2 and 3 corrected.
