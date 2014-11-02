# Maintainer: Sébastien Luttringer

pkgname=aurbot-git
#pkgver=$(git log -1 --pretty=format:%h)
pkgver=$(date +%y%j%H%M)
pkgrel=1
pkgdesc='AUR Builder Bot'
arch=('any')
url='https://github.com/seblu/aurbot'
license=('GPL2')
makedepends=('python-distribute')
depends=('python' 'systemd')
optdepends=('devtools')
install=aurbot.install

package() {
  cd "$startdir"
  install -Dm755 aurbot "$pkgdir/usr/bin/aurbot"
  install -Dm644 aurbot.service "$pkgdir/usr/lib/systemd/system/aurbot.service"
  install -Dm644 aurbot.sysusers "$pkgdir/usr/lib/sysusers.d/aurbot.conf"
  install -Dm644 packages.conf "$pkgdir/usr/share/doc/aurbot/samples/packages.conf"
  install -dm750 "$pkgdir/var/lib/aurbot"
}

# vim:set ts=2 sw=2 et:
