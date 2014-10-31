# Maintainer: Sébastien Luttringer

pkgname=aurbot-git
pkgver=$(git log -1 --pretty=format:%h)
pkgrel=$(date +%s)
pkgdesc='AUR Builder Bot'
arch=('any')
url='https://github.com/seblu/aurbot'
license=('GPL2')
makedepends=('python-distribute')
depends=('python')
optdepends=('devtools')

package() {
  cd "$startdir"
  python setup.py install --root "$pkgdir"
  # ensure rights are corrects
  chmod -R go+rX "$pkgdir/usr"
}

# vim:set ts=2 sw=2 ft=sh et:
