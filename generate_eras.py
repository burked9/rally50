import os
import json
import random
import re

# Configuration
ERAS_DIR = 'content/archive/eras'
DATA_DIR = 'content/data'
RALLIES_IMG_DIR = 'content/images/rallies'
BROCHURES_IMG_DIR = 'content/images/brochures'
TEMPLATE_FILE = 'theme/templates/eras_index.html'
INDEX_MD_FILE = os.path.join(ERAS_DIR, 'index.md')

# Brochure data from parse_brochures.py (manually integrated here)
BROCHURES_RAW = [
  { "name": "Derg Rally 01", "id": "0B4ubLJPS0mdTSmk3b25PUmlrbFU" },
  { "name": "Derg Rally 02", "id": "0B4ubLJPS0mdTMnNzS0lXTy1FQWM" },
  { "name": "Derg Rally 03", "id": "0B4ubLJPS0mdTbWRBTndEeW43ekk" },
  { "name": "Derg Rally 04", "id": "0B4ubLJPS0mdTWE5uR3FMaWVUNWc" },
  { "name": "Derg Rally 05", "id": "0B4ubLJPS0mdTTzc4eC1jXzU0QVU" },
  { "name": "Derg Rally 06", "id": "0B4ubLJPS0mdTcmFheWphX1ZZUjQ" },
  { "name": "Derg Rally 07", "id": "0B4ubLJPS0mdTeklUc0FZQXJjVEU" },
  { "name": "Derg Rally 08", "id": "0B4ubLJPS0mdTYUl5ckdvWnlFZHc" },
  { "name": "Derg Rally 09", "id": "0B4ubLJPS0mdTZTZaeVVGMjFJR2s" },
  { "name": "Derg Rally 10", "id": "0B4ubLJPS0mdTZ2FrVXhoVHV5ejQ" },
  { "name": "Derg Rally 11", "id": "0B4ubLJPS0mdTMDhPNktIQVZueXM" },
  { "name": "Derg Rally 12", "id": "0B4ubLJPS0mdTaVo1NW5sQnNPbFk" },
  { "name": "Derg Rally 13", "id": "0B4ubLJPS0mdTU1dUbnd0Q2pjb1k" },
  { "name": "Derg Rally 14", "id": "0B4ubLJPS0mdTeHR4NThVd2sxS0U" },
  { "name": "Derg Rally 15", "id": "0B4ubLJPS0mdTVEdpMXFqNjhTbmc" },
  { "name": "Derg Rally 16", "id": "0B4ubLJPS0mdTN29uckVick1UeUk" },
  { "name": "Derg Rally 17", "id": "0B4ubLJPS0mdTQ0ZHdVBlOGlpbkU" },
  { "name": "Derg Rally 18", "id": "0B4ubLJPS0mdTemRxa29EN3hKX1E" },
  { "name": "Derg Rally 19", "id": "0B4ubLJPS0mdTQXlhel9XNG0tUHc" },
  { "name": "Derg Rally 20", "id": "0B4ubLJPS0mdTVHJDalF2Wi1zYmc" },
  { "name": "Derg Rally 21", "id": "0B4ubLJPS0mdTMTYwUTM2MVNWVnM" },
  { "name": "Derg Rally 22", "id": "0B4ubLJPS0mdTSzdwMjhrbEFId2c" },
  { "name": "Derg Rally 23", "id": "0B4ubLJPS0mdTZUpCSkRCWE04Vkk" },
  { "name": "Derg Rally 24", "id": "0B4ubLJPS0mdTTXR4RXMtSmhfWXc" },
  { "name": "Derg Rally 25", "id": "0B4ubLJPS0mdTMy14eG4wNkxVM3c" },
  { "name": "Derg Rally 26", "id": "0B4ubLJPS0mdTTUhQSklPTjZvSk0" },
  { "name": "Derg Rally 27", "id": "0B4ubLJPS0mdTWWFaakR5QUstRlU" },
  { "name": "Derg Rally 28", "id": "0B4ubLJPS0mdTUWpRS3haTks5NXc" },
  { "name": "Derg Rally 29", "id": "0B4ubLJPS0mdTc3FXaVBkNXlVZzA" },
  { "name": "Derg Rally 30", "id": "0B4ubLJPS0mdTMmFUOC16d2dkcEE" },
  { "name": "Derg Rally 31", "id": "0B4ubLJPS0mdTYlpVSmRtMWp5ekU" },
  { "name": "Derg Rally 32", "id": "0B4ubLJPS0mdTajl1WWNXbWc3MVU" },
  { "name": "Derg Rally 33", "id": "0B4ubLJPS0mdTWDVEeFlSSGNqLUE" },
  { "name": "Derg Rally 34", "id": "0B4ubLJPS0mdTREwxejdpckV4X2c" },
  { "name": "Derg Rally 35", "id": "0B4ubLJPS0mdTWHUtTlVtWEpOTFU" },
  { "name": "Derg Rally 36", "id": "0B4ubLJPS0mdTTGdXazVtbVNXYjA" },
  { "name": "Derg Rally 37", "id": "0B4ubLJPS0mdTMFZNaHcySWhOWmc" },
  { "name": "Derg Rally 38", "id": "0B4ubLJPS0mdTTmROUlBGTHpFbGc" },
  { "name": "Derg Rally 39", "id": "0B4ubLJPS0mdTY05IQ3BaR2dpQ3c" },
  { "name": "Derg Rally 40", "id": "0B4ubLJPS0mdTTFFWMUZzalJtaDg" },
  { "name": "Derg Rally 41", "id": "0B4ubLJPS0mdTRGZMLTlYSUNIaG8" },
  { "name": "Derg Rally 42", "id": "1e9QjP4ojAxLjnj2m_nmTnvkDyisMOtHr" },
  { "name": "Derg Rally 43", "id": "1YI7sgI0LnIK91tf6X_M9hELcCHhdF0SV" },
  { "name": "Derg Rally 44", "id": "1vEz4SuCDEkr4Q28cl4cCw7quWwzK-dzH" },
]

