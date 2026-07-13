Title: Rally Flags
Date: 2024-01-29
Slug: archive/artifacts/flags
Save_as: archive/artifacts/flags/index.html
URL: archive/artifacts/flags/index.html
Summary: Archive of historical flags from the Lough Derg Rally.

Welcome to the Rally Flags archive. Below is a collection of the beautiful flags that have flown over the Lough Derg Rally over the years.

<div class="gallery-grid" id="flags-grid">
    <!-- Flag items will be added here as images are provided -->
</div>

<style>
    .gallery-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 15px;
        margin-top: 30px;
    }
    @media (min-width: 600px) {
        .gallery-grid {
            grid-template-columns: repeat(3, 1fr);
        }
    }
    @media (min-width: 1024px) {
        .gallery-grid {
            grid-template-columns: repeat(4, 1fr);
        }
    }
    .gallery-item {
        display: flex;
        flex-direction: column;
        text-decoration: none;
        color: inherit;
        background: #fff;
        border: 1px solid #eee;
        border-radius: 8px;
        padding: 10px;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .gallery-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        text-decoration: none;
    }
    .gallery-item img {
        width: 100%;
        height: 200px;
        object-fit: contain;
        margin-bottom: 10px;
    }
    .gallery-caption {
        text-align: center;
        font-weight: 500;
        color: #333;
    }
</style>
