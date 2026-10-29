Summary:	Package containing distro specific configuration and gschema overrides for Cinnamon
Name:		openmandriva-cinnamon-config
Version:	6.6.9
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/Cinnamon
Url:		https://www.openmandriva.org
Source0:	90_cinnamon-openmandriva.gschema.override
BuildArch:	noarch

Requires:	glib2.0-common
Requires:	distro-release
Requires:	mint-x-icons
Requires:       mint-y-icons
Requires:       mint-themes
Requires:       cinnamon-themes

%description
This package contains distro specific configuration and gschema
overrides for the Cinnamon desktop.

%files
%{_datadir}/glib-2.0/schemas/90_cinnamon-openmandriva.gschema.override

#----------------------------------------------------------------------------

%prep
# nothing to do here!

%build
# nothing to do here!

%install
install -dm 0755 %{buildroot}%{_datadir}/glib-2.0/schemas/
install -pm 0644 %{SOURCE0} %{buildroot}%{_datadir}/glib-2.0/schemas/

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
