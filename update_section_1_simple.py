from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
section = soup.find('section', class_='mf1-search-section')

if not section:
    print("Section not found!")
    exit(1)

# 1. Update H2 text
h2 = section.find('h2', class_='mf1-h2')
if h2: 
    h2.string = 'Forged in Punjab. Driven by Strategy.'

# 2. Update paragraph text
paragraph = section.find('p', class_='mf1-paragraph')
if paragraph: 
    paragraph.string = 'Before the Soormas hit the pitch, every match is won in the war room. From analyzing opponent data to crafting the perfect lineup, precision is our ultimate weapon.'

# 3. Update search box text
search_filled = section.find('div', id='search-box-filled-text')
if search_filled: 
    search_filled.string = 'Search: Matchday Masterplan 2026'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Simple HTML text replacements applied.")
