import pytest
import os.path


@pytest.fixture
def gff_file():
    return os.path.join(os.path.dirname(__file__), 'data',
                        'ColCEN_AT1G01010-20_TAIR10.gff3.gz')

@pytest.fixture
def gff_data():
    return (
        ('Chr1', 7489, 9757, '+', {'ID': 'AT1G01010', 'Note': 'protein_coding_gene', 'Name': 'AT1G01010', 'coverage': '1.0', 'sequence_ID': '1.0', 'extra_copy_number': '0', 'copy_num_ID': 'AT1G01010_0'}),
        ('Chr1', 9786, 12596, '-', {'ID': 'AT1G01020', 'Note': 'protein_coding_gene', 'Name': 'AT1G01020', 'coverage': '1.0', 'sequence_ID': '1.0', 'extra_copy_number': '0', 'copy_num_ID': 'AT1G01020_0'})
    )

@pytest.fixture
def bed_data():
    return (
        (('Chr1', 7488, 9757, 'AT1G01010', 0, '+'),
        ('Chr1', 9785, 12596, 'AT1G01020', 0, '-'))
    )
