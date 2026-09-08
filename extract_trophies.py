import csv
import re
import os
# Import the columns definition from the existing script
try:
    from parse_winners import columns
except ImportError:
    # Fallback if import fails (e.g. environment issues), but it should work
    columns = [
        {"id": "rally", "name": "Rally No."},
        {"id": "year", "name": "Year"},
        {"id": "estemaid", "name": "Estemaid Trophy (Committee Prize)"},
        {"id": "boyle", "name": "Boyle Trophy (Barge Race)"},
        {"id": "benjamin", "name": "Benjamin Cup (Recovery)"},
        {"id": "nm_barge", "name": "NM Barge Trophy (Hand)"},
        {"id": "wynn_juba", "name": "Wynn Juba Cup (Orienteering)"},
        {"id": "jj_kineally", "name": "JJ Kineally Cup (Overall Team)"},
        {"id": "friendship", "name": "Friendship Cup"},
        {"id": "bob_hughes", "name": "Bob Hughes Trophy (Boat Inspection)"},
        {"id": "ann_clarke", "name": "Ann Clarke Cup (Jr Friendship)"},
        {"id": "newman", "name": "Newman Cup (Surprise Inspection)"},
        {"id": "jimmy_leyden", "name": "Jimmy Leyden Trophy (Best Endeavour)"},
        {"id": "dennis_byrne", "name": "Dennis Byrne Cup (Best Newcomer)"},
        {"id": "finton_harold", "name": "Finton Harold Cup (Line Heaving Mens)"},
        {"id": "mccormack", "name": "McCormack Plate (Line Heaving Womens)"},
        {"id": "dennis_juba", "name": "Dennis Juba Cup (Man Over Board)"},
        {"id": "westpark", "name": "Westpark Cup (Boat Handling)"},
        {"id": "eric_timon", "name": "Eric Timon Ditty Cup"},
        {"id": "tavern", "name": "Tavern Cup (Time Trial)"},
        {"id": "scarriff", "name": "Scarriff Shield (Barge Handling)"},
        {"id": "jh_stimpson", "name": "JH Stimpson Cup (Sailing)"},
        {"id": "benson", "name": "Benson Shield (Young Bosun)"}
    ]

# Ensure directory exists
output_dir = 'content/data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file = os.path.join(output_dir, 'trophies.csv')

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Header requested: Trophy Name, Competition, Slug
    writer.writerow(['Trophy Name', 'Competition', 'Slug'])

    count = 0
    for col in columns:
        slug = col['id']
        # Skip the non-trophy columns
        if slug in ['rally', 'year']:
            continue

        full_name = col['name']

        # Regex to separate "Trophy Name (Competition Name)"
        # Matches anything followed by optional space and parenthesized text
        match = re.match(r"(.*?)\s*\((.*?)\)$", full_name)
        
        if match:
            trophy_name = match.group(1).strip()
            competition = match.group(2).strip()
        else:
            trophy_name = full_name.strip()
            competition = "" # No parentheses found

        writer.writerow([trophy_name, competition, slug])
        count += 1

print(f"Successfully created {output_file} with {count} trophies.")
