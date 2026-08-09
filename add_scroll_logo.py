import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Ensure the navbar logo is actually the Soormas logo and is sized correctly
nav_logos_containers = soup.find_all('div', class_='mf1-dropbox-logo')
for container in nav_logos_containers:
    # Ensure it's hidden initially by CSS but can be overridden by JS
    # Currently it has "display: none !important; background-color: transparent !important; background: none !important;"
    
    # Let's find the img inside
    img = container.find('img')
    if img:
        img['src'] = 'Branding_stuff/Logo.png?v=2'
        # Size it so it looks good in the navbar
        img['style'] = img.get('style', '') + '; height: 64px; width: auto;'
        changes.append("Updated navbar logo img src and size")

# Add the script to the end of the body
script_content = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    const heroLogo = document.getElementById('hero-left-logo');
    const navLogos = document.querySelectorAll('.mf1-dropbox-logo');
    
    // Set initial state
    navLogos.forEach(logo => {
        logo.style.setProperty('display', 'none', 'important');
    });

    if (heroLogo) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Hero logo is visible, hide nav logo
                    navLogos.forEach(logo => {
                        logo.style.setProperty('display', 'none', 'important');
                    });
                } else {
                    // Hero logo is not visible, show nav logo
                    navLogos.forEach(logo => {
                        logo.style.setProperty('display', 'block', 'important');
                    });
                }
            });
        }, {
            root: null,
            threshold: 0
        });
        
        observer.observe(heroLogo);
    }
});
</script>
"""

# Check if we already added it
if not soup.find(string=re.compile('IntersectionObserver.*hero-left-logo')):
    body = soup.find('body')
    if body:
        body.append(BeautifulSoup(script_content, 'html.parser'))
        changes.append("Injected IntersectionObserver script")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
