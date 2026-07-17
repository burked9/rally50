import json
import csv
import re

def create_csv():
    with open('content/js/winners_data.js', 'r') as f:
        js_content = f.read()

    # Extract the JSON array
    match = re.search(r'var trophyData = (\[.*?\]);', js_content, re.DOTALL)
    if not match:
        print("Could not find trophyData in winners_data.js")
        return

    json_str = match.group(1)
    
    # Clean up potential trailing commas
    json_str = re.sub(r',\s*}', '}', json_str)
    json_str = re.sub(r',\s*\]', ']', json_str)

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
        return

    # Defined ordered keys from the JS file + new trophies like church_bay
    all_keys = [
        "rally", "year", "estemaid", "boyle", "benjamin", "nm_barge", 
        "wynn_juba", "jj_kineally", "friendship", "bob_hughes", "ann_clarke", 
        "newman", "jimmy_leyden", "dennis_byrne", "finton_harold", "mccormack", 
        "dennis_juba", "westpark", "eric_timon", "tavern", "scarriff", 
        "jh_stimpson", "benson", "church_bay", "derg_cup", "goosander", "oconnor"
    ]

    keys_in_data = set()
    for row in data:
        keys_in_data.update(row.keys())

    header = ['rally', 'year'] + [k for k in all_keys if k not in ['rally', 'year']] + \
             [k for k in keys_in_data if k not in all_keys and k not in ['rally', 'year']]

    # Missing rallies from 49 down to 40 (plus COVID years)
    missing_rallies = [
        {"rally": "49", "year": "2026"},
        {"rally": "48", "year": "2025"},
        {"rally": "47", "year": "2024"},
        {"rally": "46", "year": "2023"},
        {"rally": "45", "year": "2022"},
        {"rally": "-", "year": "2021", "friendship": "No Rally (COVID)"},
        {"rally": "-", "year": "2020", "friendship": "No Rally (COVID)"},
        {"rally": "44", "year": "2019"},
        {"rally": "43", "year": "2018"},
        {"rally": "42", "year": "2017"},
        {"rally": "41", "year": "2016"},
        {"rally": "40", "year": "2015"},
    ]

    for mr in missing_rallies:
        for k in header:
            if k not in mr:
                mr[k] = ""

    final_data = missing_rallies + data

    csv_path = 'content/data/all_winners_template.csv'
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for row in final_data:
            row_out = {k: row.get(k, "") for k in header}
            writer.writerow(row_out)

    print(f"Successfully created {csv_path}")

if __name__ == "__main__":
    create_csv()
