#!/bin/bash

set -e

if [[ ! -f build.zig ]]; then
  echo "No 'build.zig' file present" >&2
  exit 1
fi

if [[ -f zigw ]]; then
  echo "Wrapper already installed" >&2
  exit 0
fi

[[ -d .zig/wrapper ]] || mkdir -p .zig/wrapper
cat << EOF > .zig/wrapper/zig-wrapper.properties
zig_version=0.12.0
EOF

cat << EOF > zigw
#!/bin/sh

set -e

. .zig/wrapper/zig-wrapper.properties
wrapper_directory="\${HOME}/.cache/zig/wrapper/\${zig_version}"
if [[ ! -f \${wrapper_directory}/zig || "\$(sh -c "\${wrapper_directory}/zig version" 2> /dev/null)" != "\${zig_version}" ]]; then
  [[ -d \${wrapper_directory} ]] || mkdir -p \${wrapper_directory}
  arch="\$(uname -m)"
  curl -L https://ziglang.org/download/\${zig_version}/zig-linux-\${arch}-\${zig_version}.tar.xz | bsdtar -C \${wrapper_directory} --strip-components 1 -xf -
  curl -L https://github.com/zigtools/zls/releases/download/\${zig_version}/zls-\${arch}-linux.tar.xz | bsdtar -C \${wrapper_directory} -xf - zls
fi

exec \${wrapper_directory}/zig "\$@"
EOF
chmod +x ./zigw
