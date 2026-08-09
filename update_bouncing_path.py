import re

html = open('index.html', 'r', encoding='utf-8').read()

old_path = """// A bumpy, looping path: Top Right -> Mid Left -> Mid Right -> Bottom Left
            const d = `M ${w*0.85} ${h*0.25} 
                       C ${w*0.5} ${h*0.05}, ${w*0.4} ${h*0.55}, ${w*0.15} ${h*0.4} 
                       C ${w*-0.1} ${h*0.25}, ${w*0.4} ${h*0.75}, ${w*0.85} ${h*0.55} 
                       C ${w*1.1} ${h*0.4}, ${w*0.5} ${h*0.95}, ${w*0.15} ${h*0.75}`;"""

# Bouncing path with sharp angles
new_path = """// Sharp bouncing ricochet path
            const d = `M ${w*0.85} ${h*0.25} 
                       L ${w*0.85} ${h*0.65} 
                       L ${w*0.15} ${h*0.95} 
                       L ${w*0.05} ${h*0.45} 
                       L ${w*0.50} ${h*0.05} 
                       L ${w*0.90} ${h*0.60} 
                       L ${w*0.25} ${h*0.85}`;"""

html = html.replace(old_path, new_path)

# Let's ensure SVG stroke-linejoin is set to round so the sharp corners don't look broken
old_svg_dashed = 'stroke-dasharray="12, 12" mask="url(#trail-mask)" opacity="0.8"'
new_svg_dashed = 'stroke-dasharray="12, 12" stroke-linejoin="round" mask="url(#trail-mask)" opacity="0.8"'
html = html.replace(old_svg_dashed, new_svg_dashed)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated to bouncing path successfully.")
