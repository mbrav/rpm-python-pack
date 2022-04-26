%{!?_version: %define _version 0.0.1 }
%global srcname python-pack-script


Name:           %{srcname}
Version:        %{_version} 
Release:        1%{?dist}
Summary:        Test RPM package builder for python package
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tar.gz

BuildArch:       noarch
BuildRequires:   python3-devel python3-setuptools
Requires:        python3

%description
Test RPM package builder for python package


%changelog
* 0.0.1
- First version being packaged