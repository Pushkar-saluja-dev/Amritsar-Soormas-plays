import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# 1. Update Abhishek Sharma image to be huge and overlap the button
img = soup.find('img', class_='mf1-hero-hero')
if img:
    # Need to replace whatever transform is currently there
    old_style = img.get('style', '')
    new_style = re.sub(r'transform:\s*[^;]+;', 'transform: translateY(10%) translateX(5%) scale(1.4) !important;', old_style)
    # If transform wasn't there (should be from previous steps, but just in case)
    if 'transform:' not in new_style:
        new_style += '; transform: translateY(10%) translateX(5%) scale(1.4) !important;'
    img['style'] = new_style
    changes.append("Updated Abhishek image to be massive and overlap the button")

# 2. Fix the H1 text alignment
h1 = soup.find('h1', class_='mf1-hero-heading')
if h1:
    h1['style'] = h1.get('style', '') + '; text-align: center !important; display: flex !important; flex-direction: column !important; align-items: center !important; line-height: 1.1 !important;'
    changes.append("Fixed H1 text alignment")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
