import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Fix Headline Visibility
h1 = soup.find('h1', id='hero-heading-custom')
if h1:
    h1['style'] = h1.get('style', '') + '; opacity: 1 !important; visibility: visible !important; transform: none !important;'
    
    # Let's ensure the spans inside have styles that reset them just in case
    new_html = '''
    <div style="opacity: 1 !important; visibility: visible !important; display: block; font-size: 80px; line-height: 1.1; font-weight: bold; color: white; text-align: center;">AMRITSAR SOORMAS</div>
    <div style="opacity: 1 !important; visibility: visible !important; display: block; font-size: 80px; line-height: 1.1; font-weight: bold; color: white; text-align: center;">BUILT FOR THE MOMENT.</div>
    <div style="opacity: 1 !important; visibility: visible !important; display: block; font-size: 80px; line-height: 1.1; font-weight: bold; color: #39ff14; text-transform: uppercase; text-align: center;">#MAIVISOORMA</div>
    '''
    h1.clear()
    h1.append(BeautifulSoup(new_html, 'html.parser'))
    changes.append("Fixed headline visibility completely")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
