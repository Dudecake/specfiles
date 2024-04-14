#!/bin/sh

set -e

../create-cosmic-spec.sh cosmic-icons 'System76 Cosmic icon theme for Linux'

exec ../build-rpm.sh "$@"
