import os
import glob
from PIL import Image, ImageDraw, ImageFont

upload_dir = r'C:\Users\pushk\.gemini\antigravity\brain\a0abc730-6056-45e9-ba56-bd063e93c63a\.user_uploaded'
files = glob.glob(os.path.join(upload_dir, '*.*'))
files.sort(key=os.path.getctime, reverse=True)

# The most recent is media__1786306848156.jpg (320x201)
img_path = files[0]
user_img = Image.open(img_path)
print(f"Selected {img_path} ({user_img.size[0]}x{user_img.size[1]})")

# Original mf1-5 card size
target_w, target_h = 688, 524
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
title = 'PracticeSession_26.mp4'
try:
    font = ImageFont.truetype("arial.ttf", size=max(16, int(target_w*0.04)))
except:
    font = ImageFont.load_default()
    
draw.text((padding + 20, target_h - padding - 40), title, fill=(0, 0, 0, 255), font=font)

os.makedirs('Branding_stuff/cards', exist_ok=True)
save_path = 'Branding_stuff/cards/mf1-5.png'
new_img.save(save_path)
print(f"Generated {save_path} with attached image.")
