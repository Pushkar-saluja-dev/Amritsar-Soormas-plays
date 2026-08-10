from PIL import Image

def pad_to_square(img_path, out_path, size=4000):
    img = Image.open(img_path).convert("RGBA")
    old_width, old_height = img.size
    
    # Calculate scale if the image is too big, though 3192x1312 fits in 4000x4000
    ratio = min(size/old_width, size/old_height)
    if ratio < 1:
        new_w = int(old_width * ratio)
        new_h = int(old_height * ratio)
        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    else:
        new_w, new_h = old_width, old_height
        
    new_img = Image.new("RGBA", (size, size), (255, 255, 255, 0)) # transparent
    x = (size - new_w) // 2
    y = (size - new_h) // 2
    
    new_img.paste(img, (x, y), img)
    new_img.save(out_path)
    print(f"Saved {out_path} at size {new_img.size}")

pad_to_square("Branding_stuff/Cricket bat no color.png", "Branding_stuff/Cricket bat no color square.png")
pad_to_square("Branding_stuff/Cricket bat with color.png", "Branding_stuff/Cricket bat with color square.png")
