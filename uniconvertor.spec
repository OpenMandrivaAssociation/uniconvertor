%define python_compile_opt python2 -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python2 -c "import compileall; compileall.compile_dir('.')"

Name:           uniconvertor
Version:        1.1.5
Release:        6
Summary:        Universal vector graphics translator
Group:          Graphics
License:        LGPLv2+ and GPLv2+ and MIT
URL:            http://sk1project.org/modules.php?name=Products&product=uniconvertor
Source0:        http://uniconvertor.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         uniconvertor-underlinking.patch
BuildRequires:  python2-devel
Requires:       python2-imaging
Requires:       python-reportlab
Requires:       sk1libs

%description
UniConvertor is a universal vector graphics translator.
It uses sK1 engine to convert one format to another.

%prep
%setup -q -n uniconvertor-%{version}
%patch0 -p1 -b .underlink

%build
CFLAGS="%{optflags}" %{__python2} setup.py build

%install
rm -rf %{buildroot}
%{__python2} setup.py install --skip-build --root %{buildroot} 

# Fix permissions
chmod a+x %{buildroot}%{python2_sitearch}/uniconvertor/__init__.py
chmod g-w %{buildroot}%{python2_sitearch}/uniconvertor/app/modules/*.so

# Don't duplicate documentation
rm -f %{buildroot}%{python2_sitearch}/uniconvertor/{COPYRIGHTS,GNU_GPL_v2,GNU_LGPL_v2}

# Satisfy rpmlint claim on debuginfo subpackage
chmod 644 src/modules/*/*.{c,h}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%doc src/COPYRIGHTS
%{_bindir}/uniconvertor
%{py2_platsitedir}/*


%changelog
* Sat Mar 10 2012 Thomas Spuhler <tspuhler@mandriva.org> 1.1.5-4mdv2012.0
+ Revision: 783909
- dropped UniConvertor-1.1.0-simplify.patch
  added uniconvertor-underlinking.patch
  added Requires: sk1libs to make it work

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 1.1.5-2mdv2011.0
+ Revision: 590057
- rebuild for python 2.7

* Sun Aug 15 2010 Funda Wang <fwang@mandriva.org> 1.1.5-1mdv2011.0
+ Revision: 569891
- new version 1.1.5

* Tue Mar 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.1.4-1mdv2010.1
+ Revision: 516854
- drop patches that breaks build (but keep them)
- update to 1.1.4

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.1.3-3mdv2010.0
+ Revision: 445612
- rebuild

* Thu Dec 25 2008 Michael Scherer <misc@mandriva.org> 1.1.3-2mdv2009.1
+ Revision: 318500
- rebuild for new python

* Fri Sep 12 2008 Frederik Himpe <fhimpe@mandriva.org> 1.1.3-1mdv2009.0
+ Revision: 284261
- First uniconvertor package for Mandriva, with thanks to Fedora for
  their SPEC and patches
- create uniconvertor

