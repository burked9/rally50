
import csv
import io

# Raw data provided by user
raw_data = """Year,Commodore,Boat
1975,William J. Knight,Golden Hours
1976,William Lysaght,Sunsasado
1977,David Knight,Humming Bird
1978,Richie O’Donoghue,Brijella
1979,No Rally,—
1980,Frank Van Den Berg,Argent Brack
1981,Thomas A. Duffy,Lotus Two
1982,Bryan Brislane,Lady Sarah
1983,Colin Becker,LadyG
1984,Maureen Duffy,Lotus Two
1985,Chris Boyle,Christina
1986,Joe Treacy,4E
1987,Albert Gill,Breakaway
1988,Tom Quinn,Abigail
1989,Mark Maguire,Maan of Derg
1990,Martin O’Brien,Ce Na Ri
1991,Eric Makim,Sunset
1992,Cathy Scotson,Ajenda
1993,Joe Treacy,4E
1994,Les Saunders,41M
1995,"Mark Maguire, Jnr",Mann of Derg
1996,Eamon Egan,Hawthorn
1997,John Moore,Twenty Pence
1998,Oliver Kennedy,—
1999,Tom Moore,Jasmine
2000,Rory Stephens,Yali
2001,Lana Treacy,Crystal Heart
2002,Andy Roche,35M
2003,Geraldine Burke,68M
2004,Fergal Kearney,Tanjuan
2005,Nicky Coady,My Little Boat
2006,Cathy Dwane,74M
2007,Clare Jordan,El-Roi
2008,Noel Griffin,Ocean Froggie
2009,Carmel Byrne,Desperado
2010,Jimmy Mac Farlane,Paradise
2011,Rory Winston,Hylander
2012,Michael Geraghty,Affaja
2013,Robert Lambert,De Eems
2014,David Brassington,Peggy May
2015,Daniel Burke,77M
2016,Joe Leonard,Shanice
2017,Ivan Thornbury,Auburn
2018,Darrell Brislane,Gallifrey"""

# File path
OUTPUT_FILE = 'content/archive/people/commodores.md'

def generate_commodores_page():
    # Parse CSV data
    f = io.StringIO(raw_data)
    reader = csv.DictReader(f)
    commodores = list(reader)
    
    # Sort by year descending (usually better for history) or ascending?
    # User provided ascending. I'll stick to ascending as it flows through history, 
    # but often lists like this are descending throughout the site (like rallies).
    # Let's check Rallies... generated content is strictly year based index.
    # User's list is ascending. I will output ascending as provided, unless I see a reason not to.
    # Actually, let's do descending so recent ones are at top? 
    # The user provided 1975 first. I'll stick to their order to be safe, or ask?
    # Rallies index is usually chronological (1975 -> 2027). So ascending is consistent with Rallies index.
    # Wait, the winners tables I made descending (2024 -> 1975).
    # Let's keep it ascending as provided for now, it tells the story.
    
    md = """Title: List of Commodores
Date: 2024-01-28
Slug: archive/people/commodores
Save_as: archive/people/commodores/index.html
URL: archive/people/commodores/index.html

Honoring the Commodores who have led the Lough Derg Rally over the past 50 years.

<div class="l-stack">
    <table class="display responsive nowrap" style="width:100%">
        <thead>
            <tr>
                <th style="text-align: left;">Year</th>
                <th style="text-align: left;">Commodore</th>
                <th style="text-align: left;">Boat</th>
            </tr>
        </thead>
        <tbody>
"""
    
    for row in commodores:
        year = row['Year']
        name = row['Commodore']
        boat = row['Boat']
        
        md += f"""            <tr>
                <td>{year}</td>
                <td>{name}</td>
                <td>{boat}</td>
            </tr>
"""

    md += """        </tbody>
    </table>
</div>
"""

    with open(OUTPUT_FILE, 'w') as f:
        f.write(md)
    print(f"Generated {OUTPUT_FILE} with {len(commodores)} records.")

if __name__ == "__main__":
    generate_commodores_page()
