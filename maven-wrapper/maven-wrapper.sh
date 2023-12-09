#!/bin/bash

set -x

if [[ ! -f pom.xml ]]; then
  echo "No 'pom.xml' file present" >&2
  exit 1
fi

if [[ -f mvnw ]]; then
  echo "Wrapper already installed" >&2
  exit 0
fi

MAVEN_VERSION=${MAVEN_VERSION:-3.9.1}
MAVEN_URL=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/${MAVEN_VERSION}/apache-maven-${MAVEN_VERSION}-bin.zip
WRAPPER_VERSION=${WRAPPER_VERSION:-3.2.0}
WRAPPER_URL=https://repo.maven.apache.org/maven2/org/apache/maven/wrapper/maven-wrapper/${WRAPPER_VERSION}/maven-wrapper-${WRAPPER_VERSION}.jar

curl -sSL --remote-name-all https://github.com/apache/maven-wrapper/raw/maven-wrapper-${WRAPPER_VERSION}/maven-wrapper-distribution/src/resources/mvnw{,.cmd}
chmod +x mvnw
mkdir -p .mvn/wrapper
cat << EOF > .mvn/wrapper/maven-wrapper.properties
distributionUrl=${MAVEN_URL}
wrapperUrl=${WRAPPER_URL}
EOF
curl -L ${WRAPPER_URL} -o .mvn/wrapper/maven-wrapper.jar
