Summary:	Package containing distro specific configuration and gschema overrides for Cinnamon
Name:		openmandriva-cinnamon-config
Version:	6.8.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/Cinnamon
Url:		https://www.openmandriva.org
Source0:	90_cinnamon-openmandriva.gschema.override
Source1:	settings-override.json
BuildArch:	noarch

Requires:	glib2.0-common
Requires:	distro-release
Requires:	cinnamon
Requires:	mint-x-icons
Requires:       mint-y-icons
Requires:       mint-themes
Requires:       cinnamon-themes

%description
This package contains distro specific configuration and gschema
overrides for the Cinnamon desktop.

%files
%{_datadir}/glib-2.0/schemas/90_cinnamon-openmandriva.gschema.override
%{_datadir}/cinnamon/applets/calendar@cinnamon.org/settings-override.json

#----------------------------------------------------------------------------

%prep
# nothing to do here!

%build
# nothing to do here!

%install
install -dm 0755 %{buildroot}%{_datadir}/glib-2.0/schemas/
install -dm 0755 %{buildroot}%{_datadir}/cinnamon/applets/calendar@cinnamon.org/
install -pm 0644 %{SOURCE0} %{buildroot}%{_datadir}/glib-2.0/schemas/
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/cinnamon/applets/calendar@cinnamon.org/

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
