import os
from PIL import Image
from PIL.ExifTags import TAGS

# Configuration
IMAGE_DIR = 'content/images/rallies/2005'
OUTPUT_FILE = 'content/archive/rallies/2005/index.md'
SITE_URL_PREFIX = '{static}/images/rallies/2005/'

def get_exif_data(image_path):
    """Extract basic EXIF data (Date, Camera Model) if available."""
    exif_info = {}
    try:
        image = Image.open(image_path)
        exif_raw = image._getexif()
        if exif_raw:
            for tag, value in exif_raw.items():
                decoded = TAGS.get(tag, tag)
                if decoded == 'DateTimeOriginal':
                    exif_info['Date'] = value
                elif decoded == 'Model':
                    exif_info['Camera'] = value
    except Exception as e:
        print(f"Error reading EXIF for {image_path}: {e}")
    return exif_info

def generate_markdown():
    # Header
    markdown_content = f"""Title: 2005 Rally
Date: 2005-01-01
Slug: archive/rallies/2005
Save_as: archive/rallies/2005/index.html
URL: archive/rallies/2005/index.html

# 2005 Rally Archive

Explore the photos from the 2005 Rally.

<div class="gallery-grid">
"""

    # Process Images
    files = sorted([f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
    
    for filename in files:
        file_path = os.path.join(IMAGE_DIR, filename)
        exif = get_exif_data(file_path)
        
        # Cleanup metadata display
        date_str = exif.get('Date', 'Unknown Date')
        camera_str = exif.get('Camera', '')
        meta_display = f"{date_str}"
        if camera_str:
            meta_display += f" | {camera_str}"
            
        # Title from filename (remove extension, replace underscores)
        title = os.path.splitext(filename)[0].replace('_', ' ').title()

        # HTML Block for Gallery Item
        gallery_item = f"""
    <div class="gallery-item" data-src="{SITE_URL_PREFIX}{filename}">
        <img src="{SITE_URL_PREFIX}{filename}" alt="{title}" loading="lazy">
        <div class="gallery-caption">{title}</div>
        <div class="gallery-metadata">{meta_display}</div>
    </div>
"""
        markdown_content += gallery_item

    # Footer
    markdown_content += """
</div>

<script src="{filename}/theme/static/js/lightbox.js"></script>
"""

    with open(OUTPUT_FILE, 'w') as f:
        f.write(markdown_content)
    
    print(f"Gallery generated at {OUTPUT_FILE} with {len(files)} images.")

if __name__ == "__main__":
    generate_markdown()
