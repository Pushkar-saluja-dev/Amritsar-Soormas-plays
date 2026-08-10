with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ('<p class="mf1-caption">Dropbox</p>', '<p class="mf1-caption">THE SOORMA STANDARD</p>'),
    ('<h2 class="mf1-h2">Creative work that’s consistently on pitch</h2>', '<h2 class="mf1-h2">Built for the big moments.<br>Ready for every match.</h2>'),
    ('<p class="mf1-paragraph">First sketches through final submissions, Cricket Team’s marketing materials are both safe and ready to roll with Dropbox. Work stays organized at every stage of production, even when things shift into high gear.</p>', '<p class="mf1-paragraph">From matchday content to team campaigns, every Soorma moment is built to carry the spirit of Amritsar. The work behind the team is just as relentless as the performance on the field.</p>'),
    ('<div>Secure your handoffs</div>', '<div>EXPLORE THE SOORMA WORLD</div>')
]

for old_str, new_str in replacements:
    if old_str in html:
        html = html.replace(old_str, new_str)
        print(f"Successfully replaced: {old_str[:30]}...")
    else:
        print(f"FAILED to find: {old_str[:30]}...")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
