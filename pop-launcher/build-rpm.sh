#!/bin/sh

set -e

install='
install -Dm0755 target/release/pop-launcher-bin %{buildroot}/%{_bindir}/pop-launcher
for plugin in calc desktop_entries files find pop_shell pulse recent scripts terminal web cosmic_toplevel; do
    dest=%{buildroot}/%{_prefix}/lib/pop-launcher/plugins/${plugin}
    mkdir -p ${dest}
    install -Dm0644 plugins/src/${plugin}/*.ron ${dest}
    ln -sf pop-launcher %{buildroot}%{_prefix}/lib/pop-launcher/plugins/${plugin}/$(echo ${plugin} | sed 's/_/-/')
done
mkdir -p %{buildroot}/%{_prefix}/lib/pop-launcher/scripts/
for script in scripts/*; do
    cp -r ${script} %{buildroot}/%{_prefix}/lib/pop-launcher/scripts/
done
'

files="
%{_bindir}/pop-launcher
%{_prefix}/lib/pop-launcher/*
"

install="${install}" files="${files}" ../create-cosmic-spec.sh launcher 'Modular IPC-based desktop launcher service' pop-launcher

exec ../build-rpm.sh "$@"
