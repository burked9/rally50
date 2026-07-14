import os
import subprocess

def process_and_get_html(img_path, target_dir, lightbox_group, title_func):
    filename = os.path.basename(img_path)
    base_name = os.path.splitext(filename)[0]
    
    jpg_path = os.path.join(target_dir, f"{base_name}.jpg")
    thumb_path = os.path.join(target_dir, f"{base_name}_thumb.jpg")
    
    # Convert HEIC to JPG
    subprocess.run(["sips", "-s", "format", "jpeg", img_path, "--out", jpg_path], check=True, capture_output=True)
    # Create thumbnail
    subprocess.run(["sips", "-Z", "600", jpg_path, "--out", thumb_path], check=True, capture_output=True)
    
    # Generate title
    title = title_func(base_name)
    
    # Relative paths for HTML
    rel_jpg = f"{{filename}}/{os.path.relpath(jpg_path, 'content')}"
    rel_thumb = f"{{filename}}/{os.path.relpath(thumb_path, 'content')}"
    
    html = f"""    <a href="{rel_jpg}" class="gallery-item" data-lightbox="{lightbox_group}" data-title="{title}">
        <img src="{rel_thumb}" alt="{title}">
        <div class="gallery-caption">{title}</div>
    </a>"""
    return html

def inject_html(md_path, html_blocks, marker):
    with open(md_path, 'r') as f:
        content = f.read()
    if marker in content:
        content = content.replace(marker, marker + "\n" + "\n".join(html_blocks))
        with open(md_path, 'w') as f:
            f.write(content)
        print(f"Injected into {md_path}")
    else:
        print(f"Marker {marker} not found in {md_path}")

def nice_title(name):
    # E.g. rally45_card -> Rally 45 Card
    # rally13_barge_race_prize_ChangSha -> Rally 13 Barge Race Prize Changsha
    name = name.replace('_', ' ')
    name = name.title()
    # Add space after Rally if it's immediately followed by a number
    import re
    name = re.sub(r'Rally(\d+)', r'Rally \1', name)
    return name

# 1. Misc Artefacts
misc_dir = "content/images/misc"
misc_md = "content/archive/artifacts/misc/index.md"
misc_html = []
for f in sorted(os.listdir(misc_dir)):
    if f.lower().endswith('.heic'):
        html = process_and_get_html(os.path.join(misc_dir, f), misc_dir, "misc", nice_title)
        misc_html.append(html)
        os.remove(os.path.join(misc_dir, f))
if misc_html:
    inject_html(misc_md, misc_html, 'id="misc-grid">\n    <!-- Items will be added here as images are provided -->')

# 2. Dinner Dance
dd_dir = "content/images/dinner-dance"
dd_md = "content/archive/artifacts/dinner-dance/index.md"
dd_html = []
for f in sorted(os.listdir(dd_dir)):
    if f.lower().endswith('.heic'):
        html = process_and_get_html(os.path.join(dd_dir, f), dd_dir, "dinner-dance", nice_title)
        dd_html.append(html)
        os.remove(os.path.join(dd_dir, f))
if dd_html:
    inject_html(dd_md, dd_html, 'id="dinner-dance-grid">\n    <!-- Items will be added here as images are provided -->')

# 3. Prizes
prize_dir = "content/images/prizes"
prize_md = "content/archive/artifacts/plaques/index.md"
prize_html = []
for f in sorted(os.listdir(prize_dir)):
    if f.lower().endswith('.heic'):
        html = process_and_get_html(os.path.join(prize_dir, f), prize_dir, "prizes", nice_title)
        prize_html.append(html)
        os.remove(os.path.join(prize_dir, f))
if prize_html:
    inject_html(prize_md, prize_html, 'id="prize-plaques-grid">\n    <!-- Prize plaques will be added here -->')

# 4. Mugs
mug_dir = "content/images/rallies/2026"
mug_md = "content/archive/artifacts/rally-mugs/index.md"
mug_html = []
for f in sorted(os.listdir(mug_dir)):
    if f.lower().endswith('.heic') and 'mug' in f.lower():
        html = process_and_get_html(os.path.join(mug_dir, f), mug_dir, "mugs", lambda n: "Rally 49 (2026)")
        mug_html.append(html)
        os.remove(os.path.join(mug_dir, f))
if mug_html:
    inject_html(mug_md, mug_html, '<!-- Items will be added here -->')

print("All new artifacts processed!")
