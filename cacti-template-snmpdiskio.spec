%define		plugin	snmpdiskio
Summary:	Disk I/O statistics (Read/Write bytes) in Cacti
Summary(pl.UTF-8):	Statystyki operacji dyskowych we/wy (odczyt/zapis w bajtach) w Cacti
Name:		cacti-addons-snmpdiskio
Version:	0.9.6
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://forums.cacti.net/files/%{plugin}-0.9.4.tar.gz
# Source0-md5:	9f3512729ae6cad0904cac0fada719eb
Patch0:		%{name}-bashism.patch
Patch1:		%{name}-0.9.6.patch
URL:		http://forums.cacti.net/about12742.html
Requires:	cacti-add_template
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
Requires:	awk

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
%setup -q -c -n %{plugin}-%{version}
mv %{plugin}-*/* .
%patch0 -p1
%patch1 -p1

cat > snmpd.%{plugin}.conf <<'EOF'
exec .1.3.6.1.4.1.2021.54 hdNum %{_sbindir}/snmpdiskio hdNum
exec .1.3.6.1.4.1.2021.55 hdIndex %{_sbindir}/snmpdiskio hdIndex
exec .1.3.6.1.4.1.2021.56 hdDescr %{_sbindir}/snmpdiskio hdDescr
exec .1.3.6.1.4.1.2021.57 hdInBlocks %{_sbindir}/snmpdiskio hdInBlocks
exec .1.3.6.1.4.1.2021.58 hdOutBlocks %{_sbindir}/snmpdiskio hdOutBlocks
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{cactidir}/resource/script_queries,%{cactidir}/resource/snmp_queries,%{_sbindir}}
install cacti_data_query_snmp_disk_statistics.xml $RPM_BUILD_ROOT%{cactidir}/resource/script_queries
install cacti_graph_template_disk_io_bytessec.xml $RPM_BUILD_ROOT%{cactidir}/resource/script_queries
install partition.xml  $RPM_BUILD_ROOT%{cactidir}/resource/snmp_queries
install snmpdiskio $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/cacti-add_template \
	%{cactidir}/resource/script_queries/cacti_data_query_snmp_disk_statistics.xml \
	%{cactidir}/resource/script_queries/cacti_graph_template_disk_io_bytessec.xml \
	%{cactidir}/resource/snmp_queries/partition.xml

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{cactidir}/resource/script_queries/cacti_data_query_snmp_disk_statistics.xml
%{cactidir}/resource/script_queries/cacti_graph_template_disk_io_bytessec.xml
%{cactidir}/resource/snmp_queries/partition.xml

%files -n snmpdiskio
%defattr(644,root,root,755)
%doc README snmpd.%{plugin}.conf
%attr(755,root,root) %{_sbindir}/snmpdiskio
