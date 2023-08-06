==================================
 RsFsw
==================================

.. image:: https://img.shields.io/pypi/v/RsFsw.svg
   :target: https://pypi.org/project/ RsFsw/

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://RsFsw.readthedocs.io/

.. image:: https://img.shields.io/pypi/l/RsFsw.svg
   :target: https://pypi.python.org/pypi/RsFsw/

.. image:: https://img.shields.io/pypi/pyversions/pybadges.svg
   :target: https://img.shields.io/pypi/pyversions/pybadges.svg

.. image:: https://img.shields.io/pypi/dm/RsFsw.svg
   :target: https://pypi.python.org/pypi/RsFsw/

Rohde & Schwarz FSW Spectrum Analyzer RsFsw instrument driver.

Basic Hello-World code:

.. code-block:: python

    from RsFsw import *

    instr = RsFsw('TCPIP::192.168.2.101::hislip0')
    idn = instr.query('*IDN?')
    print('Hello, I am: ' + idn)

Check out the full documentation on `ReadTheDocs <https://RsFsw.readthedocs.io/>`_.

Supported instruments: FSW, FSVA3000

The package is hosted here: https://pypi.org/project/RsFsw/

Documentation: https://rohde-schwarz.github.io/RsFsw_PythonDocumentation/

Examples: https://github.com/Rohde-Schwarz/Examples/tree/main/SpectrumAnalyzers/Python/RsFsw_ScpiPackage


Version history
----------------

	Latest release notes summary: Update for FSW FW 5.20

	Version 5.20.0
		- Update for FSW FW 5.20

	Version 5.0.0
		- First released version
