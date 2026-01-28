document.addEventListener('DOMContentLoaded', () => {
    // Create Lightbox Elements
    const lightbox = document.createElement('div');
    lightbox.id = 'lightbox';
    lightbox.className = 'lightbox';

    const closeBtn = document.createElement('span');
    closeBtn.className = 'lightbox-close';
    closeBtn.innerHTML = '&times;';

    const img = document.createElement('img');
    img.className = 'lightbox-content';

    const caption = document.createElement('div');
    caption.className = 'lightbox-caption';

    lightbox.appendChild(closeBtn);
    lightbox.appendChild(img);
    lightbox.appendChild(caption);
    document.body.appendChild(lightbox);

    // Add Event Listeners to Gallery Items
    const items = document.querySelectorAll('.gallery-item');
    items.forEach(item => {
        item.addEventListener('click', () => {
            const thumbnail = item.querySelector('img');
            const hiResSrc = item.getAttribute('data-src') || thumbnail.src;
            const capText = item.querySelector('.gallery-caption')?.innerText || '';
            const metaText = item.querySelector('.gallery-metadata')?.innerText || '';

            img.src = hiResSrc;
            caption.innerHTML = `<strong>${capText}</strong><br><span style="font-size:0.9rem; opacity:0.8">${metaText}</span>`;
            lightbox.classList.add('active');
        });
    });

    // Close Lightbox
    closeBtn.addEventListener('click', () => {
        lightbox.classList.remove('active');
    });

    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            lightbox.classList.remove('active');
        }
    });
});
