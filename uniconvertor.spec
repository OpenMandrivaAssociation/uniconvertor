%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

Name:           uniconvertor
Version:        1.1.5
Release:        %mkrel 4
Summary:        Universal vector graphics translator
Group:          Graphics
License:        LGPLv2+ and GPLv2+ and MIT
URL:            http://sk1project.org/modules.php?name=Products&product=uniconvertor
Source0:        http://uniconvertor.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         uniconvertor-underlinking.patch
BuildRequires:  python-devel
Requires:       python-imaging
Requires:       python-reportlab
Requires:       sk1libs

%description
UniConvertor is a universal vector graphics translator.
It uses sK1 engine to convert one format to another.

%prep
%setup -q -n uniconvertor-%{version}
%patch0 -p1 -b .underlink

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot} 

# Fix permissions
chmod a+x %{buildroot}%{python_sitearch}/uniconvertor/__init__.py
chmod g-w %{buildroot}%{python_sitearch}/uniconvertor/app/modules/*.so

# Don't duplicate documentation
rm -f %{buildroot}%{python_sitearch}/uniconvertor/{COPYRIGHTS,GNU_GPL_v2,GNU_LGPL_v2}

# Satisfy rpmlint claim on debuginfo subpackage
chmod 644 src/modules/*/*.{c,h}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%doc src/COPYRIGHTS
%{_bindir}/uniconvertor
%{py_platsitedir}/*
