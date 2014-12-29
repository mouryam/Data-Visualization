"""
Data Visualization Project
Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.

Tutorial followed by Mourya Meda

Tutorial licensing:
Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.
"""

import csv


# Put the full path to your CSV/Excel file here
MY_FILE = "../data/SFPD_Incidents_12_7_2014_to_12_14_2014.csv"


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Build a data structure to return parsed_data
	# Setup an empty list
    parsed_data = []

    # Skip over the first line with headers in the file
    fields = csv_data.next()

    # Iterate over each row of file, zip together field and value
    for row in csv_data:
    	parsed_data.append(dict(zip(fields, row)))

    # Close file
    opened_file.close()

    return parsed_data

def main():

	#Call parse function
	new_data = parse(MY_FILE, ",")

	#Print it out
	print new_data

if __name__ == "__main__":
    main()
