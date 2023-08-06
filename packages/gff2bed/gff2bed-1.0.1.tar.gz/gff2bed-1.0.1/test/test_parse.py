import pytest
import gff2bed

def test_parse(gff_file, gff_data):
    assert tuple(gff2bed.parse(gff_file)) == gff_data
