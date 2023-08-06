"""`GFF3 <https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md>`_ and `BED <https://bedtools.readthedocs.io/en/latest/content/general-usage.html>`_ are common formats for storing the coordinates of genomic features such as genes. GFF3 format is more versatile, but BED format is simpler and enjoys a rich ecosystem of utilities such as `bedtools <https://bedtools.readthedocs.io/en/latest/index.html>`_. For this reason, it is often convenient to store genomic features in GFF3 format and convert them to BED format for genome arithmetic.

This module provides two convenience functions to streamline converting data from GFF3 to BED format for bioinformatics analysis: ``parse()``, which reads data from a GFF3 file, and ``convert()``, which converts GFF3-formatted data to BED-formatted data that can be passed on e.g. to `pybedtools <https://daler.github.io/pybedtools/>`_.
"""

from gff2bed.version import __version__
from gff2bed.gff2bed import parse, convert