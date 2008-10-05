%define		plugin	snmpdiskio
Summary:	Disk I/O statistics (Read/Write bytes) in Cacti
Summary(pl.UTF-8):	Statystyki operacji dyskowych we/wy (odczyt/zapis w bajtach) w Cacti
Name:		cacti-addons-snmpdiskio
Version:	0.9.6
Release:	3
License:	GPL v2
Group:		Applications/WWW
Source0:	http://forums.cacti.net/files/%{plugin}-0.9.4.tar.gz
# Source0-md5:	9f3512729ae6cad0904cac0fada719eb
Source1:	http://forums.cacti.net//files/partition_424.xml
# Source1-md5:	d7e569dfe417f49c7b8a2fe5b5a52382
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

%prep
%setup -q -c -n %{plugin}-%{version}
mv %{plugin}-*/* .
%patch0 -p1
%patch1 -p1
cp %{SOURCE1} partition.xml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{cactidir}/resource/snmp_queries,%{_sbindir}}
install cacti_data_query_snmp_disk_statistics.xml $RPM_BUILD_ROOT%{cactidir}/resource
install cacti_graph_template_disk_io_bytessec.xml $RPM_BUILD_ROOT%{cactidir}/resource
install partition.xml  $RPM_BUILD_ROOT%{cactidir}/resource/snmp_queries

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/cacti-add_template \
	%{cactidir}/resource/cacti_data_query_snmp_disk_statistics.xml \
	%{cactidir}/resource/cacti_graph_template_disk_io_bytessec.xml

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{cactidir}/resource/cacti_data_query_snmp_disk_statistics.xml
%{cactidir}/resource/cacti_graph_template_disk_io_bytessec.xml
%{cactidir}/resource/snmp_queries/partition.xml
