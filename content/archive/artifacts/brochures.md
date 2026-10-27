Title: Rally Brochures and Magazines
Date: 2024-01-28
Slug: archive/artifacts/brochures
Save_as: archive/artifacts/brochures/index.html
URL: archive/artifacts/brochures/index.html

Browse through the digital collection of rally brochures from the past. Click on a cover to view the full PDF.

<div id="magazine-grid"></div>

<script>
// Data: List of Rally Magazines
const magazines = [
    {
        "name": "Derg Rally 01",
        "id": "1hJhY54jR-8p8cMKKosr_zxLMXDJQ2I-1"
    },
    {
        "name": "Derg Rally 02",
        "id": "0B4ubLJPS0mdTMnNzS0lXTy1FQWM"
    },
    {
        "name": "Derg Rally 03",
        "id": "0B4ubLJPS0mdTbWRBTndEeW43ekk"
    },
    {
        "name": "Derg Rally 04",
        "id": "0B4ubLJPS0mdTWE5uR3FMaWVUNWc"
    },
    {
        "name": "Derg Rally 05",
        "id": "0B4ubLJPS0mdTTzc4eC1jXzU0QVU"
    },
    {
        "name": "Derg Rally 06",
        "id": "0B4ubLJPS0mdTcmFheWphX1ZZUjQ"
    },
    {
        "name": "Derg Rally 07",
        "id": "0B4ubLJPS0mdTeklUc0FZQXJjVEU"
    },
    {
        "name": "Derg Rally 08",
        "id": "0B4ubLJPS0mdTYUl5ckdvWnlFZHc"
    },
    {
        "name": "Derg Rally 09",
        "id": "0B4ubLJPS0mdTZTZaeVVGMjFJR2s"
    },
    {
        "name": "Derg Rally 10",
        "id": "0B4ubLJPS0mdTZ2FrVXhoVHV5ejQ"
    },
    {
        "name": "Derg Rally 11",
        "id": "0B4ubLJPS0mdTMDhPNktIQVZueXM"
    },
    {
        "name": "Derg Rally 12",
        "id": "0B4ubLJPS0mdTaVo1NW5sQnNPbFk"
    },
    {
        "name": "Derg Rally 13",
        "id": "0B4ubLJPS0mdTU1dUbnd0Q2pjb1k"
    },
    {
        "name": "Derg Rally 14",
        "id": "0B4ubLJPS0mdTeHR4NThVd2sxS0U"
    },
    {
        "name": "Derg Rally 15",
        "id": "0B4ubLJPS0mdTVEdpMXFqNjhTbmc"
    },
    {
        "name": "Derg Rally 16",
        "id": "0B4ubLJPS0mdTN29uckVick1UeUk"
    },
    {
        "name": "Derg Rally 17",
        "id": "0B4ubLJPS0mdTQ0ZHdVBlOGlpbkU"
    },
    {
        "name": "Derg Rally 18",
        "id": "0B4ubLJPS0mdTemRxa29EN3hKX1E"
    },
    {
        "name": "Derg Rally 19",
        "id": "0B4ubLJPS0mdTQXlhel9XNG0tUHc"
    },
    {
        "name": "Derg Rally 20",
        "id": "0B4ubLJPS0mdTVHJDalF2Wi1zYmc"
    },
    {
        "name": "Derg Rally 21",
        "id": "0B4ubLJPS0mdTMTYwUTM2MVNWVnM"
    },
    {
        "name": "Derg Rally 22",
        "id": "0B4ubLJPS0mdTSzdwMjhrbEFId2c"
    },
    {
        "name": "Derg Rally 23",
        "id": "0B4ubLJPS0mdTZUpCSkRCWE04Vkk"
    },
    {
        "name": "Derg Rally 24",
        "id": "0B4ubLJPS0mdTTXR4RXMtSmhfWXc"
    },
    {
        "name": "Derg Rally 25",
        "id": "0B4ubLJPS0mdTMy14eG4wNkxVM3c"
    },
    {
        "name": "Derg Rally 26",
        "id": "0B4ubLJPS0mdTTUhQSklPTjZvSk0"
    },
    {
        "name": "Derg Rally 27",
        "id": "0B4ubLJPS0mdTWWFaakR5QUstRlU"
    },
    {
        "name": "Derg Rally 28",
        "id": "0B4ubLJPS0mdTUWpRS3haTks5NXc"
    },
    {
        "name": "Derg Rally 29",
        "id": "0B4ubLJPS0mdTc3FXaVBkNXlVZzA"
    },
    {
        "name": "Derg Rally 30",
        "id": "0B4ubLJPS0mdTMmFUOC16d2dkcEE"
    },
    {
        "name": "Derg Rally 31",
        "id": "0B4ubLJPS0mdTYlpVSmRtMWp5ekU"
    },
    {
        "name": "Derg Rally 32",
        "id": "0B4ubLJPS0mdTajl1WWNXbWc3MVU"
    },
    {
        "name": "Derg Rally 33",
        "id": "0B4ubLJPS0mdTWDVEeFlSSGNqLUE"
    },
    {
        "name": "Derg Rally 34",
        "id": "0B4ubLJPS0mdTREwxejdpckV4X2c"
    },
    {
        "name": "Derg Rally 35",
        "id": "0B4ubLJPS0mdTWHUtTlVtWEpOTFU"
    },
    {
        "name": "Derg Rally 36",
        "id": "0B4ubLJPS0mdTTGdXazVtbVNXYjA"
    },
    {
        "name": "Derg Rally 37",
        "id": "0B4ubLJPS0mdTMFZNaHcySWhOWmc"
    },
    {
        "name": "Derg Rally 38",
        "id": "0B4ubLJPS0mdTTmROUlBGTHpFbGc"
    },
    {
        "name": "Derg Rally 39",
        "id": "0B4ubLJPS0mdTY05IQ3BaR2dpQ3c"
    },
    {
        "name": "Derg Rally 40",
        "id": "0B4ubLJPS0mdTTFFWMUZzalJtaDg"
    },
    {
        "name": "Derg Rally 41",
        "id": "0B4ubLJPS0mdTRGZMLTlYSUNIaG8"
    },
    {
        "name": "Derg Rally 42",
        "id": "1e9QjP4ojAxLjnj2m_nmTnvkDyisMOtHr"
    },
    {
        "name": "Derg Rally 43",
        "id": "1YI7sgI0LnIK91tf6X_M9hELcCHhdF0SV"
    },
    {
        "name": "Derg Rally 44",
        "id": "1vEz4SuCDEkr4Q28cl4cCw7quWwzK-dzH"
    }
];

