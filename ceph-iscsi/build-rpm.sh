#!/bin/sh

curl -LO https://github.com/ceph/ceph-iscsi/raw/main/ceph-iscsi.spec

exec ../build-rpm.sh "$@"
