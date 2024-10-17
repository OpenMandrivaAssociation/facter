Name:		facter
Version:	1.6.6
Release:	3
Summary:	Ruby module for collecting simple facts about a host operating system
License:	Apache Software License
Group:		System/Libraries
URL:		https://www.puppetlabs.com/puppet/related-projects/facter/
Source0:	http://www.puppetlabs.com/downloads/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	ruby
Requires:	ruby >= 1.8.1
Requires:	dmidecode
Requires:	lsb-release
# needed for host, in facter/ipaddress.rb
Requires:	bind-utils

%description
Ruby module for collecting simple facts about a host Operating
system. Some of the facts are preconfigured, such as the hostname and the
operating system. Additional facts can be added through simple Ruby scripts

%prep
%setup -q

%build
# Use /usr/bin/ruby directly instead of /usr/bin/env ruby in
#+ executables. Otherwise, initscripts break since pidof can't
#+ find the right process
sed -i -e 's@^#!.*$@#! /usr/bin/ruby@' bin/facter

%install
install -d -m 0755 %{buildroot}%{ruby_sitelibdir}/%{name}
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 0644 lib/*.rb %{buildroot}%{ruby_sitelibdir}
cp -a lib/facter/* %{buildroot}%{ruby_sitelibdir}/%{name}
install -p -m 0755 bin/facter %{buildroot}%{_bindir}

%files
%doc CHANGELOG INSTALL LICENSE
%{_bindir}/facter
%{ruby_sitelibdir}/facter.rb
%{ruby_sitelibdir}/%{name}



%changelog
* Mon Mar 19 2012 Andrey Bondrov <abondrov@mandriva.org> 1.6.6-1mdv2012.0
+ Revision: 785484
- New version 1.6.6, spec cleanup

* Tue Feb 14 2012 Bogdano Arendartchuk <bogdano@mandriva.com> 1.6.3-2
+ Revision: 773894
- rebuild for ruby 1.9

* Wed Nov 30 2011 Andrey Bondrov <abondrov@mandriva.org> 1.6.3-1
+ Revision: 735734
- New version 1.6.3

* Sun Oct 09 2011 Andrey Bondrov <abondrov@mandriva.org> 1.6.1-1
+ Revision: 703890
- New version 1.6.1, new license

* Mon Jun 27 2011 Michael Scherer <misc@mandriva.org> 1.5.9-1
+ Revision: 687395
- update to new version 1.5.9

* Sun Nov 21 2010 Michael Scherer <misc@mandriva.org> 1.5.8-2mdv2011.0
+ Revision: 599427
- fix missing Requires

* Sat Sep 18 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.8-1mdv2011.0
+ Revision: 579558
- update to new version 1.5.8

* Sat Sep 26 2009 Frederik Himpe <fhimpe@mandriva.org> 1.5.7-1mdv2010.0
+ Revision: 449586
- update to new version 1.5.7

* Tue Jun 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1.5.6-1mdv2010.0
+ Revision: 391101
- Update to new version 1.5.6

* Thu Jul 24 2008 Funda Wang <fwang@mandriva.org> 1.5-1mdv2009.0
+ Revision: 245281
- New version 1.5
- drop patch100, merged upstream

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3.8-3mdv2009.0
+ Revision: 245020
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Oct 30 2007 Funda Wang <fwang@mandriva.org> 1.3.8-1mdv2008.1
+ Revision: 103817
- BR ruby
- import facter


* Thu Oct 30 2007 roudoud0u <roudoud0u@free.fr> - 1.3.8-1
- Initial Mandriva rpm package (based on David Lutterkort spec file)

* Thu Mar 29 2007 David Lutterkort <dlutter@redhat.com> - 1.3.7-1
- New version

* Fri Jan 19 2007 David Lutterkort <dlutter@redhat.com> - 1.3.6-1
- New version

* Thu Jan 18 2007 David Lutterkort <dlutter@redhat.com> - 1.3.5-3
- require which; facter is very unhappy without it

* Mon Nov 20 2006 David Lutterkort <dlutter@redhat.com> - 1.3.5-2
- Make require ruby(abi) and buildarch: noarch conditional for fedora 5 or
  later to allow building on older fedora releases

* Tue Oct 10 2006 David Lutterkort <dlutter@redhat.com> - 1.3.5-1
- New version

* Tue Sep 26 2006 David Lutterkort <dlutter@redhat.com> - 1.3.4-1
- New version

* Wed Sep 13 2006 David Lutterkort <dlutter@redhat.com> - 1.3.3-2
- Rebuilt for FC6

* Wed Jun 28 2006 David Lutterkort <dlutter@redhat.com> - 1.3.3-1
- Rebuilt

* Fri Jun 19 2006 Luke Kanies <luke@madstop.com> - 1.3.0-1
- Fixed spec file to work again with the extra memory and processor files.
- Require ruby(abi). Build as noarch

* Fri Jun 9 2006 Luke Kanies <luke@madstop.com> - 1.3.0-1
- Added memory.rb and processor.rb

* Mon Apr 17 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-4
- Rebuilt with changed upstream tarball

* Tue Mar 21 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-3
- Do not rely on install.rb, it will be deleted upstream

* Mon Mar 13 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-2
- Commented out noarch; requires fix for bz184199

* Mon Mar  6 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-1
- Removed unused macros

* Mon Feb  6 2006 David Lutterkort <dlutter@redhat.com> - 1.1.1-2
- Fix BuildRoot. Add dist to release tag

* Wed Jan 11 2006 David Lutterkort <dlutter@redhat.com> - 1.1.1-1
- Initial build.
