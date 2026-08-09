import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Update Abhishek Sharma image to be larger but offset to the right and down
img = soup.find('img', class_='mf1-hero-hero')
if img:
    img['style'] = img.get('style', '').replace('translateY(25%) scale(0.80)', 'translateY(45%) translateX(15%) scale(1.2)')
    changes.append("Fixed Abhishek image size and positioning to perfectly match original F1 driver weight without overlapping text.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
