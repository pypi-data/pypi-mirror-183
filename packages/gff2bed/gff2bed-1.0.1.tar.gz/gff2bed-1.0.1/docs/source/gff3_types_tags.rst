GFF3 types and tags
===================

Types
-----

By default, ``gff2bed.parse()`` only considers records of type *gene* in the input GFF3 file. To parse a different record type, set the ``type`` argument accordingly. For example to parse *mRNA* records:

.. code-block:: python
   
   GFF3_FILE = 'ColCEN_AT1G01010-20_TAIR10.gff3.gz'
   mrna_records = pd.DataFrame(gff2bed.parse(GFF3_FILE, type='mRNA'))
   mrna_records.head()

.. code-block:: none

         0      1      2  3                                                  4
   0  Chr1   7489   9757  +  {'ID': 'AT1G01010.1', 'Parent': 'AT1G01010', '...
   1  Chr1   9786  12596  -  {'ID': 'AT1G01020.1', 'Parent': 'AT1G01020', '...
   2  Chr1  10649  12596  -  {'ID': 'AT1G01020.2', 'Parent': 'AT1G01020', '...

To parse *exon* records:

.. code-block:: python

   exon_records = pd.DataFrame(gff2bed.parse(GFF3_FILE, type='exon'))
   exon_records.head()

.. code-block:: none

         0     1     2  3                                                  4
   0  Chr1  7489  7771  +  {'Parent': 'AT1G01010.1', 'extra_copy_number':...
   1  Chr1  7854  8134  +  {'Parent': 'AT1G01010.1', 'extra_copy_number':...
   2  Chr1  8344  8463  +  {'Parent': 'AT1G01010.1', 'extra_copy_number':...
   3  Chr1  8564  8953  +  {'Parent': 'AT1G01010.1', 'extra_copy_number':...
   4  Chr1  9032  9184  +  {'Parent': 'AT1G01010.1', 'extra_copy_number':...

.. note::

   Be mindful that different record types may have different attribute tags

Tags
----

By default, ``gff2bed.convert()`` uses the value of each record's *ID* tag to populate the name field of the emitted BED data. Sometimes, you may wish to use a different tag. For instance, the *exon* records in the example file do not have an *ID* tag, so by default passing those data to ``gff2bed.convert()`` will cause an error.

.. code-block:: python

   exon_bedtool = pybedtools.BedTool(gff2bed.convert(gff2bed.parse(GFF3_FILE, type='exon'))).saveas()

.. code-block:: none

   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "/Users/anthonyaylward/opt/anaconda3/envs/gff2bed/lib/python3.10/site-packages/pybedtools/bedtool.py", line 923, in decorated
       result = method(self, *args, **kwargs)
     File "/Users/anthonyaylward/opt/anaconda3/envs/gff2bed/lib/python3.10/site-packages/pybedtools/bedtool.py", line 3362, in saveas
       fn = self._collapse(
     File "/Users/anthonyaylward/opt/anaconda3/envs/gff2bed/lib/python3.10/site-packages/pybedtools/bedtool.py", line 1422, in _collapse
       for i in iterable:
     File "pybedtools/cbedtools.pyx", line 760, in pybedtools.cbedtools.IntervalIterator.__next__
     File "/Users/anthonyaylward/Documents/michael-lab/gff2bed/gff2bed/gff2bed.py", line 89, in convert
       yield seqid, start - 1, end, attr[tag], 0, strand
   KeyError: 'ID'

To handle this situation, set the ``tag`` argument of ``gff2.bed.convert()`` to
"Parent". Then the *Parent* tag will be used instead of *ID*.

.. code-block:: python

   exon_bedtool = pybedtools.BedTool(gff2bed.convert(gff2bed.parse(GFF3_FILE, type='exon'), tag='Parent')).saveas()
   exon_bedtool.head()

.. code-block:: none

   Chr1    7488    7771    AT1G01010.1     0       +
    Chr1   7853    8134    AT1G01010.1     0       +
    Chr1   8343    8463    AT1G01010.1     0       +
    Chr1   8563    8953    AT1G01010.1     0       +
    Chr1   9031    9184    AT1G01010.1     0       +
    Chr1   9296    9757    AT1G01010.1     0       +
    Chr1   9785    10121   AT1G01020.1     0       -
    Chr1   10295   10928   AT1G01020.1     0       -
    Chr1   11015   11091   AT1G01020.1     0       -
    Chr1   11242   11309   AT1G01020.1     0       -
