import csv
import json

def parse_data():
    output = []
    with open('content/data/all_winners_template.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            output.append(dict(row))
    return output

if __name__ == "__main__":
    data = parse_data()
    # Write to a JS file that sets a global variable
    js_content = "var trophyData = " + json.dumps(data, indent=4) + ";"
    
    with open("theme/static/js/winners_data.js", "w") as f:
        f.write(js_content)
        
    print("Generated winners_data.js")
