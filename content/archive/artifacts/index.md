Title: Artifacts
Date: 2024-01-28
Slug: archive/artifacts
Save_as: archive/artifacts/index.html
URL: archive/artifacts/index.html
Summary: A collection of various artifacts from the Rally history.

Welcome to the Artifacts Archive. Explore our collection of historical items below.

<div class="artifact-grid">
    <a href="{filename}/archive/artifacts/winners.md" class="artifact-tile">
        <div class="tile-image" style="background-image: url('{filename}/images/trophy_cup.png');"></div>
        <h3>Hall of Fame</h3>
    </a>
    
    <a href="{filename}/archive/artifacts/plaques/index.md" class="artifact-tile">
        <div class="tile-image" style="background-image: url('{filename}/images/rallies/2012/plaque.png');"></div>
        <h3>Rally Plaques</h3>
    </a>

    <a href="{filename}/archive/artifacts/rally-mugs/index.md" class="artifact-tile">
        <div class="tile-image" style="background-image: url('{filename}/images/rallies/2002/mug.jpg');"></div>
        <h3>Rally Mugs</h3>
    </a>

    <a href="{filename}/archive/artifacts/pookas/index.md" class="artifact-tile">
        <div class="tile-image" style="background-image: url('{filename}/images/pookas/pooka_1.jpg');"></div>
        <h3>Pookas</h3>
    </a>
    
    <a href="{filename}/archive/artifacts/commodores-tankards/index.md" class="artifact-tile">
        <div class="tile-image" style="background-image: url('{filename}/images/commodores_tankard_placeholder.png');"></div>
        <h3>Commodores Tankards</h3>
    </a>

     <a href="{filename}/archive/artifacts/flags/index.md" class="artifact-tile">
        <div class="tile-image" style="background-image: url('{filename}/images/rally_flag_placeholder.png');"></div>
        <h3>Flags</h3>
    </a>

    <a href="{filename}/archive/magazines/index.md" class="artifact-tile">
        <div class="tile-image" style="background-image: url('{filename}/images/archive/magazines/kingfisher.png');"></div>
        <h3>Magazine Articles</h3>
    </a>

    <a href="{filename}/archive/artifacts/brochures.md" class="artifact-tile">
        <div class="tile-image" style="background-image: url('{filename}/images/rally_placeholder.png');"></div>
        <h3>Rally Brochures</h3>
    </a>
</div>

<style>
    .artifact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 30px;
        margin-top: 40px;
    }

    .artifact-tile {
        display: flex;
        flex-direction: column;
        text-decoration: none;
        color: var(--color-text);
        border: 1px solid #eee;
        border-radius: 8px;
        overflow: hidden;
        transition: transform 0.2s, box-shadow 0.2s;
        background: #fff;
    }

    .artifact-tile:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        text-decoration: none;
    }

    .tile-image {
        width: 100%;
        height: 180px;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        border-bottom: 1px solid #f0f0f0;
    }

    .artifact-tile h3 {
        margin: 15px;
        font-size: 1.1rem;
        text-align: center;
        color: var(--primary-color);
    }
</style>
