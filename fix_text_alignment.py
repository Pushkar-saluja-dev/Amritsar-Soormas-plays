import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Fix the H1 text alignment by removing flex-direction: column which caused wrapping issues
h1 = soup.find('h1', class_='mf1-hero-heading')
if h1:
    h1['style'] = 'text-align: center !important; display: block !important;'
    # Ensure spans are full width
    for span in h1.find_all('span'):
        span['style'] = 'display: block !important; width: 100% !important;'
        # Add the green color back to the third span
        if '#MAIVISOORMA' in span.text:
            span['style'] += ' color: #39FF14 !important;'
    changes.append("Fixed H1 text alignment to prevent narrow wrapping")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
