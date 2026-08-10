with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ('<p class="mf1-caption">THE SOORMA STANDARD</p>', '<p class="mf1-caption" style="letter-spacing: 0.15em;">The Soorma Standard</p>'),
    ('<h2 class="mf1-h2">Built for the big moments.<br>Ready for every match.</h2>', '<h2 class="mf1-h2" style="font-weight: 700 !important;">Built for the big moments.<br>Ready for every match.</h2>'),
    ('<div>EXPLORE THE SOORMA WORLD</div>', '<div>Explore the Soorma world</div>')
]

for old_str, new_str in replacements:
    if old_str in html:
        html = html.replace(old_str, new_str)
        print(f"Successfully replaced: {old_str[:30]}...")
    else:
        print(f"FAILED to find: {old_str[:30]}...")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
