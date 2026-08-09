import re
from bs4 import BeautifulSoup

html_content = open('index.html', 'r', encoding='utf-8').read()
soup = BeautifulSoup(html_content, 'html.parser')

css_tag = soup.find(id='custom-cards-css')
if css_tag:
    css = css_tag.string
    
    # Fix Card 3 badge
    css = css.replace('.custom-card-3-badge {', '.custom-card-3-badge { display: flex; align-items: center; justify-content: center; min-width: 40px; ')
    css = css.replace('gap: -10px;', 'gap: 4px;')
    
    # Fix Card 5 skeleton loaders (they were missing height or width maybe, or hidden?)
    css = css.replace('.custom-card-5-skeleton {', '.custom-card-5-skeleton { height: 8px; width: 100%; ')
    css = css.replace('.custom-card-5-skeleton.short { width: 60%; }', '.custom-card-5-skeleton.short { width: 40%; }')
    css = css.replace('.custom-card-5-skeleton.medium { width: 80%; }', '.custom-card-5-skeleton.medium { width: 70%; }')
    css = css.replace('.custom-card-5-skeleton.long { width: 100%; background: #bfdbfe; }', '.custom-card-5-skeleton.long { width: 100%; background: #bfdbfe; margin-bottom: 8%; }')
    
    css_tag.string.replace_with(css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
