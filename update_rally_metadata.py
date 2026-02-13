import csv
import json
import os
import argparse

def update_metadata(year):
    # Define file paths
    csv_filename = f"Rally_{year}_Metadata.xlsx - PHOTO_CAPTIONS.csv"
    json_filename = f"rally_{year}.json"
    
    csv_file = os.path.join('content', 'data', csv_filename)
    json_file = os.path.join('content', 'data', json_filename)

    data = []

    # Check if CSV file exists
    if not os.path.exists(csv_file):
        print(f"Error: CSV file not found at {csv_file}")
        return

    try:
        with open(csv_file, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert "TRUE"/"FALSE" strings to actual Booleans if 'Unknown' key exists
                if 'Unknown' in row:
                    row['Unknown'] = row['Unknown'].upper() == 'TRUE'
                data.append(row)

        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        print(f"Successfully created {json_file} from {csv_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update Rally JSON metadata from CSV.")
    parser.add_argument("year", help=" The year of the rally to update (e.g., 2024)")
    args = parser.parse_args()

    update_metadata(args.year)
