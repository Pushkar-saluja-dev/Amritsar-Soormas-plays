import cv2
import numpy as np
from PIL import Image

# load images using cv2
img1 = cv2.imread('Branding_stuff/Cricket bat no color.png', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('Branding_stuff/Cricket bat with color.png', cv2.IMREAD_UNCHANGED)

# extract alpha channels
alpha1 = img1[:, :, 3]
alpha2 = img2[:, :, 3]

# find bounding box of alpha2
y_indices, x_indices = np.where(alpha2 > 50)
y_min, y_max = np.min(y_indices), np.max(y_indices)
x_min, x_max = np.min(x_indices), np.max(x_indices)

print(f"Bounding box of color bat: x=({x_min},{x_max}), y=({y_min},{y_max})")

# crop the color bat (the splice)
patch_color = img2[y_min:y_max, x_min:x_max]
patch_alpha = alpha2[y_min:y_max, x_min:x_max]

# template match the alpha channels!
# we will match the shape of the splice (patch_alpha) against the full bat (alpha1)
res = cv2.matchTemplate(alpha1, patch_alpha, cv2.TM_CCORR_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

print(f"Best match for the splice in the uncolored bat is at: {max_loc}")
dx = max_loc[0] - x_min
dy = max_loc[1] - y_min
print(f"To align the color bat with the uncolored bat, shift it by: dx={dx}, dy={dy}")
