from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

h1 = soup.find('h1', class_='dash-hero_heading')
if h1:
    h1.clear()
    h1.append(BeautifulSoup('AMRITSAR SOORMAS<br>BUILT FOR THE MOMENT. <br><span style="color: #39ff14;">#MAIVISOORMA</span>', 'html.parser'))
    changes.append("H1 updated")

p = soup.find('p', class_='dash-hero_p')
if p:
    p.string = "Born in Amritsar. Built for the game. The Soormas bring together talent, experience and the fighting spirit of a city that lives for cricket."
    changes.append("P updated")

nav_text = soup.find('div', class_=re.compile('.*?dash-nav_text.*?'))
if nav_text:
    nav_text.string = "AMRITSAR SOORMAS — 2026"
    changes.append("Nav text updated")
else:
    # Try finding exact text string
    el = soup.find(text=re.compile('.*?High Performance Cricket Team Mastercard Cricket.*?'))
    if el:
        el.replace_with("AMRITSAR SOORMAS — 2026")
        changes.append("Nav text updated via string match")

# Search dashboard coverage
el = soup.find(text=re.compile('.*?coverage.*?'))
if el:
    el.replace_with("AMRITSAR SOORMAS — TEAM COVERAGE")
    changes.append("Coverage updated via string match")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
