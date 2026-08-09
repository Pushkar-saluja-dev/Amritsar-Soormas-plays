import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

h1 = soup.find('h1', id='hero-heading-custom')
if h1:
    h1.clear()
    h1['class'] = ['mf1-hero-heading'] # restore the class for typography
    h1['id'] = 'hero-heading-custom'   # Keep custom ID so script doesn't target it by ID
    
    # Strip inline styles from the h1 container itself that we added
    if 'style' in h1.attrs:
        del h1['style']
        
    # We add a slight fade-in animation or just make it visible
    # Actually, if we don't have the script hiding it, it should just be visible by default.
    # The mf1-hero-heading class might have opacity:0 in CSS. Let's add opacity:1
    h1['style'] = 'opacity: 1 !important; visibility: visible !important;'
    
    new_html = '''
    <span style="display: block;">AMRITSAR SOORMAS</span>
    <span style="display: block;">BUILT FOR THE MOMENT.</span>
    <span style="display: block; color: #39ff14;">#MAIVISOORMA</span>
    '''
    h1.append(BeautifulSoup(new_html, 'html.parser'))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
