import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Fix Headline
h1 = soup.find('h1', id='hero-heading')
if h1:
    # Change ID so Webflow animation script ignores it
    h1['id'] = 'hero-heading-custom'
    if h1.has_attr('data-w-id'):
        del h1['data-w-id']
    
    # Also strip class if it targets it
    if 'mf1-hero-heading' in h1.get('class', []):
        h1['class'] = [c for c in h1['class'] if c != 'mf1-hero-heading']
        # We need to preserve the styling if we strip the class, but let's try just removing ID and data-w-id first.
        # Actually, let's keep mf1-hero-heading because it provides font size and weight.
    
    h1.clear()
    new_html = '''
    <span style="display: block; margin-bottom: 5px;">AMRITSAR SOORMAS</span>
    <span style="display: block; margin-bottom: 5px;">BUILT FOR THE MOMENT.</span>
    <span style="display: block; color: #39ff14 !important; text-transform: uppercase;">#MAIVISOORMA</span>
    '''
    h1.append(BeautifulSoup(new_html, 'html.parser'))
    changes.append("Fixed headline ID and spacing")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
