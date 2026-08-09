import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

def replace(old, new, text):
    global changes
    if old in text:
        changes += 1
        return text.replace(old, new)
    return text

# Center Title
html = replace("Dropbox x High Performance Cricket Team Mastercard Cricket® Team", "AMRITSAR SOORMAS — 2026", html)

# Learn More Button
html = replace("Learn more", "ENTER SOORMAS →", html)

# Main Headline
# Let's use regex to replace the text inside the hero h1 tag since the spacing/br might vary.
# Looking for something like Dropbox helps<br>...
h1_pattern = re.compile(r'(<h1[^>]*>)(.*?)(</h1>)', re.IGNORECASE | re.DOTALL)
def h1_repl(m):
    inner = m.group(2)
    if 'Dropbox helps' in inner or 'High Performance' in inner:
        new_inner = 'AMRITSAR SOORMAS<br>BUILT FOR THE MOMENT. <br><span style="color: #39ff14;">#MAIVISOORMA</span>'
        return m.group(1) + new_inner + m.group(3)
    return m.group(0)

html, n = h1_pattern.subn(h1_repl, html)
if n > 0: changes += n

# Supporting Paragraph
p_pattern = re.compile(r'(<p[^>]*class="dash-hero_p"[^>]*>)(.*?)(</p>)', re.IGNORECASE | re.DOTALL)
def p_repl(m):
    inner = m.group(2)
    if 'match day' in inner:
        new_inner = 'Born in Amritsar. Built for the game. The Soormas bring together talent, experience and the fighting spirit of a city that lives for cricket.'
        return m.group(1) + new_inner + m.group(3)
    return m.group(0)

html, n = p_pattern.subn(p_repl, html)
if n > 0: changes += n

# Discover Dropbox -> MEET THE SOORMAS
html = replace("Discover Dropbox", "MEET THE SOORMAS", html)

# Search Dashboard Window Text
html = replace("High Performance Cricket Team Mastercard Cricket Team x Dropbox coverage", "AMRITSAR SOORMAS — TEAM COVERAGE", html)

# Logo replacements:
# Find Dropbox SVG logo and replace with our image.
logo_pattern = re.compile(r'<div class="dash-nav_logo w-inline-block">.*?</div>', re.DOTALL)
html, n = logo_pattern.subn('<div class="dash-nav_logo w-inline-block"><img src="Branding stuff/Logo.png" alt="Amritsar Soormas" style="height: 32px; width: auto;" /></div>', html)
if n > 0: changes += n

# Remove the partner logo (McLaren)
partner_logo_pattern = re.compile(r'<div class="dash-nav_partner-logo w-inline-block">.*?</div>', re.DOTALL)
html, n = partner_logo_pattern.subn('', html)
if n > 0: changes += n

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Made {changes} changes successfully.")
