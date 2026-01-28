import os

# Configuration
BASE_DIR = 'content/archive/rallies'
INDEX_FILE = os.path.join(BASE_DIR, 'index.md')

# Rally Logic
# 1975 = Rally 1
# 1979 = No Rally
# 1980 = Rally 5
# ...
# 2019 = Rally 44
# 2020 = No Rally
# 2021 = No Rally
# 2022 = Rally 45
# ...
# 2027 = Rally 50

rallies = []

# Loop years 1975 to 2027
formatted_list = []

rally_num = 0
for year in range(1975, 2028):
    if year == 1979:
        # No rally
        continue
    elif year in [2020, 2021]:
        # No rally
        continue
    else:
        # Determine rally number
        if year < 1979:
            rally_num = year - 1974
        elif year < 2020:
            rally_num = year - 1975 # 1980 is 5
        else:
            # 2022 is 45
            # year - x = 45 => 2022 - x = 45 => x = 1977
            rally_num = year - 1977

    formatted_list.append({'year': year, 'rally_num': rally_num})

def generate_pages():
    for item in formatted_list:
        year = item['year']
        num = item['rally_num']
        
        dir_path = os.path.join(BASE_DIR, str(year))
        file_path = os.path.join(dir_path, 'index.md')
        
        # Skip if 2005 already exists (preserve our gallery)
        if year == 2005 and os.path.exists(file_path):
            print(f"Skipping 2005 (Preserving existing content)")
            continue

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            
        if not os.path.exists(file_path):
            content = f"""Title: {year} Rally (No. {num})
Date: {year}-01-01
Slug: archive/rallies/{year}
Save_as: archive/rallies/{year}/index.html
URL: archive/rallies/{year}/index.html

# {year} Rally (No. {num})

## Photos
*No photos yet.*

## Documents
*No documents yet.*
"""
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created {year}")

def update_index():
    # Sort reverse chronological
    sorted_rallies = sorted(formatted_list, key=lambda x: x['year'], reverse=True)
    
    content = """Title: Rallies Archive
Date: 2024-01-28
Slug: archive/rallies
Save_as: archive/rallies/index.html
URL: archive/rallies/index.html

# Rallies Archive

Explore the history of the rally year by year.

<div class="l-post-stack">
"""
    
    for item in sorted_rallies:
        year = item['year']
        num = item['rally_num']
        # Link using {filename} which now resolves to the fixed URL
        link = f"{{filename}}/archive/rallies/{year}/index.md"
        
        content += f"""
    <div class="post-stack-item">
        <h3 class="h4"><a href="{link}">{year} Rally (No. {num})</a></h3>
    </div>
"""
    content += "</div>"
    
    with open(INDEX_FILE, 'w') as f:
        f.write(content)
    print("Updated Rallies Index")

if __name__ == "__main__":
    generate_pages()
    update_index()
