import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# 1. Update the hero-left-logo style
existing_logo = soup.find('img', id='hero-left-logo')
if existing_logo:
    existing_logo['style'] = 'position: absolute; left: 50%; transform: translateX(-600px); top: 35px; width: 170px; height: auto; z-index: 100;'
    changes.append("Updated hero logo with new exact user styles")

# 2. Remove the IntersectionObserver script I added
script_tags = soup.find_all('script')
for script in script_tags:
    if script.string and 'IntersectionObserver' in script.string and 'hero-left-logo' in script.string:
        script.decompose()
        changes.append("Removed IntersectionObserver script")

# 3. Permanently hide the navbar logo
nav_logos = soup.find_all('div', class_='mf1-dropbox-logo')
for logo in nav_logos:
    logo['style'] = 'display: none !important;'
    changes.append("Permanently hid navbar logo")

# 4. Make "AMRITSAR SOORMAS — 2026" text act as home button
nav_text_elements = soup.find_all(string=re.compile('AMRITSAR SOORMAS — 2026'))
for text_element in nav_text_elements:
    parent = text_element.parent
    if parent and parent.name != 'a':
        # If it's a div, add cursor pointer and onclick
        if parent.name == 'div':
            parent['style'] = parent.get('style', '') + '; cursor: pointer;'
            parent['onclick'] = "window.scrollTo({top: 0, behavior: 'smooth'});"
            changes.append("Made AMRITSAR SOORMAS — 2026 text act as home button")
    elif parent and parent.name == 'a':
        parent['href'] = '#'
        parent['onclick'] = "window.scrollTo({top: 0, behavior: 'smooth'}); return false;"
        changes.append("Updated AMRITSAR SOORMAS — 2026 link to act as home button")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
