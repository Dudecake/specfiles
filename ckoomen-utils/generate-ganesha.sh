#!/bin/bash

if [[ $# -ne 2 ]]; then
  echo "${0} requires exactly 2 arguments" >&2
fi

export_id=12345
server_addr="${1}"
addrs=""
shift

cat << EOF
NFS_CORE_PARAM {
    ## Allow NFSv3 to mount paths with the Pseudo path, the same as NFSv4,
    ## instead of using the physical paths.
    mount_path_pseudo = true;
}

NFSV4 {
    GRACELESS = true;
}

_9P {
    _9P_TCP_Port = 564;
}
EOF

gluster_volumes=$(gluster volume list)

for gluster_volume in ${gluster_volumes[@]}; do
cat << EOF

EXPORT {
    Export_Id = ${export_id};
    Path = /${gluster_volume};
    Pseudo = /${gluster_volume};
    Squash = no_root_squash;
    #Sectype = sys,krb5,krb5i,krb5p;
    FSAL {
        Name = GLUSTER;
        Hostname = "${server_addr}";
        Volume = "${gluster_volume}";
    }
    CLIENT {
        clients = "$@";
        access_type = "RW";
    }
}
EOF
export_id=$((${export_id}+1))
done
