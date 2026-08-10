import os
from PIL import Image, ImageDraw, ImageFont
import urllib.request
import io
import glob

# 1. Load original card image (to get the bottom strip)
original_img = Image.open('test_card.png').convert('RGBA')
w, h = original_img.size

# 2. Get the user's original uploaded image for Brand Guidelines
# The script ran around 1786306806000. Let's find the largest image around that time, or just use media__1786306806000.png
upload_dir = r'C:\Users\pushk\.gemini\antigravity\brain\a0abc730-6056-45e9-ba56-bd063e93c63a\.user_uploaded'
user_img_path = os.path.join(upload_dir, 'media__1786306806000.png')
if not os.path.exists(user_img_path):
    print("User image not found. Using current mf1-1.png as base.")
    user_img = Image.open('Branding_stuff/cards/mf1-1.png')
else:
    user_img = Image.open(user_img_path)

# 3. Create a new image
new_img = Image.new('RGBA', (w, h), (255, 255, 255, 0))

# 4. Process the user image to fit the top portion (y=0 to 450)
target_w = w
target_h = 450
user_w, user_h = user_img.size
aspect_user = user_w / user_h
aspect_box = target_w / target_h

if aspect_user > aspect_box:
    new_h = target_h
    new_w = int(new_h * aspect_user)
    resized_user = user_img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - target_w) // 2
    cropped_user = resized_user.crop((left, 0, left + target_w, target_h))
else:
    new_w = target_w
    new_h = int(new_w / aspect_user)
    resized_user = user_img.resize((new_w, new_h), Image.LANCZOS)
    top = (new_h - target_h) // 2
    cropped_user = resized_user.crop((0, top, target_w, top + target_h))

new_img.paste(cropped_user, (0, 0))

# 5. Paste the bottom strip from original_img
bottom_strip = original_img.crop((0, 450, w, h))
new_img.paste(bottom_strip, (0, 450))

# 6. Blank out the Dropbox logo and text in the bottom strip
# We'll just draw a rectangle over it.
draw = ImageDraw.Draw(new_img)
bg_color = (243, 248, 255, 255)
# The text and logo are roughly x=30 to x=300, y=455 to 490
draw.rectangle([30, 455, 450, 490], fill=bg_color)

# 7. Write the new text
text = "2026 Soormas Marketing materials"
text_color = (83, 86, 91, 255) # Dark gray from before
try:
    font = ImageFont.truetype("arial.ttf", size=18)
except:
    font = ImageFont.load_default()

# We need to position it where the old text was. Let's just put it at x=30, y=462
draw.text((30, 463), text, fill=text_color, font=font)

# 8. Apply rounded corners mask
mask = Image.new("L", (w, h), 0)
draw_mask = ImageDraw.Draw(mask)
draw_mask.rounded_rectangle([0, 0, w, h], radius=24, fill=255)

final_img = Image.new('RGBA', (w, h), (255, 255, 255, 0))
final_img.paste(new_img, (0, 0), mask=mask)

# 9. Save it
save_path = 'Branding_stuff/cards/mf1-1.png'
final_img.save(save_path)
print(f"Generated {save_path}")

# Update HTML cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
html = re.sub(r'src="Branding_stuff/cards/mf1-1\.png(\?v=\d+)?"', 'src="Branding_stuff/cards/mf1-1.png?v=3"', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML updated.")
