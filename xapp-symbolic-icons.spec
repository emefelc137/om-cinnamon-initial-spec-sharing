Name:		xapp-symbolic-icons
Version:        1.1.0
Release:	1
Source0:	https://github.com/xapp-project/xapp-symbolic-icons/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	A set of symbolic icons which replaces the GNOME-specific Adwaita set
URL:            https://github.com/xapp-project/xapp-symbolic-icons
License:        CC0-1.0 AND CC-BY-SA-4.0 AND LGPL-3.0-only AND MIT
Group:		Graphical desktop/Other
BuildRequires:	meson
BuildSystem:	meson
Requires:       hicolor-icon-theme
BuildArch:      noarch
 
%description
A set of symbolic icons which replaces the GNOME-specific Adwaita set.
All provided icons are prefixed with xsi-.
Icon names loosely follow the Adwaita names.
 
%prep
%autosetup -p1
 
%build
%meson
%meson_build
%install
%meson_install
%transfiletriggerin -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :
 
%transfiletriggerpostun -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :
 
%files
%license LICENSE LICENSES/*.txt
%doc AUTHORS README.md
%{_bindir}/xsi-replace-adwaita-symbolic
%{_datadir}/icons/hicolor/scalable/actions/xsi-*.svg
%{_datadir}/xapp/
