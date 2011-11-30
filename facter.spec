%define name    facter
%define version 1.6.3
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Ruby module for collecting simple facts about a host operating system
License:        Apache Software License
Group:          System/Libraries
URL:            http://www.puppetlabs.com/puppet/related-projects/facter/
Source0:        http://www.puppetlabs.com/downloads/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  ruby
Requires:       ruby >= 1.8.1
Requires:       dmidecode
Requires:       lsb-release
# needed for host, in facter/ipaddress.rb
Requires:       bind-utils
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
%{__sed} -i -e 's@^#!.*$@#! /usr/bin/ruby@' bin/facter

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m 0755 %{buildroot}%{ruby_sitelibdir}/%{name}
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -d -m 0755 %{buildroot}%{_defaultdocdir}/%{name}
%{__install} -p -m 0644 lib/*.rb %{buildroot}%{ruby_sitelibdir}
%{__cp} -a lib/facter/* %{buildroot}%{ruby_sitelibdir}/%{name}
%{__install} -p -m 0755 bin/facter %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGELOG INSTALL LICENSE
%{_bindir}/facter
%{ruby_sitelibdir}/facter.rb
%{ruby_sitelibdir}/%{name}

