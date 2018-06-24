# https://github.com/go-gitea/gitea
%global provider_prefix github.com/go-gitea/gitea
%global goipath         %{provider_prefix}
%global tag             v1.4.2
%global commit          df941f5c392d327a1eaa8e0870c4b54c91066fe1

%gometa -i

Name:           %{goname}
Version:        1.4.2
Release:        1%{?dist}
Summary:        Git with a cup of tea
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

# main.go
BuildRequires: golang(github.com/urfave/cli)

# Remaining dependencies not included in main packages
Provides: bundled(golang(github.com/go-macaron/cache/redis))
Provides: bundled(golang(github.com/kballard/go-shellquote))
Provides: bundled(golang(github.com/keybase/go-crypto/openpgp/packet))
Provides: bundled(golang(github.com/go-xorm/core))
Provides: bundled(golang(github.com/go-macaron/captcha))
Provides: bundled(golang(github.com/facebookgo/grace/gracehttp))
Provides: bundled(golang(github.com/markbates/goth/providers/gplus))
Provides: bundled(golang(github.com/PuerkitoBio/goquery))
Provides: bundled(golang(github.com/denisenkom/go-mssqldb))
Provides: bundled(golang(github.com/issue9/identicon))
Provides: bundled(golang(github.com/blevesearch/bleve/analysis/tokenizer/unicode))
Provides: bundled(golang(github.com/pquerna/otp/totp))
Provides: bundled(golang(github.com/go-macaron/cache))
Provides: bundled(golang(github.com/Unknwon/com))
Provides: bundled(golang(github.com/blevesearch/bleve/analysis/token/lowercase))
Provides: bundled(golang(github.com/Unknwon/i18n))
Provides: bundled(golang(github.com/go-macaron/session/redis))
Provides: bundled(golang(github.com/go-macaron/toolbox))
Provides: bundled(golang(github.com/gogits/chardet))
Provides: bundled(golang(github.com/stretchr/testify/assert))
Provides: bundled(golang(github.com/russross/blackfriday))
Provides: bundled(golang(github.com/markbates/goth/gothic))
Provides: bundled(golang(golang.org/x/text/transform))
Provides: bundled(golang(github.com/go-macaron/cache/memcache))
Provides: bundled(golang(github.com/go-macaron/session))
Provides: bundled(golang(github.com/keybase/go-crypto/openpgp/armor))
Provides: bundled(golang(golang.org/x/net/html/charset))
Provides: bundled(golang(github.com/go-macaron/binding))
Provides: bundled(golang(github.com/gogits/cron))
Provides: bundled(golang(github.com/go-macaron/gzip))
Provides: bundled(golang(github.com/yohcop/openid-go))
Provides: bundled(golang(gopkg.in/testfixtures.v2))
Provides: bundled(golang(github.com/go-macaron/bindata))
Provides: bundled(golang(github.com/pingcap/tidb))
Provides: bundled(golang(golang.org/x/crypto/ssh))
Provides: bundled(golang(github.com/go-xorm/xorm))
Provides: bundled(golang(github.com/dgrijalva/jwt-go))
Provides: bundled(golang(github.com/go-macaron/csrf))
Provides: bundled(golang(github.com/blevesearch/bleve/analysis/token/camelcase))
Provides: bundled(golang(github.com/markbates/goth/providers/github))
Provides: bundled(golang(golang.org/x/sys/windows/svc))
Provides: bundled(golang(gopkg.in/ldap.v2))
Provides: bundled(golang(golang.org/x/sync/syncmap))
Provides: bundled(golang(github.com/lib/pq))
Provides: bundled(golang(github.com/mattn/go-sqlite3))
Provides: bundled(golang(github.com/blevesearch/bleve/analysis/token/unicodenorm))
Provides: bundled(golang(github.com/gorilla/context))
Provides: bundled(golang(github.com/nfnt/resize))
Provides: bundled(golang(github.com/markbates/goth/providers/facebook))
Provides: bundled(golang(github.com/go-xorm/tidb))
Provides: bundled(golang(gopkg.in/gomail.v2))
Provides: bundled(golang(github.com/jaytaylor/html2text))
Provides: bundled(golang(gopkg.in/ini.v1))
Provides: bundled(golang(github.com/go-xorm/builder))
Provides: bundled(golang(github.com/Unknwon/cae/zip))
Provides: bundled(golang(github.com/chaseadamsio/goorgeous))
Provides: bundled(golang(github.com/blevesearch/bleve/analysis/analyzer/custom))
Provides: bundled(golang(github.com/markbates/goth/providers/dropbox))
Provides: bundled(golang(github.com/go-sql-driver/mysql))
Provides: bundled(golang(github.com/msteinert/pam))
Provides: bundled(golang(github.com/keybase/go-crypto/openpgp))
Provides: bundled(golang(github.com/microcosm-cc/bluemonday))
Provides: bundled(golang(github.com/blevesearch/bleve/search/query))
Provides: bundled(golang(github.com/markbates/goth/providers/bitbucket))
Provides: bundled(golang(github.com/go-macaron/i18n))
Provides: bundled(golang(github.com/markbates/goth/providers/gitlab))
Provides: bundled(golang(github.com/blevesearch/bleve/mapping))
Provides: bundled(golang(github.com/markbates/goth/providers/openidConnect))
Provides: bundled(golang(github.com/pquerna/otp))
Provides: bundled(golang(github.com/markbates/goth/providers/twitter))
Provides: bundled(golang(github.com/ngaut/log))
Provides: bundled(golang(github.com/lunny/dingtalk_webhook))
Provides: bundled(golang(gopkg.in/macaron.v1))
Provides: bundled(golang(github.com/satori/go.uuid))
Provides: bundled(golang(github.com/gorilla/sessions))
Provides: bundled(golang(github.com/mcuadros/go-version))
Provides: bundled(golang(github.com/Unknwon/paginater))
Provides: bundled(golang(github.com/blevesearch/bleve/index/upsidedown))
Provides: bundled(golang(golang.org/x/net/html))
Provides: bundled(golang(golang.org/x/crypto/pbkdf2))
Provides: bundled(golang(github.com/markbates/goth))
Provides: bundled(golang(github.com/sergi/go-diff/diffmatchpatch))
Provides: bundled(golang(github.com/blevesearch/bleve))

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

