import os
import glob
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup

# Find the uploaded file
upload_dir = r'C:\Users\pushk\.gemini\antigravity\brain\a0abc730-6056-45e9-ba56-bd063e93c63a\.user_uploaded'
files = glob.glob(os.path.join(upload_dir, '*.png'))
files.sort(key=os.path.getctime, reverse=True)

# The cricket player is media__1786306575119.png. 
# We'll dynamically find the tallest aspect ratio one from the last two, or just use the newest.
# As established before, it's files[0] (or we can just hardcode the known one).
img_path = next(f for f in files if "1786306575119" in f)
user_img = Image.open(img_path)

# Original Lando card size (mf1-4 is 668x931)
target_w, target_h = 668, 931
padding = 10

# Create new image
new_img = Image.new('RGBA', (target_w, target_h), (255, 255, 255, 0))
draw = ImageDraw.Draw(new_img)

# White rounded background
draw.rounded_rectangle([padding, padding, target_w-padding, target_h-padding], radius=20, fill=(255, 255, 255, 255), outline=(220, 220, 220, 255), width=2)

# Calculate image box
box_pad = 20
box_y0 = padding + 20
box_y1 = target_h - padding - 60
box_x0 = box_pad
box_x1 = target_w - box_pad

box_w = box_x1 - box_x0
box_h = box_y1 - box_y0

# Scale and crop (object-fit: cover)
user_w, user_h = user_img.size
aspect_user = user_w / user_h
aspect_box = box_w / box_h

if aspect_user > aspect_box:
    # User image is wider than box
    new_h = box_h
    new_w = int(new_h * aspect_user)
    resized_user = user_img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - box_w) // 2
    cropped_user = resized_user.crop((left, 0, left + box_w, box_h))
else:
    # User image is taller than box
    new_w = box_w
    new_h = int(new_w / aspect_user)
    resized_user = user_img.resize((new_w, new_h), Image.LANCZOS)
    top = (new_h - box_h) // 2
    cropped_user = resized_user.crop((0, top, box_w, top + box_h))

# Paste cropped image into new_img
new_img.paste(cropped_user, (box_x0, box_y0))

# Draw title
title = 'PracticeDay_01.jpg'
try:
    font = ImageFont.truetype("arial.ttf", size=max(20, int(target_w*0.05)))
except:
    font = ImageFont.load_default()
    
draw.text((padding + 20, target_h - padding - 50), title, fill=(0, 0, 0, 255), font=font)

os.makedirs('Branding_stuff/cards', exist_ok=True)
save_path = 'Branding_stuff/cards/mf1-4.png'
new_img.save(save_path)
print(f"Generated {save_path} with attached image.")

# Update HTML for mf1-4
print("Updating HTML...")
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
section = soup.find('section', class_='mf1-search-section')

if section:
    connector = section.find('div', id='search-connector-4')
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
