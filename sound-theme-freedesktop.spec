Summary:	freedesktop.org default sound theme
Name:		sound-theme-freedesktop
Version:	0.7
Release:	%mkrel 1
Group:		System/X11
# For details on the licenses used, see README
License:	GPLv2+ and LGPLv2+ and CC-BY-SA and CC-BY
Url:		http://www.freedesktop.org/wiki/Specifications/sound-theme-spec
Source0:	http://people.freedesktop.org/~mccann/dist/%{name}-%{version}.tar.bz2
BuildRequires:	intltool
BuildArch:	noarch
Provides:	fdo-sound-theme
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The default freedesktop.org sound theme following the XDG theming
specification.  (http://0pointer.de/public/sound-theme-spec.html).

%prep
%setup -q

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

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
%doc README NEWS
%dir %{_datadir}/sounds/freedesktop
%dir %{_datadir}/sounds/freedesktop/stereo
%{_datadir}/sounds/freedesktop/index.theme
%{_datadir}/sounds/freedesktop/stereo/*.ogg
