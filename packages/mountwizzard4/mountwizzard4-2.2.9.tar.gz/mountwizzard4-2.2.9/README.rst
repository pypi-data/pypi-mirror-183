MountWizzard4
=============

Welcome to MountWizzard4 is a utility for 10micron users for improving the
workflow for astronomy work and imaging runs on Windows (10 and 11), OSx (Mojave
- Monterey), Linux (Ubuntu 18.04 and 20.04) and some Linux ARMV7 distributions
(Astroberry and StellarMate). As a python application, it should run in all
environments supporting python 3.7-3.9 and PyQt5 5.15.4 as a GUI framework.

Please check these pages for some hints to your installation:
https://mountwizzard4.readthedocs.io/en/latest/overview.html

For being fully operational, MW4 needs either:

-   INDI server(s) (see: https://indilib.org) where your devices are connected to.

-   INDIGO server(s) (see: http://www.indigo-astronomy.org) where your devices
    are connected to.

-   ASCOM Alpaca remote server (see: https://ascom-standards.org/FAQs/Index.htm)
    abstracting your ASCOM devices or devices which speak native ASCOM Alpaca if
    you want to connect over IP with your environment.

-   Running versions of Sequence Generator Pro or N.I.N.A. as frontend for camera
    device.

-   For the core devices there is native ASCOM support (Windows platform only).
    Please be reminded, that ASCOM has 32bit and 64bit driver implementations
    and MW4 could also be installed in 32bit or 64 bit python environment. They
    could be not be mixed! 32bit python supports only 32bit drivers and vice versa
    . Normally this should not be an issue...

-   In addition an internet connection is used for some services which might be
    very helpful.

It is recommended to use mount firmware 2.16 (ideally 2.16.11) or later as some
of the functions don't work with older firmware versions. It should not be a
problem using older versions. A HW pre2012 might also have some issues.

Versions, downloads and docs:
-----------------------------
|PYPI_VERSION| |PY_VERSIONS| |DownLoadsAbs| |DownLoadsMonth| |DOCS|

Code quality:
-------------
|CODE_QUALITY_PYTHON| |CODE_QUALITY_ALERTS| |CODECOV| |OPEN_ISSUES|

Unit tests:
^^^^^^^^^^^
|PYTEST macOS| |PYTEST Windows| |PYTEST Ubuntu|

Test install / run scripts:
^^^^^^^^^^^^^^^^^^^^^^^^^^^
|TEST_PACKAGES| |TEST_SCRIPTS| |RPI4_Mate18| |RPI4_Mate20|

Test coverage:
^^^^^^^^^^^^^^
|CODECOV_CHART|

Commit status:
^^^^^^^^^^^^^^
|COMMITS_WEEK| |COMMITS_MASTER|


Documentation:
--------------
There is an online documentation available for MW4 which could be searched for
entries:

Web based:
https://mountwizzard4.readthedocs.io/en/latest/

PDF format:
https://mountwizzard4.readthedocs.io/_/downloads/en/latest/pdf/

Installing procedures:
https://mountwizzard4.readthedocs.io/en/latest/install/index.html

Changelog:
https://mountwizzard4.readthedocs.io/en/latest/changelog.html

And there are some videos available for explanation in Youtube channel:
https://www.youtube.com/channel/UCJD-5qdLEcBTCugltqw1hXA/

Feedback discussions and issue reports:
---------------------------------------
Please report your issues: https://github.com/mworion/MountWizzard4/issues.
Please have a good description (maybe a screenshot if it‘s related to GUI) and
add the log file(s) to the issue. Any feedback welcome!

Please feel free to start any discussion:
https://github.com/mworion/MountWizzard4/discussions


Finally:
--------
MountWizzard4 is 'always' in development. The use this software is at your own
risk! No responsibility for damages to your mount or other equipment or your
environment, please take care yourself!

Hope this tool makes fun and helps for your hobby,

CS Michel

.. |PY_VERSIONS| image::
    https://img.shields.io/pypi/pyversions/mountwizzard4.svg

.. |DOCS| image::
    https://readthedocs.org/projects/mountwizzard4/badge/?version=stable
    :target: https://mountwizzard4.readthedocs.io/en/stable/?badge=stable
    :alt: Documentation Status

.. |PYTEST macOS| image::
    https://github.com/mworion/MountWizzard4/workflows/unit_macOS/badge.svg?branch=master

.. |PYTEST Windows| image::
    https://github.com/mworion/MountWizzard4/workflows/win_unit/badge.svg?branch=master

.. |PYTEST Ubuntu| image::
    https://github.com/mworion/MountWizzard4/workflows/unit_ubuntu/badge.svg?branch=master

.. |CODECOV| image::
    https://codecov.io/gh/mworion/MountWizzard4/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/mworion/MountWizzard4

.. |CODECOV_CHART| image::
    https://codecov.io/gh/mworion/MountWizzard4/branch/master/graphs/icicle.svg
    :target: https://codecov.io/gh/mworion/MountWizzard4
    :width: 80%
    :align: top

.. |CODE_QUALITY_ALERTS| image::
    https://img.shields.io/lgtm/alerts/g/mworion/MountWizzard4.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/mworion/MountWizzard4/latest/files/?sort=name&dir=ASC&mode=heatmap&showExcluded=false

.. |CODE_QUALITY_PYTHON| image::
    https://img.shields.io/lgtm/grade/python/g/mworion/MountWizzard4.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/mworion/MountWizzard4/?mode=list

.. |OPEN_ISSUES| image::
    https://img.shields.io/github/issues-raw/mworion/mountwizzard4
    :target: https://github.com/mworion/MountWizzard4/issues

.. |COMMITS_MASTER| image::
    https://img.shields.io/github/commits-since/mworion/mountwizzard4/2.1.0
    :target: https://github.com/mworion/MountWizzard4/commits/master

.. |COMMITS_WEEK| image::
    https://img.shields.io/github/commit-activity/w/mworion/mountwizzard4

.. |TEST_PACKAGES| image::
    https://github.com/mworion/MountWizzard4/workflows/test_packages/badge.svg?branch=master

.. |TEST_SCRIPTS| image::
    https://github.com/mworion/MountWizzard4/workflows/test_scripts/badge.svg?branch=master

.. |RPI4_Mate18| image::
    https://github.com/mworion/MountWizzard4/workflows/rpi4_mate18/badge.svg?branch=master

.. |RPI4_Mate20| image::
    https://github.com/mworion/MountWizzard4/workflows/rpi4_mate20/badge.svg?branch=master

.. |PYPI_VERSION| image::
    https://img.shields.io/pypi/v/mountwizzard4.svg
    :target: https://pypi.python.org/pypi/mountwizzard4
    :alt: MountWizzard4's PyPI Status
    
.. |DownLoadsAbs| image::
    https://pepy.tech/badge/mountwizzard4
    :target: https://pepy.tech/project/mountwizzard4

.. |DownLoadsMonth| image::
    https://pepy.tech/badge/mountwizzard4/month
    :target: https://pepy.tech/project/mountwizzard4

