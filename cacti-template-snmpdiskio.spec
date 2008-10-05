# TODO
# - %%post - add template to cacti
%define		realname	snmpdiskio
%include	/usr/lib/rpm/macros.perl
Summary:	Disk I/O statistics (Read/Write bytes) in Cacti
Summary(pl.UTF-8):	Statystyki operacji dyskowych we/wy (odczyt/zapis w bajtach) w Cacti
Name:		cacti-addons-snmpdiskio
Version:	0.9.4
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#  snmpdiskio 0.9.4 (Disk I/O statistics on Linux) - http://forums.cacti.net/about12742.html
Source0:	http://forums.cacti.net/files/%{realname}-%{version}.tar.gz
# Source0-md5:	9f3512729ae6cad0904cac0fada719eb
URL:		http://www.debianhelp.co.uk/cactitemplates.htm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti

%description
Disk I/O statistics (Read/Write bytes) in Cacti.

%description -l pl.UTF-8
Statystyki operacji dyskowych wejścia/wyjścia (odczyt/zapis w bajtach)
w Cacti.

%package -n snmpdiskio
Summary:	Disk I/O statistics (Read/Write bytes) over SNMP
Summary(pl.UTF-8):	Statystyki operacji dyskowych we/wy (odczyt/zapis w bajtach) po SNMP
Group:		Applications

%description -n snmpdiskio
This set of simple scripts gives you disk I/O statistics over SNMP;
currently net-snmp has flaky or no support for disk I/O at all. This
version gives you only one thing: Disk I/O (bytes/sec).

%description -n snmpdiskio -l pl.UTF-8
Ten zestaw prostych skryptów udostępnia statystyki wejścia/wyjścia dla
dysków po SNMP; aktualnie net-snmp ma kiepską albo żadną obsługę
dyskowego wejścia/wyjścia. Ta wersja udostępnia tylko jedną wartość:
Disk I/O (w bajtach/sekundę).

%prep
%setup -q -n %{realname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{cactidir}/cacti,%{cactidir}/scripts,%{cactidir}/resource/script_queries,%{cactidir}/resource/snmp_queries,%{cactidir}/resource/script_server,%{_bindir}}
install cacti_data_query_snmp_disk_statistics.xml $RPM_BUILD_ROOT%{cactidir}/resource/script_queries
install cacti_graph_template_disk_io_bytessec.xml $RPM_BUILD_ROOT%{cactidir}/resource/script_queries
install partition.xml  $RPM_BUILD_ROOT%{cactidir}/resource/snmp_queries
install snmpdiskio $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{cactidir}/resource/script_queries/cacti_data_query_snmp_disk_statistics.xml
%{cactidir}/resource/script_queries/cacti_graph_template_disk_io_bytessec.xml
%{cactidir}/resource/snmp_queries/partition.xml

%files -n snmpdiskio
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/snmpdiskio
