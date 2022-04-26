Name:           python-pack-script
Version:        0.0.1
Release:        1%{?dist}
Summary:        Test RPM package builder for python package
BuildArch:      noarch

License:        GPL
URL:            https://github.com/mbrav/rpm-python-pack
Source0:        %{name}-%{version}.tar.gz

Requires:       python3

%description
Test RPM package builder for python package

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name}.sh $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}.sh

%changelog
* Sun Nov  18 2020 Valentin Bajrami <valentin.bajrami@slimmer.ai> - 0.0.1
- First version being packaged