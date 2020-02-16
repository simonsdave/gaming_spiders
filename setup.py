#
# to build the distrubution @ dist/gaming_spiders-*.*.*.tar.gz
#
#   >git clone https://github.com/simonsdave/gaming_spiders.git
#   >cd gaming_spiders
#   >python setup.py bdist_wheel sdist --formats=gztar sdist --formats=gztar
#

import re

from setuptools import setup

#
# this approach used below to determine ```version``` was inspired by
# https://github.com/kennethreitz/requests/blob/master/setup.py#L31
#
# why this complexity? wanted version number to be available in the
# a runtime.
#
# the code below assumes the distribution is being built with the
# current directory being the directory in which setup.py is stored
# which should be totally fine 99.9% of the time. not going to add
# the coode complexity to deal with other scenarios
#
reg_ex_pattern = r'__version__\s*=\s*[\'"](?P<version>[^\'"]*)[\'"]'
reg_ex = re.compile(reg_ex_pattern)
version = ''
with open('gaming_spiders/__init__.py', 'r') as fd:
    for line in fd:
        match = reg_ex.match(line)
        if match:
            version = match.group('version')
            break
if not version:
    raise Exception("Can't locate project's version number")

setup(
    name='gaming_spiders',
    packages=[
        'gaming_spiders',
    ],
    scripts=[
        'gaming_spiders/bigfishonlinegames.py',
        'gaming_spiders/gamehouseonlinegames.py',
        'gaming_spiders/hiddenobjectgames.py',
        'gaming_spiders/match3games.py',
        'gaming_spiders/miniclip.py',
        'gaming_spiders/solitaireonline.py',
        'gaming_spiders/gamesonly.py',
        'gaming_spiders/mahjonggames.py',
        'gaming_spiders/mindgames.py',
        'gaming_spiders/msnonlinegames.py',
    ],
    install_requires=[
        'cloudfeaster==0.9.34',
    ],
    version=version,
    description='Gaming Spiders',
    author='Dave Simons',
    author_email='simonsdave@gmail.com',
    url='https://github.com/simonsdave/gaming_spiders'
)
