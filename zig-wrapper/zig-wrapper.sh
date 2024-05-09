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
if [[ ! -f .zig/wrapper/zig || "\$(sh -c '.zig/wrapper/zig version' 2> /dev/null)" != "\${zig_version}" ]]; then
  [[ -d .zig/wrapper ]] || mkdir -p .zig/wrapper
  arch="\$(uname -m)"
  curl -sSL https://ziglang.org/download/\${zig_version}/zig-linux-\${arch}-\${zig_version}.tar.xz | bsdtar -C .zig/wrapper --strip-components 1 -xf -
  curl -sSL https://github.com/zigtools/zls/releases/download/\${zig_version}/zls-\${arch}-linux.tar.xz | bsdtar -C .zig/wrapper -xf - zls
fi

exec .zig/wrapper/zig "\$@"
EOF
chmod +x ./zigw
