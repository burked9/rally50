import os
import glob
import re
try:
    import pymupdf as fitz
except ImportError:
    try:
        import fitz
    except ImportError:
        print("Error: PyMuPDF is not installed. Please run: pip install pymupdf")
        exit(1)

# Configuration
RAW_BROCHURES_DIR = "raw_brochures"
OUTPUT_DIR = "content/images/brochures"
TARGET_PAGES = [1, 3, 4, 6]  # 1-indexed for human readability (page 1 is index 0)
DPI = 150  # Resolution for extraction (adjust for quality/size tradeoff)

def extract_highlights():
    if not os.path.exists(RAW_BROCHURES_DIR):
        print(f"Directory '{RAW_BROCHURES_DIR}' not found. Please create it and add PDFs.")
        return

    pdf_files = glob.glob(os.path.join(RAW_BROCHURES_DIR, "*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in '{RAW_BROCHURES_DIR}'.")
        return

    print(f"Found {len(pdf_files)} PDF brochures to process...")

    for pdf_path in pdf_files:
        filename = os.path.basename(pdf_path)
        # Try to extract the year from the filename (e.g. "1985.pdf" -> "1985")
        year_match = re.search(r'(19\d{2}|20\d{2})', filename)
        if not year_match:
            print(f"Skipping '{filename}': Could not find a year in the filename.")
            continue
            
        year_str = year_match.group(1)
        
        # Ensure output directory exists for this year
        year_out_dir = os.path.join(OUTPUT_DIR, year_str)
        os.makedirs(year_out_dir, exist_ok=True)
        
        print(f"\nProcessing brochure for {year_str}...")
        
        try:
            doc = fitz.open(pdf_path)
            total_pages = len(doc)
            
            for target_page_num in TARGET_PAGES:
                page_idx = target_page_num - 1
                
                # Check if page exists in document
                if page_idx < 0 or page_idx >= total_pages:
                    print(f"  - Skipping Page {target_page_num} (document only has {total_pages} pages)")
                    continue
                    
                output_file = os.path.join(year_out_dir, f"page_{target_page_num}.png")
                
                # Render page to an image
                page = doc.load_page(page_idx)
                # Set resolution (DPI)
                zoom = DPI / 72.0 
                mat = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=mat)
                
                # Save as PNG
                pix.save(output_file)
                print(f"  + Extracted Page {target_page_num} -> {output_file}")
                
            doc.close()
        except Exception as e:
            print(f"Error processing '{filename}': {e}")
            
    print("\nExtraction complete! The Eras Gallery will now automatically pick up these PNGs.")

if __name__ == "__main__":
    extract_highlights()
