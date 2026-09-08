import json
import csv
import random

# Configuration
data_sources = {
    'rally_2023': 'content/data/rally_2023.json',
    'rally_2024': 'content/data/rally_2024.json'
}

columns = ['Filename', 'Caption', 'People', 'Boat', 'Location', 'Category', 'Unknown', 'Memory_Story']

# Generic data for demonstration
sample_names = ["Gerry Burke", "Matt McGrory", "Emily Moore", "Liam Power", "Sarah Brislane"]
sample_boats = ["68M", "Lady Diva", "Carna Bay", "Reflection", "Affaja"]
sample_locs = ["Mountshannon", "Terryglass", "Portumna", "Kilgarvan"]
sample_cats = ["Social", "Handling", "Sailing", "Junior"]

for rally_name, json_path in data_sources.items():
    output_file = f'{rally_name}_metadata.csv'
    
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            
        # Sort by alt (filename), handling empty alts
        data.sort(key=lambda x: x.get('alt', ''))
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()

            for i, item in enumerate(data):
                filename = item.get('alt')
                if not filename:
                    filename = f"ID_{item.get('id')}" # Fallback if no filename, though unlikely for most

                # Populate first 5 rows with sample data for the committee
                if i < 5:
                    row = {
                        'Filename': filename,
                        'Caption': f"Sample entry for {rally_name}",
                        'People': random.choice(sample_names),
                        'Boat': random.choice(sample_boats),
                        'Location': random.choice(sample_locs),
                        'Category': random.choice(sample_cats),
                        'Unknown': "FALSE",
                        'Memory_Story': "This is a placeholder for a funny story or memory about this day."
                    }
                else:
                    # Rest are blank for volunteers
                    row = {col: "" for col in columns}
                    row['Filename'] = filename
                    row['Unknown'] = "TRUE" # Default to true for unknown photos

                writer.writerow(row)
        
        print(f"Created {output_file} with {len(data)} entries.")

    except FileNotFoundError:
        print(f"File {json_path} not found.")
