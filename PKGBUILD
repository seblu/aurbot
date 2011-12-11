# Maintainer: Sebastien Luttringer <seblu@aur.archlinux.org>

pkgname=aurbot
pkgver=1_git_$(git log -1 --pretty=format:%h)
pkgrel=1
pkgdesc='Automatic Arch User Repository builder'
url='https://github.com/seblu/aurbot'
license=('GPL2')
arch=('any')

package() {
  # install binary
  install -D -m 755 "$startdir/aurbot" "$pkgdir/usr/bin/aurbot"

  # install config
  install -D -m 644 "$startdir/repositories.conf" "$pkgdir/etc/aurbot/repository.conf"
}

# vim:set ts=2 sw=2 ft=sh et:
