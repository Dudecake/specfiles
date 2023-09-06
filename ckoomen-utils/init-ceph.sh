#!/bin/bash

if [[ ! -f /etc/ceph/ceph.conf ]]; then
  generate-cephconf.sh "$@" > /etc/ceph/ceph.conf
fi
params=$(getopt -o '' -l cluster-name: -l monmap: -l mon-keyring: -n init-ceph -- "$@")
if [[ $? -ne 0 ]]; then
  exit 1
fi

cluster_name=ceph
hostname=${HOSTNAME:-$(hostname)}
monmap=/tmp/monmap
mon_keyring=/tmp/ceph.mon.keyring
admin_keyring=/etc/ceph/ceph.client.admin.keyring
osd_bootstrap_keyring=/var/lib/ceph/bootstrap-osd/ceph.keyring

eval set -- "$params"
unset params
while :
do
  case "${1}" in
    --cluster-name)
      cluster_name="${2}"
      shift 2
      ;;
    --monmap)
      monmap="${2}"
      shift 2
      ;;
    --mon-keyring)
      mon_keyring="${2}"
      shift 2
      ;;
    --)
      shift
      break
      ;;
  esac
done

if [[ ! -f ${mon_keyring} ]]; then
  ceph-authtool --create-keyring ${mon_keyring} \
                --gen-key -n mon. \
                --cap mon 'allow *'
  if [[ ! -f ${admin_keyring} ]]; then
    ceph-authtool --create-keyring ${admin_keyring} \
                  --gen-key -n client.admin \
                  --cap mon 'allow *' \
                  --cap osd 'allow *' \
                  --cap mds 'allow *' \
                  --cap mgr 'allow *'
  fi
  if [[ ! -f ${osd_bootstrap_keyring} ]]; then
    ceph-authtool --create-keyring ${osd_bootstrap_keyring} \
                  --gen-key -n client.bootstrap-osd \
                  --cap mon 'profile bootstrap-osd' \
                  --cap mgr 'allow r'
  fi
  ceph-authtool ${mon_keyring} --import-keyring ${admin_keyring}
  ceph-authtool ${mon_keyring} --import-keyring ${osd_bootstrap_keyring}
  chown ceph:ceph ${mon_keyring}
fi

if [[ ! -f ${monmap} ]]; then
  echo 'Please create a monmap following the instructions on <https://docs.ceph.com/en/quincy/install/manual-deployment/#monitor-bootstrapping> before re-running this script' >&2
  exit 1
fi

if [[ ! -d /var/lib/ceph/mon/${cluster_name}-${hostname} ]]; then
  sudo -u ceph mkdir /var/lib/ceph/mon/${cluster_name}-${hostname}
  sudo -u ceph ceph-mon --mkfs
                        -i ${hostname} \
                        --monmap ${monmap} \
                        --keyring ${mon_keyring}
  if [[ $(command -v firewall-cmd) != '' ]]; then
    firewall-cmd --zone=public --add-service=ceph-mon
    firewall-cmd --zone=public --add-service=ceph-mon --permanent
  fi
  systemctl enable --now ceph-mon@${hostname}
fi

if [[ ! -d /var/lib/ceph/mgr/${cluster_name}-${hostname} ]]; then
  sudo -u ceph mkdir /var/lib/ceph/mgr/${cluster_name}-${hostname}
  ceph auth get-or-create mgr.${hostname} mon 'allow profile mgr' osd 'allow *' mds 'allow *' > /var/lib/ceph/mgr/${cluster_name}-${hostname}/keyring
  chown -R ceph:ceph /var/lib/ceph/mgr/${cluster_name}-${hostname}
fi

echo 'The cluster should be ready for the creation of OSD\'s following <https://docs.ceph.com/en/quincy/install/manual-deployment/#bluestore>' > &2
