import os
import json
import base64
from PIL import Image, ImageDraw, ImageFont

# 1. Read base64
with open(r'C:\Users\pushk\.gemini\antigravity\brain\a0abc730-6056-45e9-ba56-bd063e93c63a\.system_generated\steps\2104\output.txt', 'r', encoding='utf-8') as f:
    content = f.read()

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

os.makedirs('Branding_stuff/cards', exist_ok=True)
with open('original_connector_0.png', 'wb') as f:
    f.write(img_data)

img = Image.open('original_connector_0.png').convert('RGBA')
w, h = img.size
print(f"Original image size: {w}x{h}")

draw = ImageDraw.Draw(img)

# Find the background color near the top (this image looks like a white card with rounded corners)
# Actually, the user screenshot shows a plain white background at the top where the logo and text are.
# Let's sample a color from the top center
bg_color = img.getpixel((w//2, 40))
print(f"Background color: {bg_color}")
if bg_color[3] == 0:
    # If transparent, maybe it's not a card background but a cutout?
    bg_color = (248, 248, 248, 255)

# Blank out the logo and text. They are usually at the top left.
# For a 1080x1080 image, the top section is usually from y=20 to y=150.
# We will just draw a rectangle over the whole top area except the corners.
# Let's just draw over the text/logo specifically.
draw.rectangle([40, 20, w - 40, int(h * 0.15)], fill=bg_color)

# Write the new text
text = "2026 Soormas Marketing materials"
text_color = (0, 0, 0, 255)
font_size = int(w * 0.04) # e.g. ~43px for 1080px
try:
    font = ImageFont.truetype("arialbd.ttf", size=font_size)
except:
    try:
        font = ImageFont.truetype("arial.ttf", size=font_size)
    except:
        font = ImageFont.load_default()

# Draw the text at the top, slightly inset
draw.text((80, 50), text, fill=text_color, font=font)

# Save the new image
save_path = 'Branding_stuff/cards/mf1-connector-0-v2.png'
img.save(save_path)
print(f"Saved modified image to {save_path}")

# Update index.html to override the background image
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

override_style = f"""
<style>
.mf1-connector-image.mf1-connector-image-0.is-v2 {{
    background-image: url("Branding_stuff/cards/mf1-connector-0-v2.png?v=1") !important;
}}
</style>
"""

# Inject before </head> if not already there
if "mf1-connector-0-v2.png" not in html:
    html = html.replace('</head>', override_style + '</head>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML updated with override style.")
else:
    print("HTML already contains the override style.")
