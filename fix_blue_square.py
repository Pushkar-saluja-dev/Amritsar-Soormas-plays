import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Find the logo wrapper and remove the blue background
# The blue background is usually set on the 'mf1-nav_brand' or 'mf1-dropbox-logo' or 'w-inline-block' 
# Let's add an inline style to force it to be transparent.
logos = soup.find_all('div', class_='mf1-dropbox-logo')
for logo in logos:
    logo['style'] = logo.get('style', '') + '; background-color: transparent !important; background: none !important;'
    changes.append("Removed blue background from mf1-dropbox-logo")

nav_brands = soup.find_all('a', class_=re.compile('.*?mf1-nav_brand.*?'))
for brand in nav_brands:
    brand['style'] = brand.get('style', '') + '; background-color: transparent !important; background: none !important;'
    changes.append("Removed blue background from nav brand wrapper")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
