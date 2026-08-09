import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# 1. Hide the original navbar logo
nav_logos = soup.find_all('div', class_='mf1-dropbox-logo')
for logo in nav_logos:
    logo['style'] = logo.get('style', '') + '; display: none !important;'
    changes.append("Hid original navbar logo")

# 2. Add the logo to the hero section
hero_content = soup.find('div', class_='mf1-hero-content')
if hero_content:
    # Ensure it's relative
    hero_content['style'] = hero_content.get('style', '') + '; position: relative;'
    
    # Check if we already added it so we don't duplicate
    existing_logo = soup.find('img', id='hero-left-logo')
    if not existing_logo:
        new_logo = soup.new_tag('img', id='hero-left-logo')
        new_logo['src'] = 'Branding_stuff/Logo.png?v=2'
        new_logo['style'] = 'position: absolute; left: 50%; transform: translateX(-530px); top: 10px; width: 170px; height: auto; z-index: 100;'
        hero_content.append(new_logo)
        changes.append("Injected new hero logo")
    else:
        existing_logo['style'] = 'position: absolute; left: 50%; transform: translateX(-530px); top: 10px; width: 170px; height: auto; z-index: 100;'
        changes.append("Updated existing hero logo")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
