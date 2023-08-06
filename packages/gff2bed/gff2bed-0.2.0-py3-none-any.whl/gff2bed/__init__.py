"""This package provides two convenience functions to streamline converting
data from GFF3 to BED format for bioinformatics analysis: `parse()`, which
reads data from a GFF3 file, and `convert()`, which converts GFF3-formatted
data to BED-formatted data that can be passed on e.g. to
[pybedtools](https://daler.github.io/pybedtools/).
"""

from gff2bed.version import __version__
from gff2bed.gff2bed import parse, convert