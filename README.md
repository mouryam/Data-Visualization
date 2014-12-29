Data-Visualization
==================

Parse data using Python's data structures to create a GeoJSON file for mapping.

The data is retreived from any police department's monthly reports.
The following report is collected from San Fransisco during the week of 12/07/2014 to 12/14/2014.
  
Parse.py :

Retrieves data from CSV/Excel file and returns in into a format that is easier for Python to use.

Graph.py:

Takes the data from the Parse.py and visualizes it using the Python math libraries.
Furthermore, there is a 

    visualize_days() 
which outputs in terms of a line graph for the DaysOfWeek, and

    visualize_type()
which outputs a bar graph with various categories of incidents,
  
Map.py:

Takes the data that was parsed and create a different format to render
a map. Parses through each line item of the CSV file and create a geojson object. 
Finally, collects these objects into one geojson file to upload to gist.github.com

The result of the GeoJSon file from this process is below:

https://gist.github.com/mouryam/2e7d0706061bbafbba41#file-week_of_12_07_2014-geojson 
