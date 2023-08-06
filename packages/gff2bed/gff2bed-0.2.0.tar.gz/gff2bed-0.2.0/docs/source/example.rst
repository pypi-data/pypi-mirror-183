Example
=======

.. code-block:: python

   import urllib3
   import shutil
   import pandas as pd
   import pybedtools
   import gff2bed
   
   GFF3_URL = 'https://gitlab.com/salk-tm/gff2bed/-/raw/main/test/data/ColCEN_AT1G01010-20_TAIR10.gff3.gz'
   
   # Download the example GFF3 file
   http = urllib3.PoolManager()
   with http.request('GET', GFF3_URL, preload_content=False) as r, open('ColCEN_AT1G01010-20_TAIR10.gff3.gz', 'wb') as dest_file:
       shutil.copyfileobj(r, dest_file)
   
   # Parse the GFF3 data into a Pandas data frame
   genes_df = pd.DataFrame(gff2bed.parse('ColCEN_AT1G01010-20_TAIR10.gff3.gz'))
   genes_df.head()
   
   # Parse the GFF3 data into a pybedtools BedTool
   genes_bt = pybedtools.BedTool(gff2bed.convert(gff2bed.parse('ColCEN_AT1G01010-20_TAIR10.gff3.gz'))).saveas('ColCEN_AT1G01010-20_TAIR10.bed')
   genes_bt.head()
