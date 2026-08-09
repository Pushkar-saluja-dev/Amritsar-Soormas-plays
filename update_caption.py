from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
section = soup.find('section', class_='mf1-search-section')

if section:
    caption = section.find('p', class_='mf1-caption')
    if caption and 'Dropbox Dash' in caption.text:
        caption.string = 'AMRITSAR SOORMAS'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Caption updated.")
