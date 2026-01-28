# Trophy Definitions (ID, Name, Description Placeholder)
trophies = [
    {"id": "jj_kineally", "name": "JJ Kineally Perpetual Cup (Overall Team Event)", "desc": "Awarded to the team with the highest overall score across all competitions."},
    {"id": "estemaid", "name": "Estemaid Trophy (Committee Prize)", "desc": "Awarded by the committee for a special contribution to the rally."},
    {"id": "boyle", "name": "Boyle Trophy (Barge Race)", "desc": "Awarded to the winner of the annual Barge Race."},
    {"id": "benjamin", "name": "Benjamin Cup (Recovery of a Cruiser)", "desc": "Awarded for the best recovery of a cruiser under simulated conditions."},
    {"id": "nm_barge", "name": "NM Barge Trophy (NM Barge Hand)", "desc": "Awarded for excellence in barge handling by a non-owner/crew member."},
    {"id": "wynn_juba", "name": "Wynn Juba Cup (Orienteering)", "desc": "Awarded to the winner of the marine orienteering competition."},
    {"id": "friendship", "name": "Friendship Cup", "desc": "Awarded to the boat or crew that best embodies the spirit of friendship."},
    {"id": "bob_hughes", "name": "Bob Hughes Perpetual Trophy (Boat Inspection)", "desc": "Awarded for the highest standard of boat presentation and safety."},
    {"id": "ann_clarke", "name": "Ann Clarke Cup (Junior Friendship)", "desc": "Awarded to a junior member who displays outstanding friendship and spirit."},
    {"id": "newman", "name": "Newman Cup (Surprise Boat Inspection)", "desc": "Awarded for the best result in an unannounced boat inspection."},
    {"id": "jimmy_leyden", "name": "The Jimmy Leyden Perpetual Trophy (Best Endeavour)", "desc": "Awarded for the best endeavour throughout the rally weekend."},
    {"id": "dennis_byrne", "name": "Dennis Byrne Cup (Best Newcomer)", "desc": "Awarded to the best performing new participant."},
    {"id": "finton_harold", "name": "Finton Harold M.P. Cup (Line Heaving Mens)", "desc": "Awarded to the winner of the men's line heaving competition."},
    {"id": "mccormack", "name": "The McCormack Plate (Line Heaving Womens)", "desc": "Awarded to the winner of the women's line heaving competition."},
    {"id": "dennis_juba", "name": "Dennis Juba Perpetual Cup (Man Over Board)", "desc": "Awarded to the winner of the Man Overboard rescue simulation."},
    {"id": "westpark", "name": "Westpark Cup (Boat Handling)", "desc": "Awarded for superior skill in boat handling and maneuvering."},
    {"id": "eric_timon", "name": "Eric Timon Ditty Perpetual Cup", "desc": "Awarded for the best original poem or song performed at the rally."},
    {"id": "tavern", "name": "Tavern Cup (Time Trial)", "desc": "Awarded to the winner of the navigation time trial."},
    {"id": "scarriff", "name": "Scarriff Shield (Barge Handling)", "desc": "Awarded for the best display of handling a barge."},
    {"id": "jh_stimpson", "name": "JH Stimpson Perpetual Cup (Sailing Competition)", "desc": "Awarded to the winner of the sailing race."},
    {"id": "benson", "name": "Benson Shield (Young Bosun)", "desc": "Awarded to the most promising young bosun."}
]

OUTPUT_FILE = 'content/archive/artifacts/winners.md'

def generate_markdown():
    # Frontmatter
    md = """Title: Hall of Fame (Trophy Winners)
Date: 2024-01-28
Slug: archive/artifacts/winners
Save_as: archive/artifacts/winners/index.html
URL: archive/artifacts/winners/index.html

# Hall of Fame

Explore the history of our trophies and their winners over the past 50 years.

<!-- DataTables CSS -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/responsive/2.5.0/css/responsive.dataTables.min.css">

<style>
.trophy-section { margin-top: 60px; margin-bottom: 40px; padding-top: 20px; border-top: 1px solid #eee; }
.trophy-desc { font-style: italic; color: #666; margin-bottom: 20px; max-width: 800px; }
table.dataTable { font-size: 0.9rem; }
</style>

<div class="l-stack">
"""

    # Generate Section for each Trophy
    for t in trophies:
        t_id = t['id']
        t_name = t['name']
        t_desc = t['desc']
        
        section = f"""
    <div class="trophy-section" id="{t_id}">
        <h2>{t_name}</h2>
        <div class="trophy-desc">
            <p><strong>History:</strong> {t_desc}</p>
            <p>This trophy has been contested since the early days of the rally. [More history to be added...]</p>
        </div>
        <table id="table_{t_id}" class="display responsive nowrap" style="width:100%">
            <thead>
                <tr>
                    <th data-priority="1">Year</th>
                    <th data-priority="3">Rally No.</th>
                    <th data-priority="2">Winner</th>
                </tr>
            </thead>
        </table>
    </div>
"""
        md += section

    md += "</div>\n\n"

    # JavaScript Generation
    md += f"""
<!-- Load Scripts -->
<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/responsive/2.5.0/js/dataTables.responsive.min.js"></script>
<script src="{{static}}/js/winners_data.js"></script>

<script>
$(document).ready(function() {{
"""
    
    # Init each table
    for t in trophies:
        t_id = t['id']
        js_block = f"""
    $('#table_{t_id}').DataTable({{
        data: trophyData,
        columns: [
            {{ data: 'year' }},
            {{ data: 'rally' }},
            {{ data: '{t_id}' }}
        ],
        responsive: true,
        order: [[ 0, "desc" ]],
        pageLength: 10,
        lengthMenu: [10, 25, 50, "All"],
        language: {{
            search: "",
            searchPlaceholder: "Search {t_name}..."
        }},
        // Only show rows where there is a winner (filter out empty strings for this column)
        // Actually, let's filter visually using the search or just let it show blank rows?
        // Better to custom filter:
        "searchCols": [
            null,
            null,
            {{ search: "^.+$", regex: true }} # Pre-filter for non-empty values in the 3rd column
        ]
    }});
"""
        # Note: auto-filtering empty rows via regex search on init might be aggressive but let's try just showing all data first, 
        # actually empty rows are annoying. 
        # Let's remove the pre-filter for now to avoid confusion if it hides everything (e.g. if I messed up the column name).
        # User said "I need one table...".
        # I will keep it simple.
        
        js_block_simple = f"""
    $('#table_{t_id}').DataTable({{
        data: trophyData,
        columns: [
            {{ data: 'year' }},
            {{ data: 'rally' }},
            {{ data: '{t_id}' }}
        ],
        responsive: true,
        order: [[ 0, "desc" ]],
        pageLength: 10,
        language: {{
            search: "_INPUT_",
            searchPlaceholder: "Filter..."
        }}
    }});
"""
        md += js_block_simple

    md += "});\n</script>"

    with open(OUTPUT_FILE, 'w') as f:
        f.write(md)
    print(f"Generated {OUTPUT_FILE} with {len(trophies)} tables.")

if __name__ == "__main__":
    generate_markdown()
