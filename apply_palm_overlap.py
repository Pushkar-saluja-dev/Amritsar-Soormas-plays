import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Update Abhishek Sharma image to perfectly overlap his palm with the button
img = soup.find('img', class_='mf1-hero-hero')
if img:
    old_style = img.get('style', '')
    new_style = re.sub(r'transform:\s*[^;]+;', 'transform: translateY(30%) translateX(2%) scale(1.1) !important;', old_style)
    img['style'] = new_style
    changes.append("Adjusted Abhishek image so his palm overlaps the button")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
