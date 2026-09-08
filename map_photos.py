import json
import re
from difflib import get_close_matches

# 1. Load Photos
with open('content/data/trophy_photos_raw.json', 'r') as f:
    photos = json.load(f)

# Filter empty entries
photos = [p for p in photos if p['alt'].strip()]

# 2. Define Slugs (from extracted list or manually known)
# I'll just define the map of "Slug" -> "Search Terms"
slugs = {
    'jj_kineally': 'Kenneally',
    'jimmy_leyden': 'Leyden',
    'friendship': 'Friendship',
    'ann_clarke': 'Anne Clarke',
    'estemaid': 'Eistemaid', # or Estemaid
    'church_bay': 'Church Bay',
    'boyle': 'Boyle',
    'scarriff': 'Scarriff',
    'nm_barge': 'New Metal Barge', # or NM
    'dennis_byrne': 'Dennis Byrne', # or Denis
    'westpark': 'Westpark',
    'wynn_juba': 'Wynn Juba',
    'tavern': 'Tavern',
    'dennis_juba': 'Dennis Juba', # or Denis
    'benjamin': 'Benjamin',
    'bob_hughes': 'Hughes Perpetual',
    'newman': 'Newman',
    'jh_stimpson': 'Stimpson',
    'eric_timon': 'Timon Ditty',
    'finton_harold': 'Harold',
    'mccormack': 'McCormack',
    'benson': 'Benson',
    'derg_cup': 'Derg',
    'goosander': 'Goosander',
    'sean_kenny': 'Sean Kenny',
    'oconnor': 'O\'Connor'
}

matches = {}
unmatched_photos = []

print("--- Matching Photos ---")
for photo in photos:
    filename = photo['alt']
    # Removing extension and basics
    clean_name = filename.lower().replace(' copy.jpg', '').replace('(i)', '').replace('.jpg', '').strip()
    
    found = False
    for slug, term in slugs.items():
        if term.lower() in clean_name:
            matches[slug] = photo
            print(f"MATCH: {slug} -> {filename}")
            found = True
            break
            
    if not found:
        # Try harder?
        unmatched_photos.append(filename)

print(f"\nMatched: {len(matches)}/{len(photos)}")
if unmatched_photos:
    print("\nUnmatched Photos:")
    for p in unmatched_photos:
        print(p)

# Save the map
with open('content/data/trophy_photo_map.json', 'w') as f:
    json.dump(matches, f, indent=4)
