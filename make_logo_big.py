import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Find the logo in the top navbar and make it bigger
logos = soup.find_all('img')
for img in logos:
    src = img.get('src', '')
    if 'Logo.png' in src:
        # Check if it's the navbar logo by checking parent classes or current style
        style = img.get('style', '')
        if '32px' in style:
            # Change height from 32px to 64px
            img['style'] = style.replace('32px', '64px')
            changes.append("Made navbar logo bigger (64px)")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
