Summary:	freedesktop.org default sound theme
Name:		sound-theme-freedesktop
Version:	0.8
Release:	5
Group:		System/X11
# For details on the licenses used, see README
License:	GPLv2+ and LGPLv2+ and CC-BY-SA and CC-BY
Url:		http://www.freedesktop.org/wiki/Specifications/sound-theme-spec
Source0:	http://people.freedesktop.org/~mccann/dist/%{name}-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	gettext-devel 
BuildRequires:	glib-gettextize
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch
Provides:	fdo-sound-theme
Obsoletes:	gnome-audio <= 2.22.2
Provides:	gnome-audio 
Obsoletes:	gnome-audio-extra <= 2.22.2
Provides:	gnome-audio-extra <= 2.22.2

%description
The default freedesktop.org sound theme following the XDG theming
specification.  (http://0pointer.de/public/sound-theme-spec.html).

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

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
%doc README NEWS
%dir %{_datadir}/sounds/freedesktop
%dir %{_datadir}/sounds/freedesktop/stereo
%{_datadir}/sounds/freedesktop/index.theme
%{_datadir}/sounds/freedesktop/stereo/*.oga


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7-4mdv2011.0
+ Revision: 670000
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-3mdv2011.0
+ Revision: 607550
- rebuild

* Mon Apr 19 2010 Frederic Crozat <fcrozat@mandriva.com> 0.7-2mdv2010.1
+ Revision: 536717
- gnome-audio is dead, replace it with sound-theme-freedesktop

* Sat Feb 20 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7-1mdv2010.1
+ Revision: 508832
- fix the package
- update to new version 0.7

* Fri Aug 28 2009 Colin Guthrie <cguthrie@mandriva.org> 0.6-1mdv2010.0
+ Revision: 421954
- New version: 0.6

* Thu Aug 27 2009 Colin Guthrie <cguthrie@mandriva.org> 0.5-1mdv2010.0
+ Revision: 421658
- New version: 0.5

* Tue Aug 25 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4-1mdv2010.0
+ Revision: 420651
- update to new version 0.4

* Wed Jul 29 2009 Colin Guthrie <cguthrie@mandriva.org> 0.3-1mdv2010.0
+ Revision: 402876
- New version: 0.3

* Tue Jan 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-1mdv2009.1
+ Revision: 331822
- use autotools magic ;)
- ann buildrequires on intltool
- spec file clean
- update to new version 0.2
- fix url for source
- fix docs

* Sat Sep 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.1-2mdv2009.0
+ Revision: 284484
- Update to touch the /usr/share/sounds folder to reload sound themes in libcanberra

* Mon Jul 28 2008 Colin Guthrie <cguthrie@mandriva.org> 0.1-1mdv2009.0
+ Revision: 250737
- Update group
- Update summary
- Add generic provides
- Import sound-theme-freedesktop (based on RH package by Lennart Pottering)


