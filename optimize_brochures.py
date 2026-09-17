import os
import glob
from PIL import Image

BROCHURES_DIR = "content/images/brochures"
MAX_WIDTH = 800

def optimize_images():
    png_files = glob.glob(os.path.join(BROCHURES_DIR, "**", "*.png"), recursive=True)
    print(f"Found {len(png_files)} PNG files to optimize.")
    
    for png_path in png_files:
        try:
            with Image.open(png_path) as img:
                # Convert to RGB to save as JPEG (discard alpha)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                    
                # Resize if wider than MAX_WIDTH
                if img.width > MAX_WIDTH:
                    ratio = MAX_WIDTH / float(img.width)
                    new_height = int(float(img.height) * float(ratio))
                    img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
                
                jpg_path = os.path.splitext(png_path)[0] + ".jpg"
                img.save(jpg_path, "JPEG", quality=85, optimize=True)
                
            # Delete original PNG
            os.remove(png_path)
            print(f"Optimized: {os.path.basename(jpg_path)}")
        except Exception as e:
            print(f"Error optimizing {png_path}: {e}")

    # Clean up empty directories
    for root, dirs, files in os.walk(BROCHURES_DIR, topdown=False):
        for name in dirs:
            try:
                dir_path = os.path.join(root, name)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    print(f"Removed empty directory: {dir_path}")
            except Exception as e:
                pass

if __name__ == "__main__":
    optimize_images()
