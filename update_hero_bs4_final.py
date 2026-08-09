from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# 1. Navbar center title & Coverage
nav_text = soup.find('div', class_='mf1-nav_center')
if nav_text:
    nav_text.string = "AMRITSAR SOORMAS — 2026"
    changes.append("Nav center updated via mf1-nav_center")
else:
    # fallback
    spans = soup.find_all('span')
    for span in spans:
        if span.string and 'Mastercard' in span.string and 'x' in span.string:
            span.string = "AMRITSAR SOORMAS — TEAM COVERAGE"
            changes.append("Found a span with Mastercard x")

# Just find the exact text in elements
for tag in soup.find_all(string=True):
    # This matches text nodes.
    text = tag.string
    if text:
        if 'Dropbox x High Performance Cricket Team' in text or 'Dropbox x Cricket Team Mastercard' in text:
            tag.replace_with('AMRITSAR SOORMAS — 2026')
            changes.append("Replaced navbar text")
        elif 'High Performance Cricket Team Mastercard Cricket Team x Dropbox coverage' in text or 'Cricket Team Mastercard Cricket Team × Dropbox coverage' in text or 'Mastercard Cricket Team × Dropbox coverage' in text:
            tag.replace_with('AMRITSAR SOORMAS — TEAM COVERAGE')
            changes.append("Replaced coverage text")
            
# 2. Main Headline
h1 = soup.find('h1', id='hero-heading')
if h1:
    h1.clear()
    # To prevent it from being hidden if the original had opacity: 0
    h1['style'] = h1.get('style', '') + '; opacity: 1 !important; visibility: visible !important;'
    h1.append(BeautifulSoup('AMRITSAR SOORMAS<br>BUILT FOR THE MOMENT. <br><span style="color: #39ff14;">#MAIVISOORMA</span>', 'html.parser'))
    changes.append("H1 updated")

# 3. Logo replacements
# We need to replace the Dropbox logo with Logo.png
logos = soup.find_all('a', class_='mf1-nav_brand w-inline-block')
if logos:
    for logo in logos:
        logo.clear()
        logo.append(BeautifulSoup('<img src="Branding stuff/Logo.png" alt="Amritsar Soormas" style="height: 32px; width: auto;" />', 'html.parser'))
    changes.append("Logos updated")

# Remove the partner logo (McLaren)
partner_logo = soup.find('div', class_='mf1-nav_partner')
if partner_logo:
    partner_logo.decompose()
    changes.append("Partner logo removed")
    
# Or replace all images inside mf1-nav_brand and mf1-nav_partner
for img in soup.find_all('img'):
    if img.get('alt') == 'Dropbox' or 'dropbox' in img.get('src', '').lower():
        if img.parent and 'nav' in img.parent.get('class', [''])[0]:
            img['src'] = 'Branding stuff/Logo.png'
            img['style'] = 'height: 32px; width: auto;'
            changes.append("Replaced an img tag logo")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Changes:", changes)
