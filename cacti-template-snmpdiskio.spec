#	- %post - add template to cacti
%define		realname	snmpdiskio
%include	/usr/lib/rpm/macros.perl
Summary:	Disk i/o statistics (Read/Write bytes) in Cacti 
Summary(pl.UTF-8):	Statystyki operacji I/O (Odczyt/Zapis w bajtach) dysków w Cacti
Group:		Applications/WWW
Name:		cacti-addons-snmpdiskio
Version:	0.9.4
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#  snmpdiskio 0.9.4 (Disk I/O statistics on Linux) - http://forums.cacti.net/about12742.html
Source0:	http://forums.cacti.net/files/%{realname}-%{version}.tar.gz
# Source7-md5:	9f3512729ae6cad0904cac0fada719eb
URL:		http://www.debianhelp.co.uk/cactitemplates.htm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactiroot		/usr/share/cacti
%define		webcactiscriptdir	%{webcactiroot}/scripts
%define		webcactiscrptserverdir	%{webcactiroot}/resource/script_server
%define		webcactiscriptqueriesdir %{webcactiroot}/resource/script_queries
%define		webcactisnmpqueriesdir	%{webcactiroot}/resource/snmp_queries

%description
Disk i/o statistics (Read/Write bytes) in Cacti.

%description -l pl.UTF-8
Statystyki operacji I/O (Odczyt/Zapis w bajtach) dysków w Cacti

%package -n snmpdiskio
Summary:	Disk i/o statistics (Read/Write bytes) over SNMP
Summary(pl.UTF-8):	Statystyki operacji I/O (Odczyt/Zapis w bajtach) po SNMP
Group:		Applications

%description -n snmpdiskio
Disk i/o statistics (Read/Write bytes) over SNMP.
This set of simple scripts gives you disk I/O support.
Currently net-snmp has flaky or no support for disk I/O at all.
This version: 0.9.4, gives you only one thing: Disk I/O (bytes/sec).

snmpdiskio 0.9.4 has been tested on:
* Linux 2.4 with /proc/partitions iostats patch (included by default in RHEL3)
* Linux 2.6 (/proc/diskstats)
* Net-snmp 5.0.9

%description -n snmpdiskio -l pl.UTF-8
Statystyki operacji I/O (Odczyt/Zapis w bajtach) dysków po SNMP.

%prep
%setup -q -n %{realname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{webcactiroot}/cacti,%{webcactiscriptdir},%{webcactiscriptqueriesdir},%{webcactisnmpqueriesdir},%{webcactiscrptserverdir},%{_bindir}}

install cacti_data_query_snmp_disk_statistics.xml $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}
install cacti_graph_template_disk_io_bytessec.xml $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}
install partition.xml  $RPM_BUILD_ROOT%{webcactisnmpqueriesdir}
install snmpdiskio $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{webcactiscriptqueriesdir}/cacti_data_query_snmp_disk_statistics.xml
%{webcactiscriptqueriesdir}/cacti_graph_template_disk_io_bytessec.xml
%{webcactisnmpqueriesdir}/partition.xml

%files -n snmpdiskio
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/snmpdiskio
