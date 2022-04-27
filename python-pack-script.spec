%{!?_version: %define _version 0.0.5 }
%global srcname python-pack-script


Name:           %{srcname}
Version:        %{_version} 
Release:        1%{?dist}
Summary:        Demo RPM builder for python packages
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tar.gz

BuildArch:       noarch
BuildRequires:   python3-devel python3-setuptools
Requires:        python3

%description
Demo RPM builder for python packages


%changelog
* 0.0.5
- First version being packaged