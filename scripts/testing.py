# import pandas as pd
# import pdal
# import json
# import geopandas as gpd
# from pyproj import Transformer
# # from bounds import Bounds
# from logs import logging
# from shapely.geometry import Polygon, Point
# import numpy as np


# headers = [*pd.read_csv('../data/metadata.csv', nrows=1)]
# df = pd.read_csv('../data/metadata.csv', usecols=[c for c in headers if c != 'Unnamed: 0'], index_col='filename')

# PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"

# tif_filename = '../data/USGS_1M_11_x56y495_ID_AdamsCounty_2019_B19.tif'
# laz_filename = '../data/USGS_LPC_ID_AdamsCounty_2019_B19_11TNK05644945.laz'

import matplotlib.pyplot as plt
from shapely.geometry import Polygon

from fetch_data import Fetch

pl = Fetch()

MINX, MINY, MAXX, MAXY = [-93.756155, 41.918015, -93.747334, 41.921429]
polygon = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))

gdf = pl.fetch(polygon, "IA_FullState")
print(gdf)