"""
Part III: Take the data that was parsed and create a different format to render
a map. Parse through each line item of the CSV file and create a geojson object.
Collect these objects into one geojson file to upload to gist.github.com
"""

import geojson
import Parse as p

def create_map(data_file):
    """ Creates and returns a GeoJSon file"""

    geo_map = {"type": "FeatureCollection"}

    # empty list to collect each point to graph
    item_list = []

    # iterate over the data to create the GeoJSon file.
    # using enumerate() to get the line and index which is the line number
    for index, line in enumerate(data_file):

        # skip the zero coordinates to prevent errors in map
        if line['X'] == "0" or line['Y'] == "0":
            continue

        # make new dict for each iteration
        data = {}

        # assign line items to the GeoJSOn fields
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                              ' description': line['Descript'],
                              'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        # add data dict to the item_list
        item_list.append(data)

    # for each point in item_list, add the point to the geo_map dictionary
    # setdefault creates a key called "features" with the type of an empty list
    # with each iteration, the point is added to the list
    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    # all the data is parsed in GeoJSon. Write to a file and upload
    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))

def main():
    data = p.parse(p.MY_FILE, ",")
    return create_map(data)

if __name__ == "__main__":
    main()
