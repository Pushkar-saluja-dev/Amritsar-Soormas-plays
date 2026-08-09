import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

changes = []

# Find the main driver image and replace it with Abhishek Sharma
driver_img = soup.find('img', class_='mf1-hero-hero')
if driver_img:
    driver_img['src'] = 'Branding_stuff/Abhieshek iconic sign.png'
    
    # Remove srcset and sizes so it just uses our local high-res image
    if 'srcset' in driver_img.attrs:
        del driver_img['srcset']
    if 'sizes' in driver_img.attrs:
        del driver_img['sizes']
        
    changes.append("Replaced F1 racer with Abhishek Sharma (iconic pose)")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(changes)
