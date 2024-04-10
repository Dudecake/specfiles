#!/bin/sh

set -e

../create-cosmic-spec.sh cosmic-applets '' cosmic-applet

exec ../build-rpm.sh "$@"
