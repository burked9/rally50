Title: 2023 Rally (No. 46)
Date: 2023-01-01
Slug: archive/rallies/2023
Save_as: archive/rallies/2023/index.html
URL: archive/rallies/2023/index.html

## Photos

<div id="rally-46-gallery" class="gallery-grid"></div>

<style>
  .gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 15px;
    padding: 20px;
  }
  .gallery-item {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    cursor: pointer;
  }
  .gallery-item:hover {
    transform: scale(1.03);
  }
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('rally-46-gallery');

    // Fetch the photo data from the JSON file
    fetch('/data/rally46_photos.json')
        .then(response => response.json())
        .then(rally46Photos => {
            rally46Photos.forEach(photo => {
                // Generate the URL for a large thumbnail (w1000 is good for viewing)
                const imgUrl = `https://drive.google.com/thumbnail?id=${photo.id}&sz=w1000`;
                const fullUrl = `https://drive.google.com/uc?export=view&id=${photo.id}`;

                const imgElement = `
                    <a href="${fullUrl}" target="_blank">
                        <img class="gallery-item" 
                             src="${imgUrl}" 
                             alt="${photo.alt}" 
                             loading="lazy">
                    </a>
                `;
                container.innerHTML += imgElement;
            });
        })
        .catch(error => console.error('Error loading gallery data:', error));
});
</script>

## Documents
*No documents yet.*
