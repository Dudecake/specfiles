#
# spec file for package system-user-root
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           system-user-root
Version:        20221103
Release:        0
Summary:        System user and group root
License:        MIT
Group:          System/Fhs
Source1:        system-user-root.conf
BuildArch:      noarch
Provides:       group(root)
Provides:       group(shadow)
Provides:       group(trusted)
Provides:       group(users)
Provides:       user(root)
#!BuildIgnore: group(root)
#!BuildIgnore: group(trusted)
#!BuildIgnore: user(root)

%description
This package provides the root account including the groups root,
shadow and users.

%prep
%setup -q -c -T

%build

%install
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/system-user-root.conf

%pre
if [[ ! -d /etc ]]; then
    mkdir /etc
fi
if [[ ! -f /etc/passwd ]]; then
    echo "root:x:0:0:root:/root:/bin/bash" >> /etc/passwd
    chmod 644 /etc/passwd
fi
if [[ ! -f /etc/group ]]; then
    echo -e "root:x:0:\nshadow:x:15:\ntrusted:x:42:\nusers:x:100:" >> /etc/group
    chmod 644 /etc/group
fi
if [[ ! -f /etc/shadow ]]; then
    echo "root:*:$[$(date -u +%s) / 86400]::::::" >> /etc/shadow
    chown 0:15 /etc/shadow
    chmod 640 /etc/shadow
fi

%files
%defattr(-,root,root)
%{_sysusersdir}/system-user-root.conf

%changelog
