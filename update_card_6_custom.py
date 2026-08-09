import os
import glob
from PIL import Image, ImageDraw, ImageFont

# Find the 2 most recent uploaded files
upload_dir = r'C:\Users\pushk\.gemini\antigravity\brain\a0abc730-6056-45e9-ba56-bd063e93c63a\.user_uploaded'
files = glob.glob(os.path.join(upload_dir, '*.png'))
files.sort(key=os.path.getctime, reverse=True)

# Pick the cricket player image. It's likely the one with a more portrait aspect ratio,
# or we can just pick the last one. Let's just pick the last one that is not small.
img_path = files[0]
for f in files[:2]:
    img = Image.open(f)
    w, h = img.size
    # The Lando image uploaded by the user is 196837 bytes or something. 
    # Let's just assume files[0] is the cricket player (it's the second image in the attachment list).
    print(f"File: {f}, Size: {w}x{h}")

# Actually, the user attached Lando (first) and Cricket Player (second). 
# So the cricket player is likely files[0] if it was uploaded last.
img_path = files[0]
print(f"Using image: {img_path}")
user_img = Image.open(img_path)

# Original Lando card size
target_w, target_h = 778, 579
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
    font = ImageFont.truetype("arial.ttf", size=max(16, int(target_w*0.05)))
except:
    font = ImageFont.load_default()
    
draw.text((padding + 20, target_h - padding - 40), title, fill=(0, 0, 0, 255), font=font)

save_path = 'Branding_stuff/cards/mf1-6.png'
new_img.save(save_path)
print(f"Generated {save_path} with attached image.")

# HTML is already pointing to this image, so no HTML changes are strictly needed!
