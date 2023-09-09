import csv
import os
import urllib.parse

# Read the CSV file
csv_filename = 'input.csv'
output_folder = 'output'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Dictionary to store the data for each layer
layer_data = {}

with open(csv_filename, 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        layer = row[3]  # Assuming layer column is in the fourth column (index 3)

        # Create a new TXT file for the layer if it doesn't exist
        if layer not in layer_data:
            layer_data[layer] = []

        # Replace double quotes with single quotes in the location name
        name = row[2].replace('"', "'")

        # Construct link to the actual place using location name
        link_name = urllib.parse.quote(name)  # URL encode the name
        google_maps_link = f'https://www.google.com/maps/search/?api=1&query={link_name}'

        # Add the simplified hyperlink to the row
        hyperlink = f'=HYPERLINK("{google_maps_link}", "{name}")'
        row.append(hyperlink)

        # Construct link using coordinate values
        coordinates = f'{row[1]},{row[0]}'  # Assuming longitude is in the first column (index 0), latitude is in the second column (index 1)
        coordinates_link = f'https://www.google.com/maps/search/?api=1&query={coordinates}'

        # Add the simplified hyperlink to the row
        coordinates_hyperlink = f'=HYPERLINK("{coordinates_link}", "x")'

        # Append the second hyperlink to the row
        row.append(coordinates_hyperlink)

        # Add the blank Description column
        row.insert(3, '')

        # Remove Latitude, Longitude, and Layer columns
        del row[0]  # Latitude
        del row[0]  # Longitude
        del row[2]

        # Add the row to the corresponding layer's data
        layer_data[layer].append(row)

# Dictionary for location names
location_names = {
    'Layer 000000': 'Tokyo',
    'Layer 0288D1': 'Hakone',
    'Layer 880E4F': 'Sapporo',
    'Layer 006064': 'Daytrips',
    'Layer C2185B': 'Kyoto&Nara',
    'Layer E65100': 'Accommodations',
    'Layer FFEA00': 'Osaka',
    'Layer BDBDBD': 'Hiroshima',
    'Layer 0F9D58': 'Hakodate+',
    'Layer': 'Test'
}

# Column headers
column_headers = ['Activity', 'Description', 'Link!', 'Coords', '¥¥¥', 'Notes', '', 'J', 'T', 'A', 'S', 'C', 'F']

# Write separate TXT files for each layer
for layer, data in layer_data.items():
    print(layer)
    location_name = location_names.get(layer, 'Unknown')
    if location_name == 'Unknown':
        print(layer)
        break
    txt_filename = f'{output_folder}/{location_name}.txt'
    with open(txt_filename, 'w', encoding='utf-8', newline='') as txt_file:
        # Write the column headers
        txt_file.write('\t'.join(column_headers) + '\n')

        for row in data:
            # Write the row data
            txt_file.write('\t'.join(row) + '\n')

    print(f'Successfully created {txt_filename}.')

print('Separation into separate TXT files completed.')