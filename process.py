import json
import re

input_file = r'C:\Users\pushk\.gemini\antigravity\brain\a0abc730-6056-45e9-ba56-bd063e93c63a\.system_generated\steps\126\output.txt'
output_file = r'C:\Users\pushk\Desktop\expiremen\index.html'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the JSON string part
# It looks like:
# Script ran on page and returned:
# ```json
# "<html...>"
# ```
match = re.search(r'```json\n(.*)\n```', content, re.DOTALL)
if match:
    json_str = match.group(1)
    # Parse the json string to get the raw HTML
    html_content = json.loads(json_str)
    
    # Perform replacements
    replacements = [
        (r'McLaren F1 Team', 'High Performance Cricket Team'),
        (r'McLaren F1', 'High Performance Cricket'),
        (r'McLaren', 'Cricket Team'),
        (r'race days', 'match days'),
        (r'race day', 'match day'),
        (r'track', 'pitch'),
        (r'F1', 'Cricket'),
        (r'driver', 'player'),
        (r'Driver', 'Player'),
        (r'grid', 'field'),
        (r'Lando Norris', 'Our Captain'),
        (r'Oscar Piastri', 'Our Vice Captain'),
        (r'Formula 1', 'Cricket'),
        (r'Formula One', 'Cricket'),
        (r'Grand Prix', 'World Cup'),
        (r'Papaya', 'Blue')
    ]
    
    for old, new in replacements:
        # Simple string replace, might need regex for word boundaries if we were being super strict, 
        # but string replace is safer for HTML text.
        html_content = html_content.replace(old, new)
        
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Successfully processed and saved to index.html")
else:
    print("Could not find JSON string in the output.")
