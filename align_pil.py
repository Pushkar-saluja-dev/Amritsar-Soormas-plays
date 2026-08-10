from PIL import Image

def get_real_bbox(img_path):
    img = Image.open(img_path).convert("RGBA")
    data = img.load()
    w, h = img.size
    min_x, min_y = w, h
    max_x, max_y = 0, 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = data[x, y]
            if a > 50:
                if x < min_x: min_x = x
                if y < min_y: min_y = y
                if x > max_x: max_x = x
                if y > max_y: max_y = y
    return min_x, min_y, max_x, max_y

print("img1 bbox:", get_real_bbox('Branding_stuff/Cricket bat no color.png'))
print("img2 bbox:", get_real_bbox('Branding_stuff/Cricket bat with color.png'))
