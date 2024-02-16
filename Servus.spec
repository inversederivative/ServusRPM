Name:           Servus
Version:        0.0.2
Release:        1%{?dist}
Summary:        A simple hello world program

License:        MIT
URL:            https://github.com/InverseDerivative/ServusRPM

%description
A simple hello world program.

%prep
mkdir -p %{_builddir}/Servus
cp -r %{_sourcedir}/Servus/* %{_builddir}/Servus
cd %{_builddir}/Servus
cmake .

%build
cd %{_builddir}/Servus
make



%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_builddir}/Servus/Servus %{buildroot}/usr/bin

%files
/usr/bin/Servus

%changelog
* Fri Feb 16 2024 InverseDerivative <InverseDerivative@gmail.com> - 0.0.2-1
- Initial package

