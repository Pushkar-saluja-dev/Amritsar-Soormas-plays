import os
import glob
import urllib.request
from PIL import Image, ImageDraw, ImageFont
import io

upload_dir = r'C:\Users\pushk\.gemini\antigravity\brain\a0abc730-6056-45e9-ba56-bd063e93c63a\.user_uploaded'
files = glob.glob(os.path.join(upload_dir, '*.*'))
files.sort(key=os.path.getctime, reverse=True)

# The new brand guidelines image
img_path = files[0]
user_img = Image.open(img_path)
print(f"Selected {img_path} ({user_img.size[0]}x{user_img.size[1]})")

# Original mf1-1 card size. Let's fetch it to be sure.
url = 'https://cdn.prod.website-files.com/65dcd70b48edc3a7b446950e/69c26127ed6f045a9f7b71e3_Dropbox%20(2).png'
print("Downloading original image...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    img_data = response.read()
    original_img = Image.open(io.BytesIO(img_data))
    target_w, target_h = original_img.size
    print(f"Original image size: {target_w}x{target_h}")

# We will just scale/crop the user's image to target_w, target_h
new_img = Image.new('RGBA', (target_w, target_h), (255, 255, 255, 0))

# Scale and crop (object-fit: cover)
user_w, user_h = user_img.size
aspect_user = user_w / user_h
aspect_box = target_w / target_h

if aspect_user > aspect_box:
    # User image is wider than box
    new_h = target_h
    new_w = int(new_h * aspect_user)
    resized_user = user_img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - target_w) // 2
    cropped_user = resized_user.crop((left, 0, left + target_w, target_h))
else:
    # User image is taller than box
    new_w = target_w
    new_h = int(new_w / aspect_user)
    resized_user = user_img.resize((new_w, new_h), Image.LANCZOS)
    top = (new_h - target_h) // 2
    cropped_user = resized_user.crop((0, top, target_w, top + target_h))

# Paste cropped image into new_img
new_img.paste(cropped_user, (0, 0))

# Also add rounded corners just in case, because the original had them in the PNG itself.
# To do this, we can create a mask.
mask = Image.new("L", (target_w, target_h), 0)
draw = ImageDraw.Draw(mask)
draw.rounded_rectangle([0, 0, target_w, target_h], radius=24, fill=255)

# Apply mask
final_img = Image.new('RGBA', (target_w, target_h), (255, 255, 255, 0))
final_img.paste(new_img, (0,0), mask=mask)

# Wait, looking at the user's attached image, it doesn't have white padding like a "card".
# The user's image IS the card content. If I just round the corners, it might look like a solid card.
# The original image was a white card with drop shadow (or maybe the shadow is in CSS?). 
# Let's just create a rounded card.

os.makedirs('Branding_stuff/cards', exist_ok=True)
save_path = 'Branding_stuff/cards/mf1-1.png'
final_img.save(save_path)
print(f"Generated {save_path} with attached image.")

# Update HTML for mf1-1
from bs4 import BeautifulSoup
print("Updating HTML...")
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
section = soup.find('section', class_='mf1-search-section')

if section:
    connector = section.find('div', id='search-connector-1')
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
