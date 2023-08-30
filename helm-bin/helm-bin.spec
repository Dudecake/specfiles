%define basearch %_arch
%if "%{basearch}" == "x86_64"
%define basearch amd64
%endif
%if "%{basearch}" == "aarch64"
%define basearch arm64
%endif

Name:           helm-bin
Version:        3.12.3
Release:        1%{?dist}
Summary:        Production-Grade Container Scheduling and Management
URL:            https://github.com/helm/helm
License:        Apache-2.0

Source0:        https://get.helm.sh/helm-v%{version}-linux-%{basearch}.tar.gz

Provides:       helm = %{version}
Provides:       bundled(golang(github.com/asaskevich/govalidator)
Provides:       bundled(golang(github.com/BurntSushi/toml)
Provides:       bundled(golang(github.com/containerd/containerd/content)
Provides:       bundled(golang(github.com/containerd/containerd/errdefs)
Provides:       bundled(golang(github.com/containerd/containerd/remotes)
Provides:       bundled(golang(github.com/cyphar/filepath-securejoin)
Provides:       bundled(golang(github.com/deislabs/oras/pkg/auth)
Provides:       bundled(golang(github.com/deislabs/oras/pkg/auth/docker)
Provides:       bundled(golang(github.com/deislabs/oras/pkg/content)
Provides:       bundled(golang(github.com/deislabs/oras/pkg/context)
Provides:       bundled(golang(github.com/deislabs/oras/pkg/oras)
Provides:       bundled(golang(github.com/docker/distribution/configuration)
Provides:       bundled(golang(github.com/docker/distribution/registry)
Provides:       bundled(golang(github.com/docker/distribution/registry/auth/htpasswd)
Provides:       bundled(golang(github.com/docker/distribution/registry/storage/driver/inmemory)
Provides:       bundled(golang(github.com/docker/docker/pkg/term)
Provides:       bundled(golang(github.com/docker/go-units)
Provides:       bundled(golang(github.com/evanphx/json-patch)
Provides:       bundled(golang(github.com/gobwas/glob)
Provides:       bundled(golang(github.com/gofrs/flock)
Provides:       bundled(golang(github.com/gosuri/uitable)
Provides:       bundled(golang(github.com/jmoiron/sqlx)
Provides:       bundled(golang(github.com/lib/pq)
Provides:       bundled(golang(github.com/Masterminds/semver/v3)
Provides:       bundled(golang(github.com/Masterminds/sprig/v3)
Provides:       bundled(golang(github.com/Masterminds/squirrel)
Provides:       bundled(golang(github.com/Masterminds/vcs)
Provides:       bundled(golang(github.com/mitchellh/copystructure)
Provides:       bundled(golang(github.com/opencontainers/go-digest)
Provides:       bundled(golang(github.com/opencontainers/image-spec/specs-go)
Provides:       bundled(golang(github.com/opencontainers/image-spec/specs-go/v1)
Provides:       bundled(golang(github.com/phayes/freeport)
Provides:       bundled(golang(github.com/pkg/errors)
Provides:       bundled(golang(github.com/rubenv/sql-migrate)
Provides:       bundled(golang(github.com/sirupsen/logrus)
Provides:       bundled(golang(github.com/spf13/cobra)
Provides:       bundled(golang(github.com/spf13/cobra/doc)
Provides:       bundled(golang(github.com/spf13/pflag)
Provides:       bundled(golang(github.com/xeipuuv/gojsonschema)
Provides:       bundled(golang(golang.org/x/crypto/bcrypt)
Provides:       bundled(golang(golang.org/x/crypto/openpgp)
Provides:       bundled(golang(golang.org/x/crypto/openpgp/clearsign)
Provides:       bundled(golang(golang.org/x/crypto/openpgp/packet)
Provides:       bundled(golang(golang.org/x/term)
Provides:       bundled(golang(k8s.io/api/apps/v1)
Provides:       bundled(golang(k8s.io/api/apps/v1beta1)
Provides:       bundled(golang(k8s.io/api/apps/v1beta2)
Provides:       bundled(golang(k8s.io/api/batch/v1)
Provides:       bundled(golang(k8s.io/api/core/v1)
Provides:       bundled(golang(k8s.io/api/extensions/v1beta1)
Provides:       bundled(golang(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1)
Provides:       bundled(golang(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/api/equality)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/api/errors)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/api/meta)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/api/validation)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/api/validation/path)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/fields)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/labels)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/runtime)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/runtime/schema)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/types)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/util/intstr)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/util/strategicpatch)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/util/validation)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/util/validation/field)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/util/wait)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/util/yaml)
Provides:       bundled(golang(k8s.io/apimachinery/pkg/watch)
Provides:       bundled(golang(k8s.io/apiserver/pkg/endpoints/deprecation)
Provides:       bundled(golang(k8s.io/cli-runtime/pkg/genericclioptions)
Provides:       bundled(golang(k8s.io/cli-runtime/pkg/printers)
Provides:       bundled(golang(k8s.io/cli-runtime/pkg/resource)
Provides:       bundled(golang(k8s.io/client-go/discovery)
Provides:       bundled(golang(k8s.io/client-go/dynamic)
Provides:       bundled(golang(k8s.io/client-go/kubernetes)
Provides:       bundled(golang(k8s.io/client-go/kubernetes/scheme)
Provides:       bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1)
Provides:       bundled(golang(k8s.io/client-go/kubernetes/typed/core/v1)
Provides:       bundled(golang(k8s.io/client-go/plugin/pkg/client/auth)
Provides:       bundled(golang(k8s.io/client-go/rest)
Provides:       bundled(golang(k8s.io/client-go/tools/cache)
Provides:       bundled(golang(k8s.io/client-go/tools/clientcmd)
Provides:       bundled(golang(k8s.io/client-go/tools/watch)
Provides:       bundled(golang(k8s.io/client-go/util/homedir)
Provides:       bundled(golang(k8s.io/klog/v2)
Provides:       bundled(golang(k8s.io/kubectl/pkg/cmd/util)
Provides:       bundled(golang(k8s.io/kubectl/pkg/validation)
Provides:       bundled(golang(sigs.k8s.io/yaml)

%description

%global debug_package %{nil}

%prep
%autosetup -n linux-%{basearch}

%build

%install
%__install -Dm755 helm  %{?buildroot}%{_bindir}/helm

%files
%license LICENSE
%doc README.md
%{_bindir}/helm
