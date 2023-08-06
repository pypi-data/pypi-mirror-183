import pytest
import gff2bed

def test_parse(gff_data, bed_data):
    assert tuple(gff2bed.convert(gff_data)) == bed_data
