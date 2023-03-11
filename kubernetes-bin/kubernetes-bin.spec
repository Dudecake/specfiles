%define basearch %_arch
%if "%{basearch}" == "x86_64"
%define basearch amd64
%endif
%if "%{basearch}" == "aarch64"
%define basearch arm64
%endif

Name:           kubernetes-bin
Version:        1.25.7
Release:        1%{?dist}
Summary:        Production-Grade Container Scheduling and Management
URL:            https://github.com/kubernetes/kubernetes
License:        Apache-2.0
BuildRequires:  systemd-rpm-macros

Source0:        https://storage.googleapis.com/kubernetes-release/release/v%{version}/kubernetes-server-linux-%{basearch}.tar.gz
Source1:        kubelet.service

Provides:       kubernetes = %{version}
Provides:       bundled(golang(bitbucket.org/bertimus9/systemstat))
Provides:       bundled(golang(cloud.google.com/go))
Provides:       bundled(golang(github.com/armon/circbuf))
Provides:       bundled(golang(github.com/asaskevich/govalidator))
Provides:       bundled(golang(github.com/aws/aws-sdk-go))
Provides:       bundled(golang(github.com/Azure/azure-sdk-for-go))
Provides:       bundled(golang(github.com/Azure/go-ansiterm))
Provides:       bundled(golang(github.com/Azure/go-autorest/autorest/adal))
Provides:       bundled(golang(github.com/Azure/go-autorest/autorest/date))
Provides:       bundled(golang(github.com/Azure/go-autorest/autorest))
Provides:       bundled(golang(github.com/Azure/go-autorest/autorest/mocks))
Provides:       bundled(golang(github.com/Azure/go-autorest/autorest/to))
Provides:       bundled(golang(github.com/Azure/go-autorest/autorest/validation))
Provides:       bundled(golang(github.com/Azure/go-autorest))
Provides:       bundled(golang(github.com/Azure/go-autorest/logger))
Provides:       bundled(golang(github.com/Azure/go-autorest/tracing))
Provides:       bundled(golang(github.com/beorn7/perks))
Provides:       bundled(golang(github.com/bits-and-blooms/bitset))
Provides:       bundled(golang(github.com/blang/semver))
Provides:       bundled(golang(github.com/cespare/xxhash/v2))
Provides:       bundled(golang(github.com/chai2010/gettext-go))
Provides:       bundled(golang(github.com/checkpoint-restore/go-criu/v5))
Provides:       bundled(golang(github.com/cilium/ebpf))
Provides:       bundled(golang(github.com/clusterhq/flocker-go))
Provides:       bundled(golang(github.com/containerd/cgroups))
Provides:       bundled(golang(github.com/containerd/console))
Provides:       bundled(golang(github.com/containerd/containerd))
Provides:       bundled(golang(github.com/containerd/ttrpc))
Provides:       bundled(golang(github.com/containernetworking/cni))
Provides:       bundled(golang(github.com/container-storage-interface/spec))
Provides:       bundled(golang(github.com/coredns/caddy))
Provides:       bundled(golang(github.com/coredns/corefile-migration))
Provides:       bundled(golang(github.com/coreos/go-oidc))
Provides:       bundled(golang(github.com/coreos/go-semver))
Provides:       bundled(golang(github.com/coreos/go-systemd))
Provides:       bundled(golang(github.com/coreos/go-systemd/v22))
Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2))
Provides:       bundled(golang(github.com/cyphar/filepath-securejoin))
Provides:       bundled(golang(github.com/davecgh/go-spew))
Provides:       bundled(golang(github.com/daviddengcn/go-colortext))
Provides:       bundled(golang(github.com/docker/distribution))
Provides:       bundled(golang(github.com/docker/docker))
Provides:       bundled(golang(github.com/docker/go-connections))
Provides:       bundled(golang(github.com/docker/go-units))
Provides:       bundled(golang(github.com/dustin/go-humanize))
Provides:       bundled(golang(github.com/elazarl/goproxy))
Provides:       bundled(golang(github.com/emicklei/go-restful))
Provides:       bundled(golang(github.com/euank/go-kmsg-parser))
Provides:       bundled(golang(github.com/evanphx/json-patch))
Provides:       bundled(golang(github.com/exponent-io/jsonpath))
Provides:       bundled(golang(github.com/fatih/camelcase))
Provides:       bundled(golang(github.com/felixge/httpsnoop))
Provides:       bundled(golang(github.com/form3tech-oss/jwt-go))
Provides:       bundled(golang(github.com/fsnotify/fsnotify))
Provides:       bundled(golang(github.com/fvbommel/sortorder))
Provides:       bundled(golang(github.com/godbus/dbus/v5))
Provides:       bundled(golang(github.com/go-errors/errors))
Provides:       bundled(golang(github.com/gofrs/uuid))
Provides:       bundled(golang(github.com/gogo/protobuf))
Provides:       bundled(golang(github.com/golang/groupcache))
Provides:       bundled(golang(github.com/golang/mock))
Provides:       bundled(golang(github.com/golang/protobuf))
Provides:       bundled(golang(github.com/go-logr/logr))
Provides:       bundled(golang(github.com/googleapis/gax-go/v2))
Provides:       bundled(golang(github.com/googleapis/gnostic))
Provides:       bundled(golang(github.com/google/btree))
Provides:       bundled(golang(github.com/google/cadvisor))
Provides:       bundled(golang(github.com/GoogleCloudPlatform/k8s-cloud-provider))
Provides:       bundled(golang(github.com/google/go-cmp))
Provides:       bundled(golang(github.com/google/gofuzz))
Provides:       bundled(golang(github.com/google/shlex))
Provides:       bundled(golang(github.com/google/uuid))
Provides:       bundled(golang(github.com/go-openapi/jsonpointer))
Provides:       bundled(golang(github.com/go-openapi/jsonreference))
Provides:       bundled(golang(github.com/go-openapi/swag))
Provides:       bundled(golang(github.com/go-ozzo/ozzo-validation))
Provides:       bundled(golang(github.com/gophercloud/gophercloud))
Provides:       bundled(golang(github.com/gorilla/websocket))
Provides:       bundled(golang(github.com/gregjones/httpcache))
Provides:       bundled(golang(github.com/grpc-ecosystem/go-grpc-middleware))
Provides:       bundled(golang(github.com/grpc-ecosystem/go-grpc-prometheus))
Provides:       bundled(golang(github.com/grpc-ecosystem/grpc-gateway))
Provides:       bundled(golang(github.com/heketi/heketi))
Provides:       bundled(golang(github.com/imdario/mergo))
Provides:       bundled(golang(github.com/inconshreveable/mousetrap))
Provides:       bundled(golang(github.com/ishidawataru/sctp))
Provides:       bundled(golang(github.com/JeffAshton/win_pdh))
Provides:       bundled(golang(github.com/jmespath/go-jmespath))
Provides:       bundled(golang(github.com/jonboulle/clockwork))
Provides:       bundled(golang(github.com/josharian/intern))
Provides:       bundled(golang(github.com/json-iterator/go))
Provides:       bundled(golang(github.com/karrick/godirwalk))
Provides:       bundled(golang(github.com/libopenstorage/openstorage))
Provides:       bundled(golang(github.com/liggitt/tabwriter))
Provides:       bundled(golang(github.com/lithammer/dedent))
Provides:       bundled(golang(github.com/mailru/easyjson))
Provides:       bundled(golang(github.com/MakeNowJust/heredoc))
Provides:       bundled(golang(github.com/matttproud/golang_protobuf_extensions))
Provides:       bundled(golang(github.com/Microsoft/go-winio))
Provides:       bundled(golang(github.com/Microsoft/hcsshim))
Provides:       bundled(golang(github.com/mindprince/gonvml))
Provides:       bundled(golang(github.com/mistifyio/go-zfs))
Provides:       bundled(golang(github.com/mitchellh/go-wordwrap))
Provides:       bundled(golang(github.com/mitchellh/mapstructure))
Provides:       bundled(golang(github.com/moby/ipvs))
Provides:       bundled(golang(github.com/moby/spdystream))
Provides:       bundled(golang(github.com/moby/sys/mountinfo))
Provides:       bundled(golang(github.com/moby/term))
Provides:       bundled(golang(github.com/modern-go/concurrent))
Provides:       bundled(golang(github.com/modern-go/reflect2))
Provides:       bundled(golang(github.com/mohae/deepcopy))
Provides:       bundled(golang(github.com/monochromegane/go-gitignore))
Provides:       bundled(golang(github.com/morikuni/aec))
Provides:       bundled(golang(github.com/mrunalp/fileutils))
Provides:       bundled(golang(github.com/munnerz/goautoneg))
Provides:       bundled(golang(github.com/mvdan/xurls))
Provides:       bundled(golang(github.com/mxk/go-flowrate))
Provides:       bundled(golang(github.com/nxadm/tail))
Provides:       bundled(golang(github.com/NYTimes/gziphandler))
Provides:       bundled(golang(github.com/onsi/ginkgo))
Provides:       bundled(golang(github.com/onsi/gomega))
Provides:       bundled(golang(github.com/opencontainers/go-digest))
Provides:       bundled(golang(github.com/opencontainers/image-spec))
Provides:       bundled(golang(github.com/opencontainers/runc))
Provides:       bundled(golang(github.com/opencontainers/runtime-spec))
Provides:       bundled(golang(github.com/opencontainers/selinux))
Provides:       bundled(golang(github.com/peterbourgon/diskv))
Provides:       bundled(golang(github.com/pkg/errors))
Provides:       bundled(golang(github.com/pmezard/go-difflib))
Provides:       bundled(golang(github.com/pquerna/cachecontrol))
Provides:       bundled(golang(github.com/prometheus/client_golang))
Provides:       bundled(golang(github.com/prometheus/client_model))
Provides:       bundled(golang(github.com/prometheus/common))
Provides:       bundled(golang(github.com/prometheus/procfs))
Provides:       bundled(golang(github.com/PuerkitoBio/purell))
Provides:       bundled(golang(github.com/PuerkitoBio/urlesc))
Provides:       bundled(golang(github.com/quobyte/api))
Provides:       bundled(golang(github.com/robfig/cron/v3))
Provides:       bundled(golang(github.com/rubiojr/go-vhd))
Provides:       bundled(golang(github.com/russross/blackfriday))
Provides:       bundled(golang(github.com/russross/blackfriday/v2))
Provides:       bundled(golang(github.com/seccomp/libseccomp-golang))
Provides:       bundled(golang(github.com/shurcooL/sanitized_anchor_name))
Provides:       bundled(golang(github.com/sirupsen/logrus))
Provides:       bundled(golang(github.com/soheilhy/cmux))
Provides:       bundled(golang(github.com/spf13/cobra))
Provides:       bundled(golang(github.com/spf13/pflag))
Provides:       bundled(golang(github.com/storageos/go-api))
Provides:       bundled(golang(github.com/stretchr/objx))
Provides:       bundled(golang(github.com/stretchr/testify))
Provides:       bundled(golang(github.com/syndtr/gocapability))
Provides:       bundled(golang(github.com/tmc/grpc-websocket-proxy))
Provides:       bundled(golang(github.com/vishvananda/netlink))
Provides:       bundled(golang(github.com/vishvananda/netns))
Provides:       bundled(golang(github.com/vmware/govmomi))
Provides:       bundled(golang(github.com/xiang90/probing))
Provides:       bundled(golang(github.com/xlab/treeprint))
Provides:       bundled(golang(go.etcd.io/bbolt))
Provides:       bundled(golang(go.etcd.io/etcd/api/v3))
Provides:       bundled(golang(go.etcd.io/etcd/client/pkg/v3))
Provides:       bundled(golang(go.etcd.io/etcd/client/v2))
Provides:       bundled(golang(go.etcd.io/etcd/client/v3))
Provides:       bundled(golang(go.etcd.io/etcd/pkg/v3))
Provides:       bundled(golang(go.etcd.io/etcd/raft/v3))
Provides:       bundled(golang(go.etcd.io/etcd/server/v3))
Provides:       bundled(golang(golang.org/x/crypto))
Provides:       bundled(golang(golang.org/x/mod))
Provides:       bundled(golang(golang.org/x/net))
Provides:       bundled(golang(golang.org/x/oauth2))
Provides:       bundled(golang(golang.org/x/sync))
Provides:       bundled(golang(golang.org/x/sys))
Provides:       bundled(golang(golang.org/x/term))
Provides:       bundled(golang(golang.org/x/text))
Provides:       bundled(golang(golang.org/x/time))
Provides:       bundled(golang(golang.org/x/tools))
Provides:       bundled(golang(golang.org/x/xerrors))
Provides:       bundled(golang(gonum.org/v1/gonum))
Provides:       bundled(golang(google.golang.org/api/internal/third_party/uritemplates))
Provides:       bundled(golang(google.golang.org/api))
Provides:       bundled(golang(google.golang.org/appengine))
Provides:       bundled(golang(google.golang.org/genproto))
Provides:       bundled(golang(google.golang.org/grpc))
Provides:       bundled(golang(google.golang.org/protobuf))
Provides:       bundled(golang(go.opencensus.io))
Provides:       bundled(golang(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc))
Provides:       bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp))
Provides:       bundled(golang(go.opentelemetry.io/contrib))
Provides:       bundled(golang(go.opentelemetry.io/otel/exporters/otlp))
Provides:       bundled(golang(go.opentelemetry.io/otel))
Provides:       bundled(golang(go.opentelemetry.io/otel/metric))
Provides:       bundled(golang(go.opentelemetry.io/otel/sdk/export/metric))
Provides:       bundled(golang(go.opentelemetry.io/otel/sdk))
Provides:       bundled(golang(go.opentelemetry.io/otel/sdk/metric))
Provides:       bundled(golang(go.opentelemetry.io/otel/trace))
Provides:       bundled(golang(go.opentelemetry.io/proto/otlp))
Provides:       bundled(golang(gopkg.in/gcfg.v1))
Provides:       bundled(golang(gopkg.in/inf.v0))
Provides:       bundled(golang(gopkg.in/natefinch/lumberjack.v2))
Provides:       bundled(golang(gopkg.in/square/go-jose.v2))
Provides:       bundled(golang(gopkg.in/tomb.v1))
Provides:       bundled(golang(gopkg.in/warnings.v0))
Provides:       bundled(golang(gopkg.in/yaml.v2))
Provides:       bundled(golang(gopkg.in/yaml.v3))
Provides:       bundled(golang(go.starlark.net))
Provides:       bundled(golang(go.uber.org/atomic))
Provides:       bundled(golang(go.uber.org/multierr))
Provides:       bundled(golang(go.uber.org/zap))
Provides:       bundled(golang(k8s.io/gengo))
Provides:       bundled(golang(k8s.io/klog/v2))
Provides:       bundled(golang(k8s.io/kube-openapi))
Provides:       bundled(golang(k8s.io/system-validators))
Provides:       bundled(golang(k8s.io/utils/internal/third_party/forked/golang))
Provides:       bundled(golang(k8s.io/utils))
Provides:       bundled(golang(sigs.k8s.io/apiserver-network-proxy/konnectivity-client))
Provides:       bundled(golang(sigs.k8s.io/kustomize/api))
Provides:       bundled(golang(sigs.k8s.io/kustomize/kustomize/v4))
Provides:       bundled(golang(sigs.k8s.io/kustomize/kyaml/internal/forked/github.com/go-yaml/yaml))
Provides:       bundled(golang(sigs.k8s.io/kustomize/kyaml/internal/forked/github.com/qri-io/starlib/util))
Provides:       bundled(golang(sigs.k8s.io/kustomize/kyaml))
Provides:       bundled(golang(sigs.k8s.io/structured-merge-diff/v4))
Provides:       bundled(golang(sigs.k8s.io/yaml))

