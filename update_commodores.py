import re

file_path = 'content/archive/people/commodores.md'

def get_rally_num(year):
    try:
        y = int(year)
    except:
        return ""
        
    if y == 1979 or y in [2020, 2021]:
        return "-"
    
    if y < 1979:
        return y - 1974
    elif y < 2020:
        return y - 1975
    else:
        return y - 1977

with open(file_path, 'r') as f:
    content = f.read()

# 1. Update Header
# Find <th...Year</th> and append Rally No.
header_pattern = r'(<th[^>]*>Year</th>)'
replacement = r'\1\n                <th style="text-align: left;">Rally No.</th>'
content = re.sub(header_pattern, replacement, content)

# 2. Update Rows
# Find <tr>...<td>Year</td>...</tr>
# We look for <td>(\d{4})</td>
# But we need to be careful to insert the new td after it.

def row_replacer(match):
    full_match = match.group(0)
    year_str = match.group(1)
    
    num = get_rally_num(year_str)
    
    # Construct the new cell
    new_cell = f'\n                <td>{num}</td>'
    
    # Insert after the year cell
    return f'<td>{year_str}</td>{new_cell}'

# Regex to find the Year cell. 
# Matches <td>1975</td> exactly.
content = re.sub(r'<td>(\d{4})</td>', row_replacer, content)

# Write back
with open(file_path, 'w') as f:
    f.write(content)

print(f"Updated {file_path}")
