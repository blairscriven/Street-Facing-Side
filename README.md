# Street Facing Side - QGIS Plugin

Identifies the side of the polygon (e.g. parcels or building footprints) that is facing the street, river, or any other line vector file type. Outputs a new line feature for each polygon feature, based on what side of the polygon was identified as the 'street-facing' side. Requires both an input polygon layer and input line layer. See the following example:

<img src="img\Example1.PNG"  width=30% height=30%>

*Data Source: City of Calgary, 2023, "Buildings", https://data.calgary.ca/Base-Maps/Buildings/uc4c-6kbd; City of Calgary, 2023, "Street Centreline", https://data.calgary.ca/Transportation-Transit/Street-Centreline/4dx8-rtm5 --- Edited the data to focus on just the University Heights neighbourhood in Calgary*

<br>

## Uses

Could be used to facilitate large Google-Street-View image requests - might help avoid errors where the returned image is from the back of house/building. Also, could help create more specific zonal statistics estimations. Further, could identify the side of building with a river view or the side of building with greatest proximity to inundation (using flood water contours).

## Installation

Currently, you can download the plugin from GitHub or the [QGIS Python Plugins Repository](https://plugins.qgis.org/plugins/street_facing_side/) as a zip file and then use the 'Install from ZIP' tab in the plugin manager. The plugin was created for QGIS version 3.22.8 and has not been tested on later versions. Once installed, you should see this icon: ![Srt_fac_icon](icon.png) in the 'Plugin' menu.

## Limitations

This tool is still in it's early development, so it still produces some errors and has performance limits. For example, if there is one polygon feature in front of another (compared to the street, river, etc), it can cause the wrong side to be identified as 'street-facing', as seen here:

<img src="img\Issue1.PNG"  width=30% height=30%>

*Data Source: City of Calgary, 2023, "Buildings", https://data.calgary.ca/Base-Maps/Buildings/uc4c-6kbd; City of Calgary, 2023, "Street Centreline", https://data.calgary.ca/Transportation-Transit/Street-Centreline/4dx8-rtm5 --- Edited the data to focus on just the University Heights neighbourhood in Calgary*

Planned updates:
- Create point layer in the centre of 'street-facing' line layer
- Fix the overlapping line errors
- Fix issue with features on street corners (often identifies the side of house as 'street-facing')

If you encounter any further issues or want to suggest improvements, please add a ticket to the'[issues](https://github.com/blairscriven/Street-Facing-Side/issues)' tab. You can also e-mail me at scrivenblair@gmail.com