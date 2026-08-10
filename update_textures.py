with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ('https://cdn.prod.website-files.com/68128ae464f54be2f37033b8/6840bc94bc7d64d558607070_Security-Idle.png', 'Branding_stuff/Cricket%20bat%20no%20color.png'),
    ('https://cdn.prod.website-files.com/68128ae464f54be2f37033b8/6840bc94f7d2dcbe481447cb_Security-Active.png', 'Branding_stuff/Cricket%20bat%20with%20color.png')
]

for old_str, new_str in replacements:
    if old_str in html:
        html = html.replace(old_str, new_str)
        print(f"Successfully replaced: {old_str}")
    else:
        print(f"FAILED to find: {old_str}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
