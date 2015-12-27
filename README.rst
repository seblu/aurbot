======
AURBOT
======

INTRODUCTION
============

*Aurbot* is a AUR [#]_ (Arch Linux Repository) automatic builder of packages.
Its goal is to track updates of AUR packages to build new versions, send mail
report and push the new package inside a binary repository.


*Aurbot* is piloted by its command line tools *aurbot* and timed action, like
rebuild or mail report should be done via cron.

*Aurbot* is written in Python 3.2.


DEPENDENCIES
============
- Python 3.2 [#]_
- pyalpm [#]_
- python-aur [#]_


SECURITY
========
You must take in consideration that *Aurbot* build, so execute, code (PKGBUILD)
from a remote location (AUR), pushed by users from Internet.

Package are built in a clean chroot environment, but this is not an true
security feature as explain in `man (2) chroot`.

So you should automatically build package from user you trust. At least a
little.

To avoid kind of issue *Aurbot* doesn't automatically build new package version
if owner of package if orphan or have changed from the previous build.


QUICK SETUP
===========
1. Install aurbot package
2. Create your repositories configuration
3. Init your repositories
4. Run aurbot


ENVIRONMENT
===========
*AURBOT_CONFIG* overrides the config file path (default is /etc/aurbot.conf)

*AURBOT_DATADIR* overrides the data directory path (default is /var/lib/aurbot)


SOURCES
=======
*Aurbot* sources are available on github [#]_.


LICENSE
=======
*Aubot* is licensied under the term of GPL v2 [#]_.


AUTHOR
======
*Aurbot* is developped by Sébastien Luttringer.


LINKS
=====
.. [#] https://aur.archlinux.org/
.. [#] http://python.org/download/releases/
.. [#] http://projects.archlinux.org/users/remy/pyalpm.git/
.. [#] http://xyne.archlinux.ca/projects/python3-aur/
.. [#] https://github.com/seblu/aurbot/
.. [#] http://www.gnu.org/licenses/gpl-2.0.html
