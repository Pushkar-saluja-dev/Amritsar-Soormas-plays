import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Append ?v=2 to Logo.png to bust the browser cache
for img in soup.find_all('img'):
    src = img.get('src', '')
    if 'Logo.png' in src:
        # Remove any existing query params first
        base_src = src.split('?')[0]
        img['src'] = f"{base_src}?v=2"
        changes.append("Cache-busted Logo.png")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
