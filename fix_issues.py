from bs4 import BeautifulSoup
import urllib.parse

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# 1. Fix Logo Path (URL encoding the space)
for img in soup.find_all('img'):
    src = img.get('src', '')
    if 'Branding stuff' in src:
        img['src'] = src.replace('Branding stuff', 'Branding%20stuff')
        changes.append("Fixed logo path")

# 2. Fix Headline Spacing and Color
h1 = soup.find('h1', id='hero-heading')
if h1:
    h1.clear()
    # Using <div> instead of <br> to force a block break, or inline styles
    new_html = '''
    <div style="display: block; margin-bottom: 10px;">AMRITSAR SOORMAS</div>
    <div style="display: block; margin-bottom: 10px;">BUILT FOR THE MOMENT.</div>
    <div style="display: block; color: #39ff14 !important;">#MAIVISOORMA</div>
    '''
    h1.append(BeautifulSoup(new_html, 'html.parser'))
    changes.append("Fixed headline spacing and color")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
