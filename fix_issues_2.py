import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Fix Logo Paths
for img in soup.find_all('img'):
    src = img.get('src', '')
    if 'Branding%20stuff' in src or 'Branding stuff' in src:
        img['src'] = src.replace('Branding%20stuff', 'Branding_stuff').replace('Branding stuff', 'Branding_stuff')
        changes.append("Fixed logo path")

# Fix Headline
h1 = soup.find('h1', id='hero-heading')
if h1:
    # Remove the animation hooks so Webflow doesn't strip our HTML tags
    if h1.has_attr('data-w-id'):
        del h1['data-w-id']
    
    h1.clear()
    new_html = '''
    <div style="display: block;">AMRITSAR SOORMAS</div>
    <div style="display: block;">BUILT FOR THE MOMENT.</div>
    <div style="display: block; color: #39ff14 !important; text-transform: uppercase;">#MAIVISOORMA</div>
    '''
    h1.append(BeautifulSoup(new_html, 'html.parser'))
    changes.append("Fixed headline")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
