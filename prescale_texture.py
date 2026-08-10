from PIL import Image

# We need to scale the active texture down by 0.95 around the center
img = Image.open('Branding_stuff/Cricket bat with color square.png').convert("RGBA")
w, h = img.size

# We want the image to be 0.95 times its original size, centered in the same canvas
new_w = int(w * 0.95)
new_h = int(h * 0.95)

scaled_img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
final_img = Image.new("RGBA", (w, h), (255, 255, 255, 0))

x = (w - new_w) // 2
y = (h - new_h) // 2

final_img.paste(scaled_img, (x, y), scaled_img)
final_img.save('Branding_stuff/Cricket bat with color square prescaled.png')
print("Saved prescaled texture")
