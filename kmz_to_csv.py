import zipfile
import csv
from xml.dom import minidom

# Open the KMZ file
with zipfile.ZipFile('locations.kmz', 'r') as kmz:
    # Extract the KML file from the KMZ
    kml_filename = kmz.namelist()[0]  # Assuming there's only one file in the KMZ
    kmz.extract(kml_filename)

# Parse the KML file
xmldoc = minidom.parse(kml_filename)
placemarks = xmldoc.getElementsByTagName('Placemark')

data = [['X', 'Y', 'Name', 'Layer']]  # Initialize the data with the header

# Get the layer styles
layer_styles = xmldoc.getElementsByTagName('Style')

# Assign layers to placemarks
for i, placemark in enumerate(placemarks, start=1):
    point = placemark.getElementsByTagName('Point')[0]
    coordinates = point.getElementsByTagName('coordinates')[0].firstChild.data.strip().split(',')
    name = placemark.getElementsByTagName('name')[0].firstChild.data.strip()
    
    # Get the styleUrl
    style_url = placemark.getElementsByTagName('styleUrl')[0].firstChild.data.strip()
    
    # Extract the color from the styleUrl
    color = style_url.split('-')[2]
    
    # Assign layer based on the color
    layer = f'Layer {color}'
    
    x, y = coordinates[:2]
    data.append([x, y, name, layer])

# Write the data to a CSV file
csv_filename = 'input.csv'

with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

print(f'Successfully extracted data to {csv_filename}.')
