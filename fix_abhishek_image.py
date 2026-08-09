import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Update Abhishek Sharma image to fix proportions and prevent overlap
img = soup.find('img', class_='mf1-hero-hero')
if img:
    # Use object-fit contain to maintain aspect ratio and not compress
    # Translate it down by 25% and scale it down to 80% so his hand doesn't touch the text
    img['style'] = img.get('style', '') + '; object-fit: contain !important; object-position: bottom center !important; width: 100% !important; height: 100% !important; transform: translateY(25%) scale(0.80) !important;'
    changes.append("Fixed Abhishek image proportions and positioning")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
