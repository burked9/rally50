import os
from PIL import Image

dest_base = "/Users/danielburke/Documents/repositories/Projects/rally50/content/images/rallies"
md_file = "/Users/danielburke/Documents/repositories/Projects/rally50/content/archive/artifacts/plaques/index.md"

years = []
for d in os.listdir(dest_base):
    if d.isdigit():
        if os.path.exists(os.path.join(dest_base, d, "plaque.png")):
            years.append(int(d))

years.sort()

html_lines = ['<div class="gallery-grid">']

for year in years:
    # Calculate rally number
    if year <= 2019:
        rally_num = year - 1975
    else:
        # 2020 and 2021 were cancelled, so 2022 is 45
        rally_num = year - 1977
    
    # Generate thumbnail
    src_img = os.path.join(dest_base, str(year), "plaque.png")
    thumb_img = os.path.join(dest_base, str(year), "plaque_thumb.png")
    
    print(f"Processing {year}...")
    with Image.open(src_img) as img:
        # Resize to max 600px height or width to save size while keeping quality reasonable
        img.thumbnail((600, 600))
        img.save(thumb_img, optimize=True)
        
    html_lines.append(f'    <a href="{{filename}}/images/rallies/{year}/plaque.png" class="gallery-item" data-lightbox="plaques" data-title="Rally {rally_num} ({year})">')
    html_lines.append(f'        <img src="{{filename}}/images/rallies/{year}/plaque_thumb.png" alt="Rally {rally_num} Plaque">')
    html_lines.append(f'        <div class="gallery-caption">Rally {rally_num} ({year})</div>')
    html_lines.append(f'    </a>')

html_lines.append('</div>')

new_html = "\n".join(html_lines)

# Write the exact correct index.md structure (clean replacement of the entire file)
new_md = f"""Title: Rally Plaques
Date: 2024-01-28
Slug: archive/artifacts/plaques
Save_as: archive/artifacts/plaques/index.html
URL: archive/artifacts/plaques/index.html
Summary: Archive of Rally Plaques.

{new_html}

<style>
    .gallery-grid {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 15px;
    }}
    @media (min-width: 600px) {{
        .gallery-grid {{
            grid-template-columns: repeat(3, 1fr);
        }}
    }}
    .gallery-item img {{
        height: 130px;
        object-fit: contain;
    }}
</style>
"""

with open(md_file, "w") as f:
    f.write(new_md)

print("Thumbnails generated and Markdown fully rewritten successfully.")
