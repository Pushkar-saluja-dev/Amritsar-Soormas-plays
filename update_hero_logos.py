from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Dropbox logo
dbx_logos = soup.find_all('div', class_='mf1-dropbox-logo')
for logo in dbx_logos:
    logo.clear()
    logo.append(BeautifulSoup('<img src="Branding stuff/Logo.png" alt="Amritsar Soormas" style="height: 32px; width: auto;" />', 'html.parser'))
    changes.append("Dropbox logo replaced")

# McLaren logo
mclaren_logos = soup.find_all('div', class_='mf1-mclaren-logo')
for logo in mclaren_logos:
    logo.decompose() # Remove entirely
    changes.append("McLaren logo removed")

# The partner logo block at the bottom
lockups = soup.find_all('img', class_='mf1-conclusion-logo-lockup')
for lockup in lockups:
    lockup['src'] = 'Branding stuff/Logo.png'
    lockup['style'] = 'height: 100px; width: auto;'
    changes.append("Bottom lockup replaced")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
