import os
import shutil

# Configuration
BASE_DIR = 'content/archive/rallies'
INDEX_MD_FILE = os.path.join(BASE_DIR, 'index.md')
TEMPLATE_FILE = 'theme/templates/rallies_gallery.html'

# Rally Logic
formatted_list = []
for year in range(1975, 2028):
    if year == 1979 or year in [2020, 2021]:
        continue
        
    if year < 1979:
        rally_num = year - 1974
    elif year < 2020:
        rally_num = year - 1975
    else:
        rally_num = year - 1977
        
    formatted_list.append({'year': year, 'num': rally_num})

# Sort reverse chronological (newest first)
formatted_list.sort(key=lambda x: x['year'], reverse=True)

def generate_pages():
    for item in formatted_list:
        year = item['year']
        num = item['num']
        
        dir_path = os.path.join(BASE_DIR, str(year))
        file_path = os.path.join(dir_path, 'index.md')
        
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            
        # Standard content for ALL years.
        # The dynamic template handles checking for JSON data.
        content = f"""Title: {year} Rally (No. {num})
Date: {year}-01-01
Slug: archive/rallies/{year}
Save_as: archive/rallies/{year}/index.html
URL: archive/rallies/{year}/index.html
Template: rally_dynamic

## Documents
*No documents yet.*
"""
        # Always overwrite to ensure latest template usage
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Generated {year}")

def generate_gallery_template():
    # We will generate a Template that contains the card grid.
    # We embed the list of rallies directly into the template (simpler than passing via metadata context in many cases).
    
    template_content = """{% extends "page.html" %}

{% block content %}
<div class="l-container">
    <div class="entry-content">
        <p>Explore the history of the Lough Derg Rally, year by year. Dive into the archives to find photos, brochures, and memories.</p>

        <style>
        /* Reusing/Adapting the Grid Styles */
        .rally-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 24px;
            margin-top: 30px;
        }
        
        .rally-card {
            background: #fff;
            border: 1px solid #eee;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex;
            flex-direction: column;
            text-decoration: none !important; /* Override default link underline */
            color: inherit;
        }
        
        .rally-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        }
        
        .rally-thumb {
            width: 100%;
            height: 160px;
            object-fit: cover;
            background-color: #f4f4f4;
            border-bottom: 1px solid #eee;
        }
        
        .rally-info {
            padding: 20px;
            text-align: center;
        }
        
        .rally-year {
            font-size: 1.5rem;
            font-weight: 700;
            color: #222;
            margin-bottom: 5px;
            display: block;
        }
        
        .rally-num {
            font-size: 0.9rem;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        </style>

        <div class="rally-grid">
"""
    
    # Loop through rallies to create cards
    for r in formatted_list:
        year = r['year']
        num = r['num']
        # Use simple relative path which works because all rallies are at archive/rallies/{year}/index.html
        # Note: In Pelican templates, {{ SITEURL }} is available.
        link = f"{{{{ SITEURL }}}}/archive/rallies/{year}/index.html"
        img = f"{{{{ SITEURL }}}}/images/rally_placeholder.png"
        
        template_content += f"""
            <a href="{link}" class="rally-card">
                <img src="{img}" class="rally-thumb" alt="Rally {year}">
                <div class="rally-info">
                    <span class="rally-year">{year}</span>
                    <span class="rally-num">Rally No. {num}</span>
                </div>
            </a>
"""

    template_content += """
        </div>
    </div>
</div>
{% endblock %}
"""
    
    with open(TEMPLATE_FILE, 'w') as f:
        f.write(template_content)
    print(f"Generated {TEMPLATE_FILE}")

def update_index_md():
    content = """Title: Rallies Archive
Date: 2024-01-29
Slug: archive/rallies
Save_as: archive/rallies/index.html
URL: archive/rallies/index.html
Template: rallies_gallery

"""
    with open(INDEX_MD_FILE, 'w') as f:
        f.write(content)
    print(f"Updated {INDEX_MD_FILE} to use rallies_gallery template")

if __name__ == "__main__":
    generate_pages()
    generate_gallery_template()
    update_index_md()
