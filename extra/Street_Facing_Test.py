import time

import processing
from processing.core.Processing import Processing

# Set-up Paths
Footprint_GEOPKG = 'Building_Footprints.gpkg'
Road_GEOPKG = 'Main_Roads.gpkg'
ex = 'explode.gpkg'
Output_Line = 'Building_StreetFace_Line.gpkg'
Output_Point = 'Building_StreetFace_Point.gpkg'

# Nicely formatted time string
def hms_string(sec_elapsed):
	h = int(sec_elapsed / (60 * 60))
	m = int((sec_elapsed % (60 * 60)) / 60)
	s = sec_elapsed % 60
	return "{}:{:>02}:{:>05.2f}".format(h, m, s)
start_time = time.time()

Processing.initialize()  # Enables Processing module


poly_to_lines = processing.run("native:polygonstolines", {'INPUT': Footprint_GEOPKG,
														  'OUTPUT': 'memory:'})

Footprint_Centroids = processing.run("native:centroids", {'INPUT': Footprint_GEOPKG,
														  'OUTPUT': 'memory:'})

Exploded_Lines = processing.run("native:explodelines", {'INPUT': poly_to_lines['OUTPUT'],
														'OUTPUT': ex})

Centroids_w_nearRoad_points = processing.run("native:joinbynearest", {'INPUT': Footprint_Centroids['OUTPUT'],
																	  'INPUT_2': Road_GEOPKG,
																	  'DISCARD_NONMATCHING': True,
																	  'OUTPUT': 'memory:'})

Building_to_Road_Line = processing.run("native:geometrybyexpression", {'INPUT': Centroids_w_nearRoad_points['OUTPUT'],
																	   'OUTPUT_GEOMETRY':1,
																	   'EXPRESSION':'MAKE_LINE($geometry, MAKE_POINT("nearest_x", "nearest_y"))',
																	   'OUTPUT': 'memory:'})

processing.run("native:extractbylocation", {'INPUT': ex,
											'PREDICATE': [0],
											'INTERSECT': Building_to_Road_Line['OUTPUT'],
											'OUTPUT': Output_Line})


# End the timer
time_took = time.time() - start_time
time_took_pretty = hms_string(time_took)
print(f"Total runtime: {hms_string(time_took)}")

'''
Extra Code - may or may not need in the future:

Points_on_Poly_4m = processing.run("native:pointsalonglines", {'INPUT':Footprint_GEOPKG,
															'DISTANCE': 4,
															'OUTPUT': 'memory:'})

Create line between road and building using this code in 'Geometry as Expression' tool:
make_line(
  -- the current feature's geometry (point from sensor layer).
  $geometry,
  -- the matching feature's geometry from the layer 'place-name-osm-clean'
  -- where the attribute 'name_en' matches the current feature's attribute
  -- "PLACE_NAME_NAME_EN"
  geometry(get_feature('place-name-osm-clean', 'name_en', "PLACE_NAME_NAME_EN" ))
)'''