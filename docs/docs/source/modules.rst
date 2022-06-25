Modules
=====

fetching data
------------

to get the shape conrdinate
----------------

To retrieve the coordinates of the shape,
you can use the ``fetch_data.get_polygon()`` function:

.. py:function:: fetch.get_polygon(polygon : str)

   Return a list of random ingredients as strings.

   :param kind: the shape of the polygon.
   :type kind: str
   :return: boundary and coordinates of the polygon.
   :rtype: tuple, str

to get the pipeline
----------------

To get the pipeline,
you can use the ``fetch_data.get_pipeline()`` function:

.. py:function:: fetch.get_pipeline(polygon_input : str, region : str)

   Return a json file with all the information.

   :param kind: the polygon coordinate, the region of the area
   :type kind: str, str              
   :return: json file.
   :rtype: json

to get the elevation of the ground
----------------

To retrieve the elevation of the ground,
you can use the ``fetch_data.get_elevation()`` function:

.. py:function:: fetch.get_polygon(bounds: str, polygon_str: str, region: str)

   Return a dataframe with the elevation and coordinate as a columns.

   :param kind: the boumdaries, the shape of the polygon, the region of the area
   :type kind: str, str, str              
   :return: dataframe.
   :rtype: df

to process it all in one
----------------

To do all the above fuctions and get list of elevation of coordinates,
you can use the ``fetch_data.fetch()`` function:

.. py:function:: fetch.fetch(polygon_str: str, region: str)

   Return a lists of dataframe.

   :param kind:  the shape of the polygon, the region of the area
   :type kind: str, str
   :return: a list of elevations.
   :rtype: list 
