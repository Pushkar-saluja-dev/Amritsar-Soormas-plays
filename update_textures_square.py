with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ('Branding_stuff/Cricket%20bat%20no%20color.png', 'Branding_stuff/Cricket%20bat%20no%20color%20square.png'),
    ('Branding_stuff/Cricket%20bat%20with%20color.png', 'Branding_stuff/Cricket%20bat%20with%20color%20square.png')
]

for old_str, new_str in replacements:
    if old_str in html:
        html = html.replace(old_str, new_str)
        print(f"Successfully replaced: {old_str}")
    else:
        print(f"FAILED to find: {old_str}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
