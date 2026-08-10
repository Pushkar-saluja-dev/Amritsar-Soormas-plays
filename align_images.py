import cv2
import numpy as np
from PIL import Image

# Read both images in grayscale
img1 = cv2.imread('Branding_stuff/Cricket bat no color.png', 0)
img2 = cv2.imread('Branding_stuff/Cricket bat with color.png', 0)

print(f"img1 size: {img1.shape}")
print(f"img2 size: {img2.shape}")

# Use Template Matching to find the offset
# We will match the center of img1 in img2
h, w = img1.shape
cy, cx = h//2, w//2
# take a 400x400 patch from center of img1
patch_size = 400
patch = img1[cy-patch_size//2:cy+patch_size//2, cx-patch_size//2:cx+patch_size//2]

res = cv2.matchTemplate(img2, patch, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

print(f"Max match value: {max_val}")
print(f"Match location (top-left of patch): {max_loc}")
print(f"Expected location (if perfectly aligned): ({cx-patch_size//2}, {cy-patch_size//2})")

dx = max_loc[0] - (cx - patch_size//2)
dy = max_loc[1] - (cy - patch_size//2)
print(f"Offset (dx, dy): {dx}, {dy}")
