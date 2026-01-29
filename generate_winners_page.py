# Trophy Definitions with Categories and Descriptions
trophies = [
    # Premier
    {"id": "jj_kineally", "name": "JJ Kenneally Perpetual Challenge Cup", "category": "premier", "image": "trophy_cup.png", 
     "desc": "This cup was presented by the well-known Limerick jeweller, JJ Kenneally, in the early years of the rally. JJ was a great supporter of the branch and for many years his shop window in Wickham Street, Limerick, displayed all the rally trophies for the week prior to the rally. This is the premier rally trophy and is awarded to the overall winning team of the rally."},
    
    # Meaning / Spirit
    {"id": "jimmy_leyden", "name": "The Jimmy Leyden Perpetual Trophy", "category": "spirit", "image": "trophy_shield.png",
     "desc": "Presented to the branch in memory of Jimmy Leydon. Jimmy was a founder member of the branch and a regular rally goer. This shield is awarded for 'Best Endeavour' and the recipient is chosen by the Commodore of the rally."},
    {"id": "friendship", "name": "Friendship Cup", "category": "spirit", "image": "trophy_cup.png",
     "desc": "Presented to the branch by the Northern Ireland Branch of the IWAI in 2002. This cup is awarded to the person who receives the most nominations from fellow ralliers for representing the spirit of the rally."},
    {"id": "ann_clarke", "name": "Anne Clarke Trophy", "category": "spirit", "image": "trophy_cup.png",
     "desc": "Presented to the branch by the Clarke family. Awarded to the young person who best represents the 'Spirit of the Rally' (Junior Friendship)."},
    {"id": "estemaid", "name": "The Eistemaid Trophy", "category": "spirit", "image": "trophy_cup.png",
     "desc": "Presented to the branch by Fr. Paddy Dowling, a founder member of the branch. This is a competition for committee members only and is usually held on the morning after the dinner dance!"},
     
    # Newcomer
    {"id": "dennis_byrne", "name": "The Denis Byrne Cup", "category": "newcomer", "image": "trophy_cup.png",
     "desc": "Presented to the branch by David Knight and Frank Van Den Berg in memory of Denis Byrne. Denis was a young man who lived in Whitegate and worked with David and Frank on their boats. He was a regular rally goer until his untimely death in a car accident. This cup is awarded to the winner of the 'First Mate' boat handling competition."},
    {"id": "church_bay", "name": "The Church Bay Cup", "category": "newcomer", "image": "trophy_cup.png",
     "desc": "Presented to the branch in 2018 by the Burke family in memory of Billy and Moira Burke. Awarded to the 'Best Newcomer' to the rally."},

    # Barges
    {"id": "boyle", "name": "The Boyle Trophy", "category": "barge", "image": "trophy_barge.png",
     "desc": "Presented to the branch by Chris Boyle in 1986. At that time, many members were beginning to restore old canal boats (barges) and Chris presented the trophy to encourage barge owners to enter the rally. It is awarded to the winner of the Barge Race."},
    {"id": "scarriff", "name": "The Scarriff Perpetual Shield", "category": "barge", "image": "trophy_barge.png",
     "desc": "Presented to the branch by Dan McInerney, owner of the 60M (Scalpa). It is awarded for Barge Handling – Heritage."},
    {"id": "nm_barge", "name": "New Metal Barge Trophy", "category": "barge", "image": "trophy_barge.png",
     "desc": "Presented to the branch for the winner of the Barge Handling competition for modern-built barges."},

    # Skills / Technical
    {"id": "westpark", "name": "The Westpark Cup", "category": "skill", "image": "trophy_cup.png",
     "desc": "The Westpark Hotel in Portumna was the base for many a rally in the 1980s. The owners presented this cup to the branch to be awarded to the winner of the Boat Handling competition."},
    {"id": "wynn_juba", "name": "The Wynn Juba Perpetual Cup", "category": "skill", "image": "trophy_cup.png",
     "desc": "Presented by Denis and Wynn Juba from Leicester, England. Denis and Wynn were regular rally goers in the 1980s and 90s. This cup is awarded to the winner of the Orienteering competition."},
    {"id": "tavern", "name": "The Tavern Cup", "category": "skill", "image": "trophy_cup.png",
     "desc": "Marty Mara, owner of The Tavern in Ballinderry, presented this cup to the branch. It is awarded to the winner of the Time Trial."},
    {"id": "dennis_juba", "name": "The Denis Juba Perpetual Cup", "category": "skill", "image": "trophy_cup.png",
     "desc": "Awarded to the winner of the Man Overboard competition."},
    {"id": "benjamin", "name": "The Benjamin Cup", "category": "skill", "image": "trophy_cup.png",
     "desc": "This cup was originally intended for Rally One, but as that rally was cancelled in 1979, the ESB presented it to the branch to be awarded for the 'Recovery of a Cruiser' competition."},
    {"id": "bob_hughes", "name": "The Hughes Perpetual Trophy", "category": "skill", "image": "trophy_plaque.png",
     "desc": "Presented to the branch by Bob and Rita Hughes. Awarded for the Boat Inspection competition."},
    {"id": "newman", "name": "The Newman Perpetual Cup", "category": "skill", "image": "trophy_cup.png",
     "desc": "Presented by Frank and Louise Newman. Awarded to the winner of a surprise boat inspection."},
    {"id": "jh_stimpson", "name": "The Stimpson Cup", "category": "skill", "image": "trophy_cup.png",
     "desc": "Awarded to the best 'Open Boat' entrant. In the early years, many ralliers did not have cruisers and took part in the rally using lake boats and camping in tents along the way."},

    # Fun / Other
    {"id": "eric_timon", "name": "The Ditty Cup", "category": "fun", "image": "trophy_cup.png",
     "desc": "Presented by Eric Timon. This is one of the most popular competitions of the rally. Ralliers are invited to compose a 'ditty' (a song or poem) about the rally and perform it at the entertainment evening."},
    {"id": "finton_harold", "name": "The Harold Memorial Perpetual Trophy", "category": "fun", "image": "trophy_shield.png",
     "desc": "Presented to the branch in memory of Fintan Harold. Fintan was a long-time member of the branch and a regular rally goer. It is awarded to the winner of the Men's Line Heaving competition."},
    {"id": "mccormack", "name": "The Jane McCormack Salver", "category": "fun", "image": "trophy_plaque.png",
     "desc": "Presented to the branch by Bill McCormack of Cormacruisers. Awarded to the winner of the Ladies Line Heaving competition."},
    {"id": "benson", "name": "The Benson Perpetual Shield", "category": "fun", "image": "trophy_shield.png",
     "desc": "Presented by Robin Benson of the 'Marlou'. Awarded to the winner of the 'Young Bosun' competition."},
]

