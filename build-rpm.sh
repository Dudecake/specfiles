#!/bin/sh

set -ex
SPEC_FILE="$(ls -1 ./*.spec | head -n1)"
RPM_FILE=$(python3 -c "import specfile; print(specfile.Specfile(\"${SPEC_FILE}\").expand(\"%name-%version-%release.src.rpm\"))")
if [[ ! -z "${FORCE_REBUILD}" || ! -f "${2}/source/tree/${RPM_FILE}" ]]; then
  spectool -g -R ./*.spec
  spectool ./*.spec | grep -Po '(?<=: )(?!http).+' | xargs -I{} cp {} $(rpm -E '%{_sourcedir}')
  rpmbuild -bs ./*.spec -D "_srcrpmdir ${PWD}"
  dnf builddep -y ./*.src.rpm
  rpmbuild --rebuild ./*.src.rpm -D "_rpmdir ${1}" -D "_srcrpmdir ${1}"
  mv ./*.src.rpm "${1}/source"
else
  rm -f ./*.src.rpm
  echo "No rebuild neccesary for package $(basename $PWD)" >&2
fi
