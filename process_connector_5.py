import os
import json
import base64
from PIL import Image, ImageDraw, ImageFont

# 1. Read base64
with open(r'C:\Users\pushk\.gemini\antigravity\brain\a0abc730-6056-45e9-ba56-bd063e93c63a\.system_generated\steps\2158\output.txt', 'r', encoding='utf-8') as f:
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
if data_url.startswith('data:'):
    b64_str = data_url.split(',')[1]
    img_data = base64.b64decode(b64_str)
    
    with open('connector_5_test.png', 'wb') as f:
        f.write(img_data)
    
    img = Image.open('connector_5_test.png').convert('RGBA')
    print(f"Connector 5 size: {img.size}")
else:
    print(f"Error: {data_url}")
