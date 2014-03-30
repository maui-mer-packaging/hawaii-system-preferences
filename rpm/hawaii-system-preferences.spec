# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       hawaii-system-preferences

# >> macros
# << macros

Summary:    Hawaii system preferences
Version:    0.2.0.1.20140301.24fa434
Release:    1
Group:      Applications/System
License:    LGPLv2.1+ and GPLv2+
URL:        https://github.com/mauios/hawaii-system-preferences.git
Source0:    hawaii-system-preferences-%{version}.tar.xz
Source100:  hawaii-system-preferences.yaml
Requires:   libhawaii
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  cmake
BuildRequires:  bzip2-devel
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qtaccountsservice-devel
BuildRequires:  qtconfiguration-devel
BuildRequires:  libhawaii-devel
BuildRequires:  desktop-file-utils

%description
Provides preferences for the Hawaii desktop environment.

%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.LIB README
%{_bindir}/hawaii-system-preferences
%dir %{_datadir}/hawaii-system-preferences
%dir %{_datadir}/hawaii-system-preferences/translations
%{_datadir}/hawaii-system-preferences/translations/*.qm
%{_datadir}/hawaii-system-preferences/plugins/*/translations/*.qm
%{_datadir}/applications/*.desktop
%dir %{_libdir}/hawaii/plugins/preferences
%{_libdir}/hawaii/plugins/preferences/*.so
# >> files
# << files
