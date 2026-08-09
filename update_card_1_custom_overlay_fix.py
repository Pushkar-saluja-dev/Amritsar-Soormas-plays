import os
import glob
import urllib.request
from PIL import Image, ImageDraw, ImageFont
import io

upload_dir = r'C:\Users\pushk\.gemini\antigravity\brain\a0abc730-6056-45e9-ba56-bd063e93c63a\.user_uploaded'
files = glob.glob(os.path.join(upload_dir, '*.*'))
files.sort(key=os.path.getctime, reverse=True)

img_path = files[0]
user_img = Image.open(img_path)

url = 'https://cdn.prod.website-files.com/65dcd70b48edc3a7b446950e/69c26127ed6f045a9f7b71e3_Dropbox%20(2).png'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    img_data = response.read()
    original_img = Image.open(io.BytesIO(img_data)).convert("RGBA")
    
target_w, target_h = original_img.size

draw = ImageDraw.Draw(original_img)
# 634x495 is the total size.
# Paint over logo, but be careful not to hit the B!
# Let's say logo is x: 25 to 88, y: 30 to 90.
draw.rectangle([25, 20, 85, 95], fill=(255, 255, 255, 255)) 

box_pad = 30
box_y0 = 120
box_y1 = target_h - 30
box_x0 = 30
box_x1 = target_w - 30

box_w = box_x1 - box_x0
box_h = box_y1 - box_y0

user_w, user_h = user_img.size
aspect_user = user_w / user_h
aspect_box = box_w / box_h

if aspect_user > aspect_box:
    new_h = box_h
    new_w = int(new_h * aspect_user)
    resized_user = user_img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - box_w) // 2
    cropped_user = resized_user.crop((left, 0, left + box_w, box_h))
else:
    new_w = box_w
    new_h = int(new_w / aspect_user)
    resized_user = user_img.resize((new_w, new_h), Image.LANCZOS)
    top = (new_h - box_h) // 2
    cropped_user = resized_user.crop((0, top, box_w, top + box_h))

inner_mask = Image.new("L", (box_w, box_h), 0)
inner_draw = ImageDraw.Draw(inner_mask)
inner_draw.rounded_rectangle([0, 0, box_w, box_h], radius=16, fill=255)

original_img.paste(cropped_user, (box_x0, box_y0), mask=inner_mask)

save_path = 'Branding_stuff/cards/mf1-1.png'
original_img.save(save_path)
print(f"Generated {save_path} with fixed B.")
