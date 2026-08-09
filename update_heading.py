from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
section = soup.find('section', class_='mf1-search-section')

if section:
    h2 = section.find('h2', class_='mf1-h2')
    if h2: 
        h2.string = 'Forged in Amritsar. Driven by Strategy.'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Heading updated.")
