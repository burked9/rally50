Title: Hall of Fame (Trophy Winners)
Date: 2024-01-28
Slug: archive/artifacts/winners
Save_as: archive/artifacts/winners/index.html
URL: archive/artifacts/winners/index.html

# Hall of Fame

Search over 40 years of history to find a winner, boat, or year.

<!-- DataTables CSS -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/responsive/2.5.0/css/responsive.dataTables.min.css">

<style>
/* Custom Table Styles */
#winnersTable {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
}

#winnersTable thead th {
    text-align: left;
    background-color: #f4f4f4;
    border-bottom: 2px solid #ddd;
    padding: 10px;
}

#winnersTable tbody td {
    padding: 10px;
    border-bottom: 1px solid #eee;
}

/* Hide most columns on mobile default, DataTables responsive handles the rest */
</style>

<div style="margin-top: 20px;">
    <table id="winnersTable" class="display responsive nowrap" style="width:100%">
        <thead>
            <tr>
                <!-- Define main headers -->
                <th data-priority="1">Year</th>
                <th data-priority="2">Rally</th>
                <th data-priority="3">Overall Team (Kineally Cup)</th>
                <th>Committee Prize (Estemaid)</th>
                <th>Barge Race (Boyle)</th>
                <th>Recovery (Benjamin)</th>
                <th>NM Barge (Hand)</th>
                <th>Orienteering (Wynn Juba)</th>
                <th>Friendship Cup</th>
                <th>Boat Inspection (Hughes)</th>
                <th>Jr Friendship (Clarke)</th>
                <th>Surprise Inspection (Newman)</th>
                <th>Best Endeavour (Leyden)</th>
                <th>Best Newcomer (Byrne)</th>
                <th>Line Heaving Mens (Harold)</th>
                <th>Line Heaving Womens (McCormack)</th>
                <th>Man Over Board (Juba)</th>
                <th>Boat Handling (Westpark)</th>
                <th>Ditty Cup (Timon)</th>
                <th>Time Trial (Tavern)</th>
                <th>Barge Handling (Scarriff)</th>
                <th>Sailing (Stimpson)</th>
                <th>Young Bosun (Benson)</th>
            </tr>
        </thead>
    </table>
</div>

<!-- Load Scripts -->
<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/responsive/2.5.0/js/dataTables.responsive.min.js"></script>
<script src="{static}/js/winners_data.js"></script>

<script>
$(document).ready(function() {
    $('#winnersTable').DataTable({
        data: trophyData,
        columns: [
            { data: 'year' },
            { data: 'rally' },
            { data: 'jj_kineally' }, // Overall Team
            { data: 'estemaid' },
            { data: 'boyle' },
            { data: 'benjamin' },
            { data: 'nm_barge' },
            { data: 'wynn_juba' },
            { data: 'friendship' },
            { data: 'bob_hughes' },
            { data: 'ann_clarke' },
            { data: 'newman' },
            { data: 'jimmy_leyden' },
            { data: 'dennis_byrne' },
            { data: 'finton_harold' },
            { data: 'mccormack' },
            { data: 'dennis_juba' },
            { data: 'westpark' },
            { data: 'eric_timon' },
            { data: 'tavern' },
            { data: 'scarriff' },
            { data: 'jh_stimpson' },
            { data: 'benson' }
        ],
        responsive: true,
        order: [[ 0, "desc" ]], // Sort by Year desc
        pageLength: 25,
        language: {
            search: "_INPUT_",
            searchPlaceholder: "Search winners..."
        }
    });
});
</script>
