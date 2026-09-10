import re
import os

source_file = 'content/archive/people/commodores.md'
target_file = 'theme/templates/commodores_table.html'

def extract_table():
    if not os.path.exists(source_file):
        print(f"Error: {source_file} not found.")
        return

    with open(source_file, 'r') as f:
        content = f.read()

    # Find the table using regex
    # It starts with <table and ends with </table>
    match = re.search(r'(<table.*?</table>)', content, re.DOTALL)
    
    if match:
        table_html = match.group(1)
        
        # We can clean up the class list to remove 'display responsive nowrap' so our custom css takes over fully
        table_html = re.sub(r'class="[^"]*"', 'class="vintage-table"', table_html, count=1)
        
        with open(target_file, 'w') as f:
            f.write(table_html)
        print(f"Successfully extracted table to {target_file}")
    else:
        print("Error: Could not find table in markdown file.")

if __name__ == "__main__":
    extract_table()
