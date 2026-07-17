#!/bin/bash

mkdir -p content/images/thumbnails

# Loop over all image types
for img in content/images/*.jpg content/images/*.jpeg content/images/*.png content/images/*.heic; do
    # Check if the file exists (in case a glob doesn't match anything)
    if [ -f "$img" ]; then
        filename=$(basename "$img")
        name="${filename%.*}"
        
        # Don't create thumbnails of thumbnails or placeholder images if they exist
        if [[ "$name" == *"_thumbnail"* ]] || [[ "$name" == *"placeholder"* ]]; then
            echo "Skipping $filename"
            continue
        fi

        echo "Processing $filename..."
        sips -Z 600 -s format jpeg "$img" --out "content/images/thumbnails/${name}.jpg"
    fi
done

echo "Thumbnails generated successfully!"
