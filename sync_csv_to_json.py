import json
import csv
import os

# Configuration
pairs = [
    ('content/data/rally_2023.json', 'rally_2023_metadata.csv'),
    ('content/data/rally_2024.json', 'rally_2024_metadata.csv')
]

for json_path, csv_path in pairs:
    if not os.path.exists(csv_path):
        print(f"CSV {csv_path} not found, skipping.")
        continue

    print(f"Syncing {csv_path} -> {json_path}...")
    
    # Read CSV Data into a dictionary keyed by Filename
    csv_data = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # key by Filename. 
            # Note: The JSON 'alt' usually holds the filename.
            key = row['Filename'].strip()
            if key:
                csv_data[key] = row
    
    # Load JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        json_items = json.load(f)
    
    # Update JSON items
    updated_count = 0
    for item in json_items:
        # Match by 'alt' (which holds the filename) or 'id' if filename fallback was used
        # Our generator used 'alt' or f"ID_{id}"
        
        lookup_key = item.get('alt', '').strip()
        if not lookup_key:
             lookup_key = f"ID_{item.get('id')}"
             
        if lookup_key in csv_data:
            metadata = csv_data[lookup_key]
            
            # Update fields
            item['Caption'] = metadata.get('Caption', '')
            item['People'] = metadata.get('People', '')
            item['Boat'] = metadata.get('Boat', '')
            item['Location'] = metadata.get('Location', '')
            item['Category'] = metadata.get('Category', '')
            item['Memory_Story'] = metadata.get('Memory_Story', '')
            
            # Handle Unknown Flag (normalize to boolean or string "TRUE")
            unknown_val = metadata.get('Unknown', '').strip().upper()
            item['Unknown'] = (unknown_val == 'TRUE' or unknown_val == 'YES')
            
            updated_count += 1
            
    # Save JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_items, f, indent=4)
        
    print(f"Updated {updated_count} items in {json_path}.")

# --- Post-Sync: Generate Count Manifest ---
print("\nGenerating photo_counts.json manifest...")
counts = {}
data_dir = 'content/data'

for filename in os.listdir(data_dir):
    if filename.startswith('rally_') and filename.endswith('.json'):
        # Extract year from rally_YYYY.json
        try:
            year = filename.replace('rally_', '').replace('.json', '')
            # year must be 4 digits
            if len(year) == 4 and year.isdigit():
                filepath = os.path.join(data_dir, filename)
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    counts[year] = len(data)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

output_path = os.path.join(data_dir, 'photo_counts.json')
with open(output_path, 'w') as f:
    json.dump(counts, f, indent=4)
    
print(f"Manifest created: {output_path} with {len(counts)} years.")
