Title: Artifacts
Date: 2024-01-28
Slug: archive/artifacts
Save_as: archive/artifacts/index.html
URL: archive/artifacts/index.html
Summary: A collection of various artifacts from the Rally history.

Welcome to the Artifacts Archive. Explore our collection of historical items below.

<div class="artifact-grid">
    <a href="{filename}/archive/artifacts/winners.md" class="artifact-tile">
        <img src="{filename}/images/trophy_cup.png" alt="Hall of Fame" class="tile-image">
        <h3>Hall of Fame</h3>
    </a>
    
    <a href="{filename}/archive/artifacts/brochures.md" class="artifact-tile">
        <img src="{filename}/images/rally_brochure_thumbnail.jpg" alt="Rally Brochures" class="tile-image">
        <h3>Rally Brochures</h3>
    </a>

    <a href="{filename}/archive/artifacts/plaques/index.md" class="artifact-tile">
        <img src="{filename}/images/rallies/1993/plaque_thumb.png" alt="Rally Plaques" class="tile-image">
        <h3>Rally Plaques</h3>
    </a>

    <a href="{filename}/archive/artifacts/rally-mugs/index.md" class="artifact-tile">
        <img src="{filename}/images/rallies/2002/mug.jpg" alt="Rally Mugs" class="tile-image">
        <h3>Rally Mugs</h3>
    </a>

    <a href="{filename}/archive/artifacts/pookas/index.md" class="artifact-tile">
        <img src="{filename}/images/pookas/Pooka41m_thumb.jpg" alt="Pookas" class="tile-image" style="object-position: top;">
        <h3>Pookas</h3>
    </a>
    
    <a href="{filename}/archive/artifacts/commodores-tankards/index.md" class="artifact-tile">
        <img src="{filename}/images/commodores_tankard_placeholder.png" alt="Commodores Tankards" class="tile-image">
        <h3>Commodores Tankards</h3>
    </a>

     <a href="{filename}/archive/artifacts/flags/index.md" class="artifact-tile">
        <img src="{filename}/images/flags/burgee_rally39_thumb.jpg" alt="Flags" class="tile-image">
        <h3>Flags</h3>
    </a>

    <a href="{filename}/archive/magazines/index.md" class="artifact-tile">
        <img src="{filename}/images/archive/magazines/kingfisher.png" alt="Magazine Articles" class="tile-image">
        <h3>Magazine Articles</h3>
    </a>

    <a href="{filename}/archive/artifacts/commodores-plaques/index.md" class="artifact-tile">
        <img src="{filename}/images/commodores_tankard_placeholder.png" alt="Commodores Plaques" class="tile-image">
        <h3>Commodores Plaques</h3>
    </a>

    <a href="{filename}/archive/artifacts/misc/index.md" class="artifact-tile">
        <img src="{filename}/images/rally_flag_placeholder.png" alt="Misc Artefacts" class="tile-image">
        <h3>Misc Artefacts</h3>
    </a>

    <a href="{filename}/archive/artifacts/dinner-dance/index.md" class="artifact-tile">
        <img src="{filename}/images/rally_flag_placeholder.png" alt="Dinner Dance Artefacts" class="tile-image">
        <h3>Dinner Dance Artefacts</h3>
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
        object-fit: cover;
        display: block;
        border-bottom: 1px solid #f0f0f0;
    }

    .artifact-tile h3 {
        margin: 15px;
        font-size: 1.1rem;
        text-align: center;
        color: var(--primary-color);
    }
</style>