const grid = document.getElementById('magazine-grid');

magazines.forEach(mag => {
    // Generate the URL for the first page thumbnail
    const thumbUrl = `https://drive.google.com/thumbnail?id=${mag.id}&sz=w400`;
    // Generate the URL to view the PDF
    const viewUrl = `https://drive.google.com/file/d/${mag.id}/view?usp=sharing`;

    const card = `
        <div class="mag-card">
            <a href="${viewUrl}" target="_blank">
                <img src="${thumbUrl}" alt="${mag.name}" loading="lazy">
                <p>${mag.name}</p>
            </a>
        </div>
    `;
    grid.innerHTML += card;
});
</script>

<style>
    /* Expand page container so 5 columns fit comfortably and stay centered */
    main, .l-measure, .l-container, .entry-content {
        max-width: 1200px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }
    #magazine-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 24px;
        justify-content: center;
        margin: 40px auto 0 auto;
        max-width: 1150px;
    }
    .mag-card {
        width: calc((100% - 96px) / 5);
        min-width: 170px;
        max-width: 210px;
        text-align: center;
        font-family: sans-serif;
    }
    .mag-card a {
        text-decoration: none;
        color: inherit;
        display: block;
    }
    .mag-card img {
        width: 100%;
        height: 260px;
        object-fit: cover;
        border: 1px solid #ddd;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        border-radius: 4px;
        transition: transform 0.2s, box-shadow 0.2s;
        background: #f8f8f8;
    }
    .mag-card p {
        margin-top: 10px;
        font-weight: bold;
        font-size: 0.95rem;
        color: #1D2545;
    }
    /* Subtle hover effect for the magazines */
    .mag-card img:hover {
        transform: translateY(-4px) scale(1.03);
        border-color: #004a99;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    }
</style>
