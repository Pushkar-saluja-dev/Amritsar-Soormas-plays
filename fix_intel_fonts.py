import re
from bs4 import BeautifulSoup

html_content = open('index.html', 'r', encoding='utf-8').read()
soup = BeautifulSoup(html_content, 'html.parser')

css_tag = soup.find(id='custom-cards-css')
if css_tag:
    css = css_tag.string
    
    # Scale down the fonts and spacing so it fits in a 153px square
    css = css.replace('.custom-card-5-top {\n  font-size: 14px;', '.custom-card-5-top {\n  font-size: 9px;')
    css = css.replace('.custom-card-5-title {\n  font-size: 16px;', '.custom-card-5-title {\n  font-size: 11px;')
    css = css.replace('.custom-card-5-title {\n  font-size: 11px;\n  font-weight: 800;\n  line-height: 1.2;\n  margin-bottom: 12%;', '.custom-card-5-title {\n  font-size: 11px;\n  font-weight: 800;\n  line-height: 1.2;\n  margin-bottom: 8%;')
    css = css.replace('.custom-card-5-icon {\n  width: 16px;\n  height: 16px;', '.custom-card-5-icon {\n  width: 12px;\n  height: 12px;')
    
    css = css.replace('.custom-card-5-skeleton {\n  height: 8px;', '.custom-card-5-skeleton {\n  height: 4px;')
    css = css.replace('gap: 8px;', 'gap: 4px;')
    
    css = css.replace('.custom-card-5-footer-text {\n  font-size: 11px;', '.custom-card-5-footer-text {\n  font-size: 7px;')
    css = css.replace('margin-bottom: 10px;', 'margin-bottom: 4px;')
    css = css.replace('.custom-card-5-footer-icon {\n  width: 14px;\n  height: 14px;', '.custom-card-5-footer-icon {\n  width: 10px;\n  height: 10px;')
    
    css_tag.string.replace_with(css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
