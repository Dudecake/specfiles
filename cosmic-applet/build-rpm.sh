#!/bin/sh

set -e

../create-cosmic-rpm.sh cosmic-applets '' cosmic-applet

exec ../build-rpm.sh "$@"
