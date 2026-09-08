import os
import glob
import shutil
import re

src_dir = "/Users/danielburke/Library/CloudStorage/OneDrive-Personal/work/RALLY50/plaques/rallyplaques/converted"
dest_base = "/Users/danielburke/Documents/repositories/Projects/rally50/content/images/rallies"
md_file = "/Users/danielburke/Documents/repositories/Projects/rally50/content/archive/artifacts/plaques/index.md"

# 1. Delete existing holding files
for ext in ["png", "jpg", "jpeg"]:
    for filepath in glob.glob(f"{dest_base}/*/plaque.{ext}"):
        os.remove(filepath)
        print(f"Removed {filepath}")

# 2. Copy and rename new files, track years
years = []
for filename in os.listdir(src_dir):
    if filename.endswith(".png"):
        src_path = os.path.join(src_dir, filename)
        year_str = filename.split("_")[-1].replace(".png", "")
        year = int(year_str)
        years.append(year)
        
        dest_dir = os.path.join(dest_base, str(year))
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, "plaque.png")
        
        shutil.copy2(src_path, dest_path)
        print(f"Copied {filename} to {dest_path}")

years.sort()

# 3. Generate HTML
html_lines = ['<div class="gallery-grid">', '    <!-- Items will be added here -->']
for year in years:
    rally_num = year - 1975
    html_lines.append(f'    <a href="{{filename}}/images/rallies/{year}/plaque.png" class="gallery-item" data-lightbox="plaques" data-title="Rally {rally_num} ({year})">')
    html_lines.append(f'        <img src="{{filename}}/images/rallies/{year}/plaque.png" alt="Rally {rally_num} Plaque">')
    html_lines.append(f'        <div class="gallery-caption">Rally {rally_num} ({year})</div>')
    html_lines.append(f'    </a>')
html_lines.append('</div>')

new_html = "\n".join(html_lines)

# 4. Update index.md
with open(md_file, "r") as f:
    content = f.read()

pattern = re.compile(r'<div class="gallery-grid">.*?</div>', re.DOTALL)
new_content = pattern.sub(new_html, content)

with open(md_file, "w") as f:
    f.write(new_content)

print("Markdown updated successfully.")
