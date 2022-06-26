# Python package for handling LIDAR data point cloud 
How much maize a field produces is very spatially variable. Even if the same farming practices, seeds and fertilizer are applied exactly the same by machinery over a field, there can be a very large harvest at one corner and a low harvest at another corner.  We would like to be able to better understand which parts of the farm are likely to produce more or less maize, so that if we try a new fertilizer on part of this farm, we have more confidence that any differences in the maize harvest 9are due mostly to the new fertilizer changes, and not just random effects due to other environmental factors. 

Water is very important for crop growth and health.  We can better predict maize harvest if we better understand how water flows through a field, and which parts are likely to be flooded or too dry. One important ingredient to understanding water flow in a field is by measuring the elevation of the field at many points. The USGS recently released high resolution elevation data as a lidar point cloud called USGS 3DEP in a public dataset on Amazon. This dataset is essential to build models of water flow and predict plant health and maize harvest.

the task to produce an easy to use, reliable and well designed python module that domain experts and data scientists can use to fetch, visualise, and transform publicly available satellite and LIDAR data. In particular, your code should interface with USGS 3DEP and fetch data using their API.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [Contact](#contact)

## General info
the package does the following task 
- Data Fetching and Loading
- Visualization
- Data Transformation


## Technologies
* sphinx for docs


## Setup:
```
git clone https://github.com/sam23121/agritech.git
pip install -r requirements.py
python -m testing
```
the docs for the package is https://sam23121.github.io/docs/html/index.html


## Code Examples
Show examples of usage:
```
pl = Fetch()
gdf = pl.fetch(polygon, "IA_FullState")
```




## To-do list:
* improve the modularity
* let users choose from a list of states
* improve the docs

## Status
Project is: _in progress_,



## Contact
Created by [@sam23121] - feel free to contact me!