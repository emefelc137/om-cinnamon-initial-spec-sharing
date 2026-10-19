Name:		mint-y-icons
Version:	1.9.6
Release:	1
Source0:	https://github.com/linuxmint/mint-y-icons/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	The Mint-Y icon theme
URL:		https://github.com/linuxmint/mint-y-icons
License:	LicenseRef-Callaway-CC-BY-SA
Group:		Graphical desktop/Other

BuildArch:      noarch
 
BuildRequires:  fdupes
 
Requires:       filesystem
Requires:       mint-x-icons
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme
 
%description
%{summary}.
 
%prep
%autosetup

%build
 
%install
%{__cp} -pr ${PWD}%{_prefix} %{buildroot}
%fdupes -s %{buildroot}
 
%transfiletriggerin -- %{_datadir}/icons/Mint-Y
for _dir in %{_datadir}/icons/Mint-Y*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done
 
%transfiletriggerpostun -- %{_datadir}/icons/Mint-Y
for _dir in %{_datadir}/icons/Mint-Y*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done
 
%files
%license debian/copyright
%doc debian/changelog
%doc README.md
%{_datadir}/icons/Mint-*/
%{_datadir}/folder-color-switcher/
