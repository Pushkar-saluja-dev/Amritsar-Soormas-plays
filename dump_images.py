from PIL import Image
import os

img1 = Image.open('Branding_stuff/Cricket bat no color.png').convert('RGBA')
img2 = Image.open('Branding_stuff/Cricket bat with color.png').convert('RGBA')

# composite img2 over img1 to see if they overlap properly
res = Image.alpha_composite(img1.resize((3192, 1312)), img2.resize((3192, 1312)))
res = res.resize((800, 328))
res.save('overlap.png')
