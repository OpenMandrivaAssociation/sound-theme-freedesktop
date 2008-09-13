Name: sound-theme-freedesktop
Version: 0.1
Release: %mkrel 2
Summary: freedesktop.org default sound theme
Group: System/X11
Source0: http://0pointer.de/public/sound-theme-freedesktop.tar.gz
# For details on the licenses used, see README
License: GPLv2+ and LGPLv2+ and CC-BY-SA and CC-BY
Url: http://0pointer.de/public/sound-theme-freedesktop.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Provides: fdo-sound-theme

%description
The default freedesktop.org sound theme following the XDG theming
specification.  (http://0pointer.de/public/sound-theme-spec.html).

%prep
%setup -q -n freedesktop

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/sounds/freedesktop
cp -av index.theme stereo/ %{buildroot}%{_datadir}/sounds/freedesktop

%clean
rm -rf %{buildroot}

# (cg) libcanberra will purge it's cache and reload it's themes
# when the %{_datadir}/sounds folder is touched.
# While it's technically not needed to touch the folder itself,
# the RH rpm still does this so we will too. It may be needed in the
# future :)
%post
touch --no-create %{_datadir}/sounds %{_datadir}/sounds/freedesktop

%postun
touch --no-create %{_datadir}/sounds %{_datadir}/sounds/freedesktop

%files
%defattr(-,root,root)
%doc README
%dir %{_datadir}/sounds/freedesktop
%dir %{_datadir}/sounds/freedesktop/stereo
%{_datadir}/sounds/freedesktop/index.theme
%{_datadir}/sounds/freedesktop/stereo/*.ogg
