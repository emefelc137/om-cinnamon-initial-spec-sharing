Name:		mint-x-icons
Version:	1.7.9
Release:	1
Source0:	https://github.com/linuxmint/mint-x-icons/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	Icon theme for Linux Mint
URL:		https://github.com/linuxmint/mint-x-icons
License:	GPL-3.0-or-later
Group:          Graphical desktop/Other

BuildArch:      noarch
 
BuildRequires:  fdupes
 
Requires:       filesystem
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme
 
%description
%{summary}.
 
 
%prep
%autosetup -c
 
%install
%{__cp} -pr %{name}-%{version}%{_prefix} %{buildroot}
%fdupes -s %{buildroot}
 
 
%transfiletriggerin -- %{_datadir}/icons/Mint-X
for _dir in %{_datadir}/icons/Mint-X*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done
 
 
%transfiletriggerpostun -- %{_datadir}/icons/Mint-X
for _dir in %{_datadir}/icons/Mint-X*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done
 
 
%files
%license %{name}-%{version}/debian/copyright
%doc %{name}-%{version}/debian/changelog
%{_datadir}/icons/Mint-X*
%{_datadir}/folder-color-switcher/
