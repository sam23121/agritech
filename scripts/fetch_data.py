import pandas as pd
import pdal
import json
import geopandas as gpd
# from pyproj import Transformer
# from bounds import Bounds
from logs import logging
from shapely.geometry import Polygon, Point
import numpy as np


# headers = [*pd.read_csv('../data/metadata.csv', nrows=1)]
# df = pd.read_csv('../data/metadata.csv', usecols=[c for c in headers if c != 'Unnamed: 0'], index_col='filename')

# PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"

# tif_filename = '../data/USGS_1M_11_x56y495_ID_AdamsCounty_2019_B19.tif'
# laz_filename = '../data/USGS_LPC_ID_AdamsCounty_2019_B19_11TNK05644945.laz'
# filename_tif = '../data/usgs.tif'
# filename_laz = '../data/usgs.laz'

# MINX, MINY, MAXX, MAXY = [-93.756155, 41.918015, -93.747334, 41.921429]
# poly = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))

# input_epsg = 3857
# output_epsg = 4326 

class Fetch:

    def __init__(self):
        
        self.input_epsg = 3857
        self.MINX = -93.756155
        self.MINY = 41.918015
        self.MAXX = -93.747334
        self.MINY = 41.921429
        self.PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
        self.tif_filename = '../data/data'
        self.laz_filename = '../data/data'
        self.output_epsg = 4326 


    def get_polygon(self, polygon):
        
        # polygon_df = gpd.GeoDataFrame()
        # polygon_df['geometry'] = None
        # polygon_df.loc[0, 'geometry'] = polygon
        polygon_df = gpd.GeoDataFrame([polygon], columns=['geometry'])
        polygon_df.set_crs(epsg=self.output_epsg, inplace=True)
        polygon_df['geometry'] = polygon_df['geometry'].to_crs(epsg=self.input_epsg)
        minx, miny, maxx, maxy = polygon_df['geometry'][0].bounds
        bound = f"([{minx}, {miny}], [{maxx}, {maxy}])"
        xcord, ycord = polygon_df['geometry'][0].exterior.coords.xy
        polygon_input = 'POLYGON(('
        for x, y in zip(list(xcord), list(ycord)):
            polygon_input += f'{x} {y}, '
        polygon_input = polygon_input[:-2]
        polygon_input += '))'

        print(polygon_input)

        return bound, polygon_input

    def get_pipeline(self, bounds, polygon, region):
        
        try:
            # pipe = json.read_json('../usgs2.json')
            json_obj = 'usgs2.json'
            with open(json_obj, 'r') as json_file:
                pipe = json.load(json_file)
            # filename = region
            # points = df.loc[filename, 'points'] 

            pipe['pipeline'][0]['filename'] = self.PUBLIC_DATA_PATH + region + "/ept.json"
            pipe['pipeline'][0]['bounds'] = bounds
            pipe['pipeline'][1]['polygon'] = polygon
            pipe['pipeline'][7]['filename'] =  self.laz_filename + ".laz"
            pipe['pipeline'][8]['filename'] =  self.tif_filename + ".tif"
            logging.info("pipeline initiated")
            with open("new.json", "w") as write_file:
                json.dump(pipe, write_file, indent=4)
            pl = pdal.Pipeline(json.dumps(pipe))

            return pl
        except:
            logging.exception("failed to initiate pipeline")


    def get_elevation(self, bounds, polygon_str, region):
        
        filename = region
        pl = self.get_pipeline(bounds, polygon_str, region)
        pl.execute()
        print(pl)
        for i in pl.arrays:
            geometry_points = [Point(x, y) for x, y in zip(i["X"], i["Y"])]
            elevations = np.array(i["Z"])

            df2 = gpd.GeoDataFrame(columns=["elevation", "geometry"])
            df2['elevation'] = elevations
            df2['geometry'] = geometry_points
            df2 = df2.set_geometry("geometry")
            df2.set_crs(epsg=self.output_epsg, inplace=True)
            logging.info(f"successfully read geodata: {filename}")
        
        return df2

    def fetch(self, polygon, region):
        
        bound, polygon_str = self.get_polygon(polygon)
        df = self.get_elevation(bound, polygon_str, region)
        
        geo_data = list()
        geo_data.append({'geo_data': df})
        return geo_data

    # if __name__ == "__main__":
    #     fetch(Polygon, region='IA_FullState/')



    
