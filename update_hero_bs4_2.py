from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

def replace_string(pattern, new_html):
    el = soup.find(string=re.compile(pattern))
    if el:
        parent = el.parent
        parent.clear()
        parent.append(BeautifulSoup(new_html, 'html.parser'))
        changes.append(f"Replaced: {pattern}")
        return True
    return False

# Center title
replace_string('.*?High Performance Cricket Team Mastercard Cricket.*?', 'AMRITSAR SOORMAS — 2026')

# Main headline
# The main headline might be split into multiple text nodes.
# Let's search for "Dropbox helps"
el = soup.find(string=re.compile('Dropbox helps'))
if el:
    h1 = el.find_parent('h1') or el.find_parent('h2') or el.find_parent('div')
    if h1:
        h1.clear()
        h1.append(BeautifulSoup('AMRITSAR SOORMAS<br>BUILT FOR THE MOMENT. <br><span style="color: #39ff14;">#MAIVISOORMA</span>', 'html.parser'))
        changes.append("Replaced Headline")

# Paragraph
el2 = soup.find(string=re.compile('.*?match day to launch day.*?'))
if el2:
    p = el2.find_parent('p') or el2.find_parent('div')
    if p:
        p.string = "Born in Amritsar. Built for the game. The Soormas bring together talent, experience and the fighting spirit of a city that lives for cricket."
        changes.append("Replaced Paragraph")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
