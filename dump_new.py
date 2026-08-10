from PIL import Image

idle = Image.open('Branding_stuff/Cricket bat no color square.png').convert("RGBA")
active = Image.open('Branding_stuff/Cricket bat with color square prescaled.png').convert("RGBA")

print("Idle max alpha:", idle.split()[3].getextrema())
print("Active max alpha:", active.split()[3].getextrema())
