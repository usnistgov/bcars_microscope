.. -*- mode: rst -*-

.. image:: https://github.com/usnistgov/bcars_microscope/actions/workflows/python-testing.yml/badge.svg
	:alt: pytest
	:target: https://github.com/usnistgov/bcars_microscope/actions/workflows/python-testing.yml

.. image:: https://codecov.io/gh/usnistgov/bcars_microscope/branch/main/graph/badge.svg?token=WIHgHEUc82
	:alt: Codecov
	:target: https://codecov.io/gh/usnistgov/bcars_microscope

.. image:: https://img.shields.io/badge/License-NIST%20Public%20Domain-green.svg
    :alt: NIST Public Domain
    :target: https://github.com/usnistgov/bcars_microscope/blob/main/LICENSE.md

BCARS Microscope - Python software to run BCARS microscope at NIST.
============================================================

Python software to run BCARS microscope at NIST.

References
~~~~~~~~~~~

.. [1] J. Smith, "A clever title", A clever journal **vol**, p -- p (2000). 

Dependencies
------------

-   Python 3.* (Tested on 3.8)
-   NumPy (Tested on 1.19)
-   SciPy (Tested on 1.5)
-   Scikit-learn (Tested on 1.0)

Installation
-------------

**NOTE**: The `examples/` and `doc/` folders are not included in the pip installation.
You will need to download the file from the `GitHub repo <https://github.com/usnistgov/bcars_microscope>`_ manually. 

Using pip
~~~~~~~~~

.. code::

    pip install bcars_microscope

Using pip (soft install, i.e. can update with git)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::
    
    # Make new directory for bcars_microscope and enter it
    # Clone from github
    git clone https://github.com/usnistgov/bcars_microscope .

    pip install -e .

    # To update in the future
    git pull

Usage
------

Citing This Software
---------------------

J. Smith, "A clever title", A clever journal **vol**, p -- p (2000). 

LICENSE
----------
This software was developed by employees of the National Institute of Standards and Technology (NIST), an agency of the Federal Government. Pursuant to `title 17 United States Code Section 105 <http://www.copyright.gov/title17/92chap1.html#105>`_, works of NIST employees are not subject to copyright protection in the United States and are considered to be in the public domain. Permission to freely use, copy, modify, and distribute this software and its documentation without fee is hereby granted, provided that this notice and disclaimer of warranty appears in all copies.

THE SOFTWARE IS PROVIDED 'AS IS' WITHOUT ANY WARRANTY OF ANY KIND, EITHER EXPRESSED, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTY THAT THE SOFTWARE WILL CONFORM TO SPECIFICATIONS, ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND FREEDOM FROM INFRINGEMENT, AND ANY WARRANTY THAT THE DOCUMENTATION WILL CONFORM TO THE SOFTWARE, OR ANY WARRANTY THAT THE SOFTWARE WILL BE ERROR FREE. IN NO EVENT SHALL NIST BE LIABLE FOR ANY DAMAGES, INCLUDING, BUT NOT LIMITED TO, DIRECT, INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES, ARISING OUT OF, RESULTING FROM, OR IN ANY WAY CONNECTED WITH THIS SOFTWARE, WHETHER OR NOT BASED UPON WARRANTY, CONTRACT, TORT, OR OTHERWISE, WHETHER OR NOT INJURY WAS SUSTAINED BY PERSONS OR PROPERTY OR OTHERWISE, AND WHETHER OR NOT LOSS WAS SUSTAINED FROM, OR AROSE OUT OF THE RESULTS OF, OR USE OF, THE SOFTWARE OR SERVICES PROVIDED HEREUNDER.

Contact
-------
Charles H. Camp Jr.: `charles.camp@nist.gov <mailto:charles.camp@nist.gov>`_

Contributors
-------------

-   Charles H. Camp Jr.
