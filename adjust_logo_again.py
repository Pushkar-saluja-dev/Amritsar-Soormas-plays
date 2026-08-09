import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Find the existing hero-left-logo and update its style
existing_logo = soup.find('img', id='hero-left-logo')
if existing_logo:
    existing_logo['style'] = 'position: absolute; left: 50%; transform: translateX(-570px); top: 30px; width: 170px; height: auto; z-index: 100;'
    changes.append("Updated hero logo with precise user styles")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
