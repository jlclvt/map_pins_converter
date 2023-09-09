import os
import shutil
import subprocess
import sys

def main(kmz_file):
    # Run kmz_to_csv.py to convert KMZ to CSV
    csv_file = 'input.csv'
    subprocess.run([sys.executable, 'kmz_to_csv.py', kmz_file, csv_file])

    
    # Run csv_cleanup.py to process the CSV file and generate TXT files
    subprocess.run([sys.executable, 'csv_cleanup.py', csv_file])

    # Delete the CSV file
    if os.path.exists(csv_file):
        os.remove(csv_file)

    # Delete the KML file
    kml_file = 'doc.kml'
    if os.path.exists(kml_file):
        os.remove(kml_file)

# Specify the KMZ file path
kmz_file = 'locations.kmz'

# Call the main function
main(kmz_file)
