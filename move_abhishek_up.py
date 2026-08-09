import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Move Abhishek Sharma slightly up by changing translateY from 30% to 25%
img = soup.find('img', class_='mf1-hero-hero')
if img:
    old_style = img.get('style', '')
    new_style = old_style.replace('translateY(30%)', 'translateY(25%)')
    img['style'] = new_style
    changes.append("Moved Abhishek image slightly up")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
