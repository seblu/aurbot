# Maintainer: Sébastien Luttringer

pkgname=aurbot-git
pkgver=1
pkgrel=1
pkgdesc='AUR Builder Bot'
arch=('any')
url='https://git.seblu.net/archlinux/aurbot/'
license=('GPL2')
backup=('etc/aurbot.conf')
makedepends=('git' 'python-distribute')
depends=('systemd' 'python' 'python-systemd')
optdepends=('devtools')

pkgver() {
  cd "$startdir"
  printf '%s.%(%Y%m%d%H%M)T' "$(git rev-list --count HEAD)"
}

package() {
  cd "$startdir"
  install -Dm755 aurbot "$pkgdir/usr/bin/aurbot"
  install -Dm644 /dev/null "$pkgdir/etc/aurbot.conf"

  install -dm755 "$pkgdir/usr/share/doc/aurbot/samples"
  install -m644 aurbot.conf.example{1,2,3} "$pkgdir/usr/share/doc/aurbot/samples"

  install -Dm644 aurbot.service "$pkgdir/usr/lib/systemd/system/aurbot.service"
  install -Dm644 aurbot.sysusers "$pkgdir/usr/lib/sysusers.d/aurbot.conf"
  install -Dm644 aurbot.tmpfiles "$pkgdir/usr/lib/tmpfiles.d/aurbot.conf"
}

# vim:set ts=2 sw=2 et:
