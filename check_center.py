from PIL import Image

img = Image.open('Branding_stuff/Cricket bat with color square.png').convert("RGBA")
pixels = img.load()

center_x, center_y = img.width // 2, img.height // 2
print(f"Center pixel: {pixels[center_x, center_y]}")
print(f"Pixel at 1980, 2480: {pixels[1980, 2480]}")

# Find any opaque pixel
opaque_pixels = [(x, y) for x in range(img.width) for y in range(img.height) if pixels[x, y][3] > 0]
if opaque_pixels:
    print(f"Found {len(opaque_pixels)} opaque pixels.")
    print(f"First opaque pixel at: {opaque_pixels[0]}")
    print(f"Last opaque pixel at: {opaque_pixels[-1]}")
    import random
    print(f"Sample opaque pixels: {random.sample(opaque_pixels, min(5, len(opaque_pixels)))}")
else:
    print("No opaque pixels found!")
