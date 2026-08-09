import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Shorten the search box background
bg = soup.find('div', class_='mf1-hero-search-background')
if bg:
    bg['style'] = bg.get('style', '') + ' max-width: 650px !important; margin: 0 auto !important;'
    changes.append("Shortened search box width")

# Move cards inward
left_container = soup.find('div', class_='mf1-hero-connector-container-left')
if left_container:
    left_container['style'] = left_container.get('style', '') + ' left: 10% !important;'
    changes.append("Moved left cards inward")

right_container = soup.find('div', class_='mf1-hero-connector-container-right')
if right_container:
    right_container['style'] = right_container.get('style', '') + ' right: 10% !important;'
    changes.append("Moved right cards inward")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
