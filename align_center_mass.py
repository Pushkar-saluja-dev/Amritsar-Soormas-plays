import cv2
import numpy as np
from PIL import Image

# load images
img1 = np.array(Image.open('Branding_stuff/Cricket bat no color.png').convert('RGBA'))
img2 = np.array(Image.open('Branding_stuff/Cricket bat with color.png').convert('RGBA'))

# extract alpha channels
alpha1 = img1[:, :, 3]
alpha2 = img2[:, :, 3]

# let's find the center of mass of the highly opaque pixels
y1, x1 = np.where(alpha1 > 200)
cy1, cx1 = np.mean(y1), np.mean(x1)

y2, x2 = np.where(alpha2 > 200)
cy2, cx2 = np.mean(y2), np.mean(x2)

print(f"Center of mass for uncolored bat: {cx1}, {cy1}")
print(f"Center of mass for colored bat: {cx2}, {cy2}")

dx = cx1 - cx2
dy = cy1 - cy2

print(f"Rough offset to align color bat to uncolored bat: dx={dx}, dy={dy}")
