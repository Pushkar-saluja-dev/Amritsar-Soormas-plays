from PIL import Image

# 1. Load the original bat images
idle_orig = Image.open('Branding_stuff/Cricket bat no color.png').convert('RGBA')
active_orig = Image.open('Branding_stuff/Cricket bat with color.png').convert('RGBA')

# 2. Scale them down to fit 3600x1200
scale_factor = min(3600 / float(active_orig.width), 1200 / float(active_orig.height))

idle_scaled = idle_orig.resize((int(idle_orig.width * scale_factor), int(idle_orig.height * scale_factor)), Image.Resampling.LANCZOS)
active_scaled = active_orig.resize((int(active_orig.width * scale_factor), int(active_orig.height * scale_factor)), Image.Resampling.LANCZOS)

# 3. Create the 4000x4000 canvases
idle_canvas = Image.new('RGBA', (4000, 4000), (255, 255, 255, 0))
active_canvas = Image.new('RGBA', (4000, 4000), (255, 255, 255, 0))

# 4. Paste the scaled bats into the center
idle_offset = ((4000 - idle_scaled.width) // 2, (4000 - idle_scaled.height) // 2)
active_offset = ((4000 - active_scaled.width) // 2, (4000 - active_scaled.height) // 2)

idle_canvas.paste(idle_scaled, idle_offset, idle_scaled)
active_canvas.paste(active_scaled, active_offset, active_scaled)

# 5. Save the output
idle_canvas.save('Branding_stuff/Cricket bat no color square.png')
active_canvas.save('Branding_stuff/Cricket bat with color square.png')
print('Done!')