Provides: bundled(golang(github.com/PuerkitoBio/goquery))
Provides: bundled(golang(github.com/Unknwon/cae/zip))
Provides: bundled(golang(github.com/Unknwon/com))
Provides: bundled(golang(github.com/Unknwon/i18n))
Provides: bundled(golang(github.com/Unknwon/paginater))
Provides: bundled(golang(github.com/blevesearch/bleve))
Provides: bundled(golang(github.com/blevesearch/bleve/analysis/analyzer/custom))
Provides: bundled(golang(github.com/blevesearch/bleve/analysis/token/camelcase))
Provides: bundled(golang(github.com/blevesearch/bleve/analysis/token/lowercase))
Provides: bundled(golang(github.com/blevesearch/bleve/analysis/token/unicodenorm))
Provides: bundled(golang(github.com/blevesearch/bleve/analysis/tokenizer/unicode))
Provides: bundled(golang(github.com/blevesearch/bleve/index/upsidedown))
Provides: bundled(golang(github.com/blevesearch/bleve/mapping))
Provides: bundled(golang(github.com/blevesearch/bleve/search/query))
Provides: bundled(golang(github.com/chaseadamsio/goorgeous))
Provides: bundled(golang(github.com/denisenkom/go-mssqldb))
Provides: bundled(golang(github.com/dgrijalva/jwt-go))
Provides: bundled(golang(github.com/facebookgo/grace/gracehttp))
Provides: bundled(golang(github.com/go-macaron/bindata))
Provides: bundled(golang(github.com/go-macaron/binding))
Provides: bundled(golang(github.com/go-macaron/cache))
Provides: bundled(golang(github.com/go-macaron/cache/memcache))
Provides: bundled(golang(github.com/go-macaron/cache/redis))
Provides: bundled(golang(github.com/go-macaron/captcha))
Provides: bundled(golang(github.com/go-macaron/csrf))
Provides: bundled(golang(github.com/go-macaron/gzip))
Provides: bundled(golang(github.com/go-macaron/i18n))
Provides: bundled(golang(github.com/go-macaron/session))
Provides: bundled(golang(github.com/go-macaron/session/redis))
Provides: bundled(golang(github.com/go-macaron/toolbox))
Provides: bundled(golang(github.com/go-sql-driver/mysql))
Provides: bundled(golang(github.com/go-xorm/builder))
Provides: bundled(golang(github.com/go-xorm/core))
Provides: bundled(golang(github.com/go-xorm/tidb))
Provides: bundled(golang(github.com/go-xorm/xorm))
Provides: bundled(golang(github.com/gogits/chardet))
Provides: bundled(golang(github.com/gogits/cron))
Provides: bundled(golang(github.com/gorilla/context))
Provides: bundled(golang(github.com/gorilla/sessions))
Provides: bundled(golang(github.com/issue9/identicon))
Provides: bundled(golang(github.com/jaytaylor/html2text))
Provides: bundled(golang(github.com/kballard/go-shellquote))
Provides: bundled(golang(github.com/keybase/go-crypto/openpgp))
Provides: bundled(golang(github.com/keybase/go-crypto/openpgp/armor))
Provides: bundled(golang(github.com/keybase/go-crypto/openpgp/packet))
Provides: bundled(golang(github.com/lib/pq))
Provides: bundled(golang(github.com/lunny/dingtalk_webhook))
Provides: bundled(golang(github.com/markbates/goth))
Provides: bundled(golang(github.com/markbates/goth/gothic))
Provides: bundled(golang(github.com/markbates/goth/providers/bitbucket))
Provides: bundled(golang(github.com/markbates/goth/providers/dropbox))
Provides: bundled(golang(github.com/markbates/goth/providers/facebook))
Provides: bundled(golang(github.com/markbates/goth/providers/github))
Provides: bundled(golang(github.com/markbates/goth/providers/gitlab))
Provides: bundled(golang(github.com/markbates/goth/providers/gplus))
Provides: bundled(golang(github.com/markbates/goth/providers/openidConnect))
Provides: bundled(golang(github.com/markbates/goth/providers/twitter))
Provides: bundled(golang(github.com/mattn/go-sqlite3))
Provides: bundled(golang(github.com/mcuadros/go-version))
Provides: bundled(golang(github.com/microcosm-cc/bluemonday))
Provides: bundled(golang(github.com/msteinert/pam))
Provides: bundled(golang(github.com/nfnt/resize))
Provides: bundled(golang(github.com/ngaut/log))
Provides: bundled(golang(github.com/pingcap/tidb))
Provides: bundled(golang(github.com/pquerna/otp))
Provides: bundled(golang(github.com/pquerna/otp/totp))
Provides: bundled(golang(github.com/russross/blackfriday))
Provides: bundled(golang(github.com/satori/go.uuid))
Provides: bundled(golang(github.com/sergi/go-diff/diffmatchpatch))
Provides: bundled(golang(github.com/stretchr/testify/assert))
Provides: bundled(golang(github.com/urfave/cli))
Provides: bundled(golang(github.com/yohcop/openid-go))
Provides: bundled(golang(golang.org/x/crypto/pbkdf2))
Provides: bundled(golang(golang.org/x/crypto/ssh))
Provides: bundled(golang(golang.org/x/net/html))
Provides: bundled(golang(golang.org/x/net/html/charset))
Provides: bundled(golang(golang.org/x/sync/syncmap))
Provides: bundled(golang(golang.org/x/sys/windows/svc))
Provides: bundled(golang(golang.org/x/text/transform))
Provides: bundled(golang(gopkg.in/gomail.v2))
Provides: bundled(golang(gopkg.in/ini.v1))
Provides: bundled(golang(gopkg.in/ldap.v2))
Provides: bundled(golang(gopkg.in/macaron.v1))
Provides: bundled(golang(gopkg.in/testfixtures.v2))

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q


%build
%gobuildroot

#%gobuild -o _bin/ %{import_path}/
#%gobuild -o _bin/scripts %{import_path}/scripts


%install
install -d -p %{buildroot}%{_bindir}
#install -p -m 0755 _bin/ %{buildroot}%{_bindir}
#install -p -m 0755 _bin/scripts %{buildroot}%{_bindir}

%goinstall

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc CONTRIBUTING.md CHANGELOG.md README.md README_ZH.md
#%{_bindir}/
#%{_bindir}/scripts

%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTING.md CHANGELOG.md README.md README_ZH.md
%changelog
* Tue Jun 05 2018 root - Forge-specific packaging variables
- First package for Fedora

