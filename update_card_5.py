import urllib.request
from PIL import Image, ImageDraw, ImageFont
import os
import io
from bs4 import BeautifulSoup

os.makedirs('Branding_stuff/cards', exist_ok=True)

# 1. Generate the placeholder image
url = 'https://cdn.prod.website-files.com/65dcd70b48edc3a7b446950e/69c25a35f9fb8af7ddff437b_Frame%201400005878%20(1).png'
title = 'PracticeDay_01.jpg'

print("Downloading original image...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    img_data = response.read()
    original_img = Image.open(io.BytesIO(img_data))
    w, h = original_img.size
    
    new_img = Image.new('RGBA', (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(new_img)
    
    padding = 10
    draw.rounded_rectangle([padding, padding, w-padding, h-padding], radius=20, fill=(255, 255, 255, 255), outline=(220, 220, 220, 255), width=2)
    
    try:
        font = ImageFont.truetype("arial.ttf", size=max(16, int(w*0.05)))
    except:
        font = ImageFont.load_default()
        
    box_pad = 40
    box_y0 = padding + 40
    box_y1 = h - padding - 60
    draw.rectangle([box_pad, box_y0, w-box_pad, box_y1], fill=(40, 40, 40, 255))
    
    ph_text = "IMAGE TO BE ADDED"
    try:
        ph_font = ImageFont.truetype("arial.ttf", size=max(12, int(w*0.04)))
    except:
        ph_font = font
    ph_bbox = draw.textbbox((0, 0), ph_text, font=ph_font)
    draw.text((w/2 - (ph_bbox[2]-ph_bbox[0])/2, (box_y0+box_y1)/2 - (ph_bbox[3]-ph_bbox[1])/2), ph_text, fill=(200, 200, 200, 255), font=ph_font)
    
    draw.text((padding + 20, h - padding - 40), title, fill=(0, 0, 0, 255), font=font)
    
    save_path = 'Branding_stuff/cards/mf1-5.png'
    new_img.save(save_path)
    print(f"Generated {save_path} ({w}x{h})")

# 2. Update HTML
print("Updating HTML...")
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
section = soup.find('section', class_='mf1-search-section')

if section:
    connector = section.find('div', id='search-connector-5')
    if connector:
        img = connector.find('img')
        if img:
            img['src'] = save_path
            if 'srcset' in img.attrs:
                del img['srcset']
            if 'sizes' in img.attrs:
                del img['sizes']

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("HTML updated.")
