import numpy as np
import laspy as lp
import matplotlib.pyplot as plt
import geopandas as gpd
from .logs import log
import os




input_path = "../data/"
dataname = "USGS_LPC_ID_AdamsCounty_2019_B19_11TNK05644945"

point_cloud = lp.read(input_path+dataname+".las")

colors = np.vstack((point_cloud.red, point_cloud.green,
                   point_cloud.blue)).transpose()


def plot_3d_map(df):
    
    if df['elevation'][0] != None:
        gdf = df
        gdf.crs = "epsg:4326"
        print(gdf)

    x = gdf.geometry.x
    y = gdf.geometry.y
    z = gdf.elevation
    points = np.vstack((x, y, z)).transpose()
    factor = 160
    decimated_points = points[::]
    decimated_colors = colors[::]
    print(len(decimated_colors))
    print(decimated_colors)
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    ax = plt.axes(projection='3d')
    ax.scatter(decimated_points[:, 0], decimated_points[:, 1],
               decimated_points[:, 2],  s=0.01, color=decimated_colors/255)
    plt.show()