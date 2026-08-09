import re
from bs4 import BeautifulSoup

html_content = open('index.html', 'r', encoding='utf-8').read()
soup = BeautifulSoup(html_content, 'html.parser')

css_tag = soup.find(id='custom-cards-css')
if css_tag:
    css = css_tag.string
    
    # Fix Card 3 badge
    css = css.replace('.custom-card-3-badge {', '.custom-card-3-badge { white-space: nowrap; font-size: 10px; margin-left: 8px; ')
    
    # Fix Card 5 skeleton loaders (they were missing height or width maybe, or hidden?)
    css = css.replace('.custom-card-5-skeleton {', '.custom-card-5-skeleton { display: block; min-height: 8px; ')
    
    css_tag.string.replace_with(css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