%description

%global debug_package %{nil}

%prep
%autosetup -n kubernetes

%build

%install
%__mkdir -p %{?buildroot}%{_bindir}/
%__cp -a ./server/bin/.  %{?buildroot}%{_bindir}/
%__install -D %{SOURCE1} %{?buildroot}%{_unitdir}/kubelet.service

%files
%license LICENSES/LICENSE
%{_bindir}/kubectl
%{_bindir}/kubectl-convert
%{_bindir}/kube-scheduler.docker_tag
%{_bindir}/kube-scheduler
%{_bindir}/kube-proxy.tar
%{_bindir}/kube-controller-manager.docker_tag
%{_bindir}/apiextensions-apiserver
%{_bindir}/kube-apiserver.tar
%{_bindir}/kube-proxy.docker_tag
%{_bindir}/kube-proxy
%{_bindir}/kubelet
%{_bindir}/kube-log-runner
%{_bindir}/kube-aggregator
%{_bindir}/kube-apiserver.docker_tag
%{_bindir}/kube-controller-manager
%{_bindir}/kube-scheduler.tar
%{_bindir}/kube-controller-manager.tar
%{_bindir}/kube-apiserver
%{_bindir}/mounter
%{_bindir}/kubeadm
%{_unitdir}/kubelet.service