OUTPUT_FILE = 'content/archive/artifacts/winners.md'
STATIC_IMG_PATH = '{static}/images/'

def generate_markdown():
    md = """Title: Hall of Fame (Trophy Winners)
Date: 2024-01-29
Slug: archive/artifacts/winners
Save_as: archive/artifacts/winners/index.html
URL: archive/artifacts/winners/index.html


Welcome to our shiny new Hall of Fame gallery! Click on a trophy to view its history and past winners.
Use the buttons below to filter the awards.

<!-- DataTables CSS -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/responsive/2.5.0/css/responsive.dataTables.min.css">

<style>
/* Filter Buttons */
.filter-btn {
    background-color: #f8f9fa;
    border: 1px solid #ddd;
    border-radius: 20px;
    padding: 8px 16px;
    margin: 5px;
    cursor: pointer;
    transition: all 0.2s;
    font-size: 0.9rem;
}
.filter-btn.active, .filter-btn:hover {
    background-color: #007bff;
    color: white;
    border-color: #007bff;
}

/* Trophy Grid */
.trophy-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 30px;
    margin-top: 30px;
}
.trophy-card {
    background: #fff;
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    transition: transform 0.2s;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.trophy-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}
.trophy-icon {
    width: 64px;
    height: 64px;
    margin-bottom: 15px;
    object-fit: contain;
}
.trophy-category {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #888;
    margin-bottom: 5px;
}
.trophy-title {
    font-weight: bold;
    font-size: 1.1rem;
    margin-bottom: 10px;
}
.trophy-short-desc {
    font-size: 0.9rem;
    color: #666;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

/* Modal */
.modal-overlay {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.7);
    z-index: 1000;
    justify-content: center;
    align-items: center;
    padding: 20px;
}
.modal-content {
    background: white;
    padding: 30px;
    border-radius: 8px;
    max-width: 900px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}
.modal-close {
    position: absolute;
    top: 15px;
    right: 20px;
    font-size: 1.5rem;
    cursor: pointer;
    color: #aaa;
}
.modal-close:hover { color: #333; }
.modal-header {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-bottom: 20px;
    border-bottom: 1px solid #eee;
    padding-bottom: 20px;
}
.modal-header img { width: 80px; height: 80px; }
.modal-history { margin-bottom: 30px; line-height: 1.6; color: #444; }
</style>

<!-- Filters -->
<div class="filters" style="text-align: center; margin-bottom: 40px;">
    <button class="filter-btn active" onclick="filterTrophies('all')">All</button>
    <button class="filter-btn" onclick="filterTrophies('premier')">Premier</button>
    <button class="filter-btn" onclick="filterTrophies('barge')">Barges</button>
    <button class="filter-btn" onclick="filterTrophies('skill')">Skills</button>
    <button class="filter-btn" onclick="filterTrophies('spirit')">Spirit</button>
    <button class="filter-btn" onclick="filterTrophies('newcomer')">Newcomer</button>
    <button class="filter-btn" onclick="filterTrophies('fun')">Fun</button>
</div>

<!-- Grid -->
<div class="trophy-grid">
"""

    # Generate Grid Cards
    for t in trophies:
        md += f"""
    <div class="trophy-card category-{t['category']}" onclick="openModal('{t['id']}')">
        <img src="{STATIC_IMG_PATH}{t['image']}" class="trophy-icon" alt="{t['name']}">
        <span class="trophy-category">{t['category']}</span>
        <div class="trophy-title">{t['name']}</div>
        <div class="trophy-short-desc">{t['desc']}</div>
    </div>
"""
    
    md += "</div>\\n\\n"

    # Generate Modals
    for t in trophies:
        md += f"""
<div id="modal-{t['id']}" class="modal-overlay" onclick="closeModal(event, '{t['id']}')">
    <div class="modal-content" onclick="event.stopPropagation()">
        <span class="modal-close" onclick="closeModal(event, '{t['id']}')">&times;</span>
        <div class="modal-header">
            <img src="{STATIC_IMG_PATH}{t['image']}" alt="{t['name']}">
            <h2>{t['name']}</h2>
        </div>
        <div class="modal-history">
            <h3>About this Trophy</h3>
            <p>{t['desc']}</p>
        </div>
        <h3>Past Winners</h3>
        <table id="table_{t['id']}" class="display responsive nowrap" style="width:100%">
            <thead>
                <tr>
                    <th data-priority="1">Year</th>
                    <th data-priority="3">Rally No.</th>
                    <th data-priority="2">Winner</th>
                </tr>
            </thead>
        </table>
    </div>
</div>
"""

    # JavaScript
    md += f"""
<!-- Scripts -->
<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/responsive/2.5.0/js/dataTables.responsive.min.js"></script>
<script src="{{static}}/js/winners_data.js"></script>

<script>
// Filter Logic
function filterTrophies(category) {{
    // Update Active Button
    const buttons = document.querySelectorAll('.filter-btn');
    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    // Filter Cards
    const cards = document.querySelectorAll('.trophy-card');
    cards.forEach(card => {{
        if (category === 'all' || card.classList.contains('category-' + category)) {{
            card.style.display = 'flex';
        }} else {{
            card.style.display = 'none';
        }}
    }});
}}

// Modal Logic
function openModal(id) {{
    const modal = document.getElementById('modal-' + id);
    modal.style.display = 'flex';
    
    // Recalculate DataTable responsiveness when modal opens
    // This is needed because DataTables doesn't calculate widths correctly in hidden elements
    const table = $('#table_' + id).DataTable();
    table.columns.adjust().responsive.recalc();
}}

function closeModal(event, id) {{
    const modal = document.getElementById('modal-' + id);
    modal.style.display = 'none';
}}

$(document).ready(function() {{
    // Initialize DataTables
"""

    for t in trophies:
        md += f"""
    $('#table_{t['id']}').DataTable({{
        data: trophyData,
        columns: [
            {{ data: 'year' }},
            {{ data: 'rally' }},
            {{ data: '{t['id']}', defaultContent: "" }} // defaultContent avoids error if col missing
        ],
        responsive: true,
        order: [[ 0, "desc" ]],
        pageLength: 10,
        language: {{ search: "_INPUT_", searchPlaceholder: "Filter..." }}
    }});
"""

    md += "});\\n</script>"

    with open(OUTPUT_FILE, 'w') as f:
        f.write(md)
    print(f"Generated {OUTPUT_FILE} with gallery layout.")

if __name__ == "__main__":
    generate_markdown()
