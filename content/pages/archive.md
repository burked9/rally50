Title: The Rally 50 Archive
Date: 2024-01-28
Slug: archive
Template: page

Welcome to the digital archive of the IWAI Lough Derg Rally. Here you will find a treasure trove of history, memories, and artifacts from the past 50 years.

<style>
.archive-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    margin-top: 40px;
    margin-bottom: 40px;
}
.archive-widget {
    background: #fff;
    border: 1px solid #eaeaea;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
    color: inherit;
}
.archive-widget:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}
.archive-widget img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-bottom: 1px solid #eaeaea;
}
.archive-widget-content {
    padding: 24px;
}
.archive-widget h3 {
    margin-top: 0;
    margin-bottom: 10px;
    font-size: 1.5rem;
    color: #222;
}
.archive-widget p {
    margin: 0;
    color: #555;
    font-size: 0.95rem;
    line-height: 1.4;
}
</style>

<div class="archive-grid">
    <!-- Eras Widget -->
    <a href="{filename}/archive/eras/index.md" class="archive-widget">
        <img src="{filename}/images/category_historical.png" alt="Eras & Decades">
        <div class="archive-widget-content">
            <h3>Eras & Decades</h3>
            <p>A curated journey through time. Explore highlights and brochures grouped in 5-year chapters.</p>
        </div>
    </a>

    <!-- Rallies Widget -->
    <a href="{filename}/archive/rallies/index.md" class="archive-widget">
        <img src="{filename}/images/rallies_placeholder.png" alt="Rallies">
        <div class="archive-widget-content">
            <h3>All Rallies</h3>
            <p>The complete archive. Explore every unedited photo gallery from rallies past, organized by individual year.</p>
        </div>
    </a>

    <!-- Artifacts Widget -->
    <a href="{filename}/archive/artifacts/index.md" class="archive-widget">
        <img src="{filename}/images/artifacts_placeholder.png" alt="Artifacts">
        <div class="archive-widget-content">
            <h3>Artifacts</h3>
            <p>View our physical collection of plaques, trophies, tankards, tickets, and flags.</p>
        </div>
    </a>

    <!-- People Widget -->
    <a href="{filename}/archive/people/index.md" class="archive-widget">
        <img src="{filename}/images/people/snippets/derg_perpetual_cup_rally24.jpg" alt="People">
        <div class="archive-widget-content">
            <h3>People</h3>
            <p>Remembering those who made the rally, including commodores, memorials, and Hall of Fame.</p>
        </div>
    </a>
</div>

**More to come, potentially select articles published in Magazines**
