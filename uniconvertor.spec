%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"



Name:           uniconvertor
Version:        1.1.4
Release:        %mkrel 1
Summary:        Universal vector graphics translator
Group:          Graphics
License:        LGPLv2+ and GPLv2+ and MIT
URL:            http://sk1project.org/modules.php?name=Products&product=uniconvertor
Source0:        http://sk1project.org/downloads/uniconvertor/v%{version}/%{name}-%{version}.tar.gz
Patch0:         UniConvertor-1.1.0-simplify.patch
Patch1:         UniConvertor-1.1.1-rename-in-help.patch
Patch2:         UniConvertor-1.1.1-use-exec.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  python-devel
Requires:       python-imaging
Requires:       python-reportlab


%description
UniConvertor is a universal vector graphics translator.
It uses sK1 engine to convert one format to another.

%prep
%setup -q -n UniConvertor-%{version}
%patch0 -p1 -b .simplify
#%patch1 -p1 -b .rename-in-help
#%patch2 -p1 -b .use-exec

# Prepare for inclusion into documentation part
install -p -m644 src/COPYRIGHTS COPYRIGHTS

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

# Rename uniconv script due to conflicts with netatalk
# (https://bugzilla.redhat.com/show_bug.cgi?id=405011)
mv %{buildroot}%{_bindir}/uniconv %{buildroot}%{_bindir}/uniconvertor


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README
%doc COPYRIGHTS 
%{_bindir}/uniconvertor
%{py_platsitedir}/*

