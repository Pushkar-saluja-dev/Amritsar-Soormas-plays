from PIL import Image
import os

img1 = Image.open('Branding_stuff/Cricket bat no color square.png').convert('RGBA')
img2 = Image.open('Branding_stuff/Cricket bat with color square.png').convert('RGBA')

# composite img2 over img1 to see if they overlap properly
res = Image.alpha_composite(img1, img2)
res = res.resize((800, 800))
res.save('overlap_squares.png')
