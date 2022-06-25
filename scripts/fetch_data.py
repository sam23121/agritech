import pandas as pd
import pdal
import json
import geopandas as gpd
from pyproj import Transformer
# from bounds import Bounds
from logs import logging
from shapely.geometry import Polygon, Point
import numpy as np


headers = [*pd.read_csv('../data/metadata.csv', nrows=1)]
df = pd.read_csv('../data/metadata.csv', usecols=[c for c in headers if c != 'Unnamed: 0'], index_col='filename')

PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"

tif_filename = '../data/USGS_1M_11_x56y495_ID_AdamsCounty_2019_B19.tif'
laz_filename = '../data/USGS_LPC_ID_AdamsCounty_2019_B19_11TNK05644945.laz'
filename_tif = '../data/usgs.tif'
filename_laz = '../data/usgs.laz'

MINX, MINY, MAXX, MAXY = [-93.756155, 41.918015, -93.747334, 41.921429]
poly = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))

input_epsg = 3857
output_epsg = 26915

def get_polygon(polygon):
    
    polygon_df = gpd.GeoDataFrame()
    polygon_df['geometry'] = None
    polygon_df.loc[0, 'geometry'] = poly
    polygon_df.set_crs(epsg=output_epsg, inplace=True)
    polygon_df['geometry'] = polygon_df['geometry'].to_crs(epsg=3857)
    minx, miny, maxx, maxy = polygon_df['geometry'][0].bounds
    bound = f"({[minx, maxx]},{[miny,maxy]})"
    xcord, ycord = polygon_df['geometry'][0].exterior.coords.xy
    polygon_input = 'POLYGON(('
    for x, y in zip(list(xcord), list(ycord)):
        polygon_input += f'{x} {y}, '
    polygon_input = polygon_input[:-2]
    polygon_input += '))'

    print(polygon_input)

    return bound, polygon_input

def get_pipeline(polygon, region):
    
    try:
        # pipe = json.read_json('../usgs2.json')
        json_obj = 'usgs.json'
        with open(json_obj, 'r') as json_file:
            pipe = json.load(json_file)
        PUBLIC_ACCESS_PATH = PUBLIC_DATA_PATH+region+"ept.json"
        filename = region
        xmin = df.loc[filename, 'xmin']
        ymin = df.loc[filename, 'ymin']
        xmax = df.loc[filename, 'xmax'] 
        ymax = df.loc[filename, 'ymax'] 
        # points = df.loc[filename, 'points'] 

        pipe['pipeline'][0]['filename'] = PUBLIC_ACCESS_PATH
        pipe['pipeline'][0]['bounds'] = [int(xmin), int(ymin),int(xmax), int(ymax)]
        pipe['pipeline'][1]['polygon'] = polygon
        pipe['pipeline'][4]['filename'] = filename_laz #laz_filename
        pipe['pipeline'][5]['filename'] = filename_tif #tif_filename
        logging.info("pipeline initiated")
        with open("new.json", "w") as write_file:
            json.dump(pipe, write_file, indent=4)
        pl = pdal.Pipeline(json.dumps(pipe))

        return pl
    except:
        logging.exception("failed to initiate pipeline")


def get_elevation(bounds, polygon_str, region):
    
    filename = region
    pl = get_pipeline(polygon_str, region)
    pl.execute()
    print(pl)
    for i in pl.arrays:
      geometry_points = [Point(x, y) for x, y in zip(i["X"], i["Y"])]
      elevations = np.array(i["Z"])

      df2 = gpd.GeoDataFrame(columns=["elevation", "geometry"])
      df2['elevation'] = elevations
      df2['geometry'] = geometry_points
      df2 = df2.set_geometry("geometry")
      df2.set_crs(epsg=output_epsg, inplace=True)
    logging.info(f"successfully read geodata: {filename}")
    
    return df2

def fetch(polygon, region):
    
    bound, polygon_str = get_polygon(polygon)
    df = get_elevation(bound, polygon_str, region)
    
    geo_data = list()
    geo_data.append({'geo_data': df})
    return geo_data

if __name__ == "__main__":
    fetch(Polygon, region='IA_FullState/')



 