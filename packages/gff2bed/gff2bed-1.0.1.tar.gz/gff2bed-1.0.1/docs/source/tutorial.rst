Tutorial
========

To follow this tutorial, first ensure you have the following modules installed
in addition to ``gff2bed``:

- `urllib3 <https://urllib3.readthedocs.io/en/stable/>`_
- `pandas <https://pandas.pydata.org/docs/>`_
- `pybedtools <https://daler.github.io/pybedtools/>`_

This tutorial will involve working with some files on disk, so we'll make a
temporary directory for easy cleanup later.

.. code-block:: python

    from tempfile import TemporaryDirectory
    temp_dir = TemporaryDirectory()

Next, download an example GFF3 file

.. code-block:: python

   import urllib3
   import shutil
   import os.path
   GFF3_URL = 'https://gitlab.com/salk-tm/gff2bed/-/raw/main/test/data/ColCEN_AT1G01010-20_TAIR10.gff3.gz'
   GFF3_FILE = os.path.join(temp_dir.name, 'ColCEN_AT1G01010-20_TAIR10.gff3.gz')
   http = urllib3.PoolManager()
   with http.request('GET', GFF3_URL, preload_content=False) as r, open(GFF3_FILE, 'wb') as dest_file:
       shutil.copyfileobj(r, dest_file)

To read the GFF3 file into a Pandas data frame without converting to BED, use ``gff2bed.parse()``

.. code-block:: python
    
   import pandas as pd
   import gff2bed
   gff_data = pd.DataFrame(gff2bed.parse(GFF3_FILE))
   gff_data.head()

.. code-block:: none

         0     1      2  3                                                  4
   0  Chr1  7489   9757  +  {'ID': 'AT1G01010', 'Note': 'protein_coding_ge...
   1  Chr1  9786  12596  -  {'ID': 'AT1G01020', 'Note': 'protein_coding_ge...

.. note::

   The implementation of ``gff2bed`` follows a philosophy of simplicity. It depends on nothing but the built-in python libraries, and it includes nothing but the ``parse()`` and ``convert()`` functions. Typically when applying ``gff2bed`` in practice, you will use it in conjunction with other modules such as ``pandas`` or ``pybedtools`` 

To create a data frame of BED formatted data, pass the stream to ``gff2bed.convert()`` before passing to ``pd.DataFrame()``

.. code-block:: python

   bed_data = pd.DataFrame(gff2bed.convert(gff2bed.parse(GFF3_FILE)))
   bed_data.head()

.. code-block:: none

         0     1      2          3  4  5
   0  Chr1  7488   9757  AT1G01010  0  +
   1  Chr1  9785  12596  AT1G01020  0  -

You can similarly create a ``BedTool`` with ``pybedtools``

.. code-block:: python

   from pybedtools import BedTool
   bed_data = BedTool(gff2bed.convert(gff2bed.parse(GFF3_FILE))).saveas()
   bed_data.head()

.. code-block:: none

    Chr1    7488    9757    AT1G01010       0       +
     Chr1   9785    12596   AT1G01020       0       -

To complete the tutorial, clean up the temporary directory

.. code-block:: python

    temp_dir.cleanup()
