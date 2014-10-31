from setuptools import setup
import os

ldesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='aurbot',
    version=0,
    description='AUR builder bot',
    long_description=ldesc,
    author='Sébastien Luttringer',
    license='GPL2',
    scripts=['aurbot'],
    data_files=(
		('/usr/share/aurbot/', ('README.rst', 'COPYING', 'CHANGELOG')),
		('/usr/share/doc/aurbot/samples/', ('packages.conf',))
    ),
    classifiers=[
        'Operating System :: Unix',
        'Programming Language :: Python',
        ],
    )