# Map rally numbers to brochure IDs
brochure_map = {}
for b in BROCHURES_RAW:
    match = re.search(r'\d+', b['name'])
    if match:
        num = int(match.group(0))
        brochure_map[num] = b['id']


# Rally Logic
rallies = []
for year in range(1975, 2028):
    if year == 1979 or year in [2020, 2021]:
        continue
        
    if year < 1979:
        rally_num = year - 1974
    elif year < 2020:
        rally_num = year - 1975
    else:
        rally_num = year - 1977
        
    rallies.append({'year': year, 'num': rally_num})


# Group into Eras (buckets of 5 rallies)
eras = []
for i in range(0, len(rallies), 5):
    bucket = rallies[i:i+5]
    if not bucket:
        continue
    
    first_rally = bucket[0]
    last_rally = bucket[-1]
    
    era_num = (i // 5) + 1
    
    eras.append({
        'era_num': era_num,
        'title': f"Rallies {first_rally['num']} - {last_rally['num']} ({first_rally['year']} - {last_rally['year']})",
        'bucket': bucket
    })

# Reverse the eras so newest appears first
eras.reverse()

def resolve_md_url(md_rel_path):
    """Resolve the generated HTML URL from a markdown file's frontmatter."""
    full_path = os.path.join('content', md_rel_path.lstrip('/'))
    url = None
    slug = None
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            for line in f:
                line_s = line.strip()
                if not line_s:
                    break
                if line_s.lower().startswith('url:'):
                    url = line_s.split(':', 1)[1].strip()
                elif line_s.lower().startswith('slug:'):
                    slug = line_s.split(':', 1)[1].strip()
    if url:
        return '/' + url.lstrip('/')
    if slug:
        return '/' + slug.lstrip('/') + '.html'
    return '/' + md_rel_path.lstrip('/').replace('.md', '.html')

def parse_people_items():
    """Parse included subsections of content/archive/people/index.md and group by rally number."""
    people_md_path = 'content/archive/people/index.md'
    included_sections = {
        'Our Commodores',
        'Rally Memories',
        'Rally Committees',
        'Rally Photo Collages',
        'Snippets & Snapshots'
    }
    by_rally = {}
    if not os.path.exists(people_md_path):
        return by_rally

    with open(people_md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split by ## headings
    sections = re.split(r'^##\s+(.+)$', text, flags=re.MULTILINE)
    # sections[0] is preamble, then pairs of (heading, body)
    for i in range(1, len(sections), 2):
        heading = sections[i].strip()
        body = sections[i + 1]
        if heading not in included_sections:
            continue

        # Find all <a ...>...</a> blocks
        anchors = re.findall(r'<a\s+([^>]+)>(.*?)</a>', body, flags=re.DOTALL)
        for attrs, inner in anchors:
            href_m = re.search(r'href="([^"]+)"', attrs)
            img_m = re.search(r'<img\s+[^>]*src="([^"]+)"', inner)
            cap_m = re.search(r'<div class="gallery-caption">(.*?)</div>', inner, flags=re.DOTALL)
            if not (href_m and img_m and cap_m):
                continue

            raw_href = href_m.group(1).strip()
            raw_img = img_m.group(1).strip()
            caption = cap_m.group(1).strip()

            # Match first Rally number in caption
            rally_m = re.search(r'Rally\s+(\d+)', caption, flags=re.IGNORECASE)
            if not rally_m:
                continue
            rally_num = int(rally_m.group(1))

            # Resolve href
            is_image = True
            if raw_href.startswith('{filename}'):
                rel_md = raw_href.replace('{filename}', '')
                resolved_href = resolve_md_url(rel_md)
                is_image = False
            else:
                resolved_href = raw_href.replace('{static}', '')

            resolved_thumb = raw_img.replace('{static}', '').replace('{filename}', '')

            by_rally.setdefault(rally_num, []).append({
                'title': caption,
                'section': heading,
                'href': resolved_href,
                'thumb': resolved_thumb,
                'is_image': is_image
            })

    return by_rally

def generate_era_pages():
    people_by_rally = parse_people_items()

    for era in eras:
        era_num = era['era_num']
        dir_path = os.path.join(ERAS_DIR, str(era_num))
        file_path = os.path.join(dir_path, 'index.md')
        
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            
        content = f"""Title: Era {era_num}: {era['title']}
Date: 2024-01-01
Slug: archive/eras/{era_num}
Save_as: archive/eras/{era_num}/index.html
URL: archive/eras/{era_num}/index.html
Template: era_dynamic

## Overview
A curated look back at {era['title']}.
"""
        with open(file_path, 'w') as f:
            f.write(content)
        
        # Now generate the JSON payload for this era
        era_data = {
            "title": era['title'],
            "years": []
        }
        
        for r in era['bucket']:
            year = r['year']
            num = r['num']
            
            year_data = {
                "year": year,
                "rally_num": num,
                "photos": [],
                "photo_count": 0,
                "brochure_id": brochure_map.get(num, None),
                "artifacts": [],
                "brochure_pages": [],
                "people_items": people_by_rally.get(num, [])
            }
            
            # Scan for artifacts
            year_rallies_dir = os.path.join(RALLIES_IMG_DIR, str(year))
            if os.path.exists(year_rallies_dir):
                for f in sorted(os.listdir(year_rallies_dir)):
                    if f.lower().endswith(('.png', '.jpg', '.jpeg')) and not f.endswith('_thumb.png') and not f.endswith('_thumb.jpg'):
                        year_data['artifacts'].append(f)
                        
            # Scan for brochure pages
            year_brochures_dir = os.path.join(BROCHURES_IMG_DIR, str(year))
            if os.path.exists(year_brochures_dir):
                for f in sorted(os.listdir(year_brochures_dir)):
                    if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                        year_data['brochure_pages'].append(f)
            
            # Look for photos
            json_file = os.path.join(DATA_DIR, f'rally_{year}.json')
            if os.path.exists(json_file):
                try:
                    with open(json_file, 'r') as f:
                        photos = json.load(f)
                    
                    if photos:
                        year_data["photo_count"] = len(photos)
                        for p in photos:
                            year_data["photos"].append({
                                "id": p.get("id"),
                                "alt": p.get("alt", f"Rally {year}")
                            })
                except Exception as e:
                    print(f"Error reading {json_file}: {e}")
            
            era_data["years"].append(year_data)
            
        # Write JSON for era
        era_json_path = os.path.join(DATA_DIR, f'era_{era_num}.json')
        with open(era_json_path, 'w') as f:
            json.dump(era_data, f, indent=4)
        
        print(f"Generated Era {era_num}")

def generate_eras_index():
    if not os.path.exists(ERAS_DIR):
        os.makedirs(ERAS_DIR)
        
    content = """Title: Eras & Decades
Date: 2024-01-29
Slug: archive/eras
Save_as: archive/eras/index.html
URL: archive/eras/index.html
Template: eras_gallery

"""
    with open(INDEX_MD_FILE, 'w') as f:
        f.write(content)
    print(f"Updated {INDEX_MD_FILE}")
    
    # Generate the template for the Eras gallery index
    template_content = """{% extends "page.html" %}

{% block content %}
<style>
/* Full width override */
main {
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
}
.era-container {
    width: 100%;
    max-width: 100%;
    padding: 0 40px;
    margin: 0;
}
</style>
<div class="era-container">
    <div class="entry-content">
        <p>A curated journey through time. Explore highlights and brochures grouped in 5-year chapters.</p>

        <style>
        .era-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
            margin-top: 30px;
        }
        @media (max-width: 900px) {
            .era-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 600px) {
            .era-grid { grid-template-columns: 1fr; }
        }
        
        .era-card {
            background: #fff;
            border: 1px solid #eee;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex;
            flex-direction: column;
            text-decoration: none !important;
            color: inherit;
        }
        
        .era-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        }
        
        .era-thumb {
            width: 100%;
            height: 180px;
            object-fit: cover;
            background-color: #f4f4f4;
            border-bottom: 1px solid #eee;
        }
        
        .era-info {
            padding: 20px;
            text-align: center;
        }
        
        .era-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #222;
            margin-bottom: 5px;
            display: block;
        }
        </style>

        <div class="era-grid">
"""
    
    for era in eras:
        link = f"{{{{ SITEURL }}}}/archive/eras/{era['era_num']}/index.html"
        img = f"{{{{ SITEURL }}}}/images/category_historical.png"
        
        template_content += f"""
            <a href="{link}" class="era-card">
                <img src="{img}" class="era-thumb" alt="Era {era['era_num']}">
                <div class="era-info">
                    <span class="era-title">{era['title']}</span>
                </div>
            </a>
"""

    template_content += """
        </div>
    </div>
</div>
{% endblock %}
"""
    
    with open('theme/templates/eras_gallery.html', 'w') as f:
        f.write(template_content)
    print("Generated theme/templates/eras_gallery.html")

if __name__ == "__main__":
    generate_era_pages()
    generate_eras_index()
