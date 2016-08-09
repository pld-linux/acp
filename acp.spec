Summary:	Acp is a rough implementation of an optimized filesystem walker
Name:		acp
Version:	0.6
Release:	1
License:	unknown
Group:		Utilities
Source0:	https://oss.oracle.com/~mason/acp/%{name}-%{version}.tar.bz2
# Source0-md5:	47bbf4a22eaf37d7932ecb92d4c623ce
URL:		https://oss.oracle.com/~mason/acp/
BuildRequires:	rpmbuild(macros) >= 1.318
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Acp is a rough implementation of an optimized filesystem walker. In
general, when doing a full read of a directory tree you touch three
different groups of objects.

Directory data Inode data (things returned by stat(2)) File bodies Acp
creates queues corresponding to each of these groups, and tries to do
work in bulk in each one. As it finds files and directories the are
sorted by either inode number (the default) or by the first block in
the file (acp -b).

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -fno-strict-aliasing"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
