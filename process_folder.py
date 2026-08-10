import os
import json
import base64
from PIL import Image, ImageDraw, ImageFont

# 1. Read base64 from output.txt
with open(r'C:\Users\pushk\.gemini\antigravity\brain\a0abc730-6056-45e9-ba56-bd063e93c63a\.system_generated\steps\2054\output.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse the JSON string out of the output
lines = content.split('\n')
json_str = ""
in_json = False
for line in lines:
    if line.startswith('```json'):
        in_json = True
        continue
    if line.startswith('```') and in_json:
        break
    if in_json:
        json_str += line

data_url = json.loads(json_str)
b64_str = data_url.split(',')[1]
img_data = base64.b64decode(b64_str)

# 2. Save original image
with open('original_folder.png', 'wb') as f:
    f.write(img_data)

img = Image.open('original_folder.png').convert('RGBA')
w, h = img.size
print(f"Original image size: {w}x{h}")

# 3. Edit the image
# It's a white card with a blue folder. The text "2026 McLaren Marketing Materials" and Dropbox logo are at the top left.
# Let's inspect the top area (say y=0 to 100).
# Actually, I can just draw a white rectangle over the top area to hide the logo and text, and write the new text!
# Let's write the new text "2026 Soormas Marketing materials".

draw = ImageDraw.Draw(img)

# The user screenshot shows the Dropbox logo and text at the very top.
# Let's blank out the area. We assume the text and logo are roughly x=30 to x=600, y=30 to y=80.
# Instead of guessing the exact color, we can sample the background.
# Since it's a white card with a folder, the background near the top left is probably just white or very light gray.
bg_color = img.getpixel((10, 10)) # or we can just use white, or fill it with the color around the logo.
print(f"Background color at 10,10: {bg_color}")

# Draw a rectangle to cover the logo and text.
# The logo and text in the screenshot appear to be on a white-ish background.
# Wait, let's just make it a clean cover. We'll use the color at x=100, y=10.
cover_color = (248, 248, 248, 255) # light gray/white typical of these cards.
draw.rectangle([40, 40, w - 40, 100], fill=img.getpixel((w//2, 20))) # use color from top center

# Write the new text
text = "2026 Soormas Marketing materials"
text_color = (0, 0, 0, 255) # Black text
try:
    font = ImageFont.truetype("arialbd.ttf", size=max(24, int(w*0.035)))
except:
    try:
        font = ImageFont.truetype("arial.ttf", size=max(24, int(w*0.035)))
    except:
        font = ImageFont.load_default()

# The text should be positioned where the old text was.
draw.text((100, 50), text, fill=text_color, font=font)

# Save the updated image to Branding_stuff/cards/folder.png
os.makedirs('Branding_stuff/cards', exist_ok=True)
save_path = 'Branding_stuff/cards/folder.png'
img.save(save_path)
print(f"Saved modified image to {save_path}")

# Update HTML to use this image
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
html = re.sub(r"url\('https://cdn\.prod\.website-files\.com/[^']+_Folder-p-500\.png'\)", f"url('{save_path}')", html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML updated.")
