json = """
[
    "../data/USGS_LPC_ID_AdamsCounty_2019_B19_11TNK05644945.laz",
    {
        "type": "filters.sort",
        "dimension": "X"
    }
]
"""

import pdal
pipeline = pdal.Pipeline(json)
count = pipeline.execute()
arrays = pipeline.arrays
metadata = pipeline.metadata
log = pipeline.log