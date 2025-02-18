# COSMIC Desktop meta package
Name:           cosmic-epoch
Version:        1.0.0

Release:        1%{?dist}
Summary:        The next generation COSMIC Desktop Environment

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-epoch

Requires:       cosmic-app-library
Requires:       cosmic-applets
Requires:       cosmic-bg
Requires:       cosmic-comp
Requires:       cosmic-edit
Requires:       cosmic-files
Requires:       cosmic-greeter
Requires:       cosmic-icons
Requires:       cosmic-launcher
Requires:       pop-launcher
Requires:       cosmic-notifications
Requires:       cosmic-osd
Requires:       cosmic-panel
Requires:       cosmic-randr
Requires:       cosmic-screenshot
Requires:       cosmic-session
Requires:       cosmic-settings
Requires:       cosmic-settings-daemon
Requires:       cosmic-store
Requires:       cosmic-term
Requires:       cosmic-workspaces
Requires:       xdg-desktop-portal-cosmic

Provides:       cosmic-desktop

BuildArch:      noarch

%global debug_package %{nil}

%description
%{summary}

%files
