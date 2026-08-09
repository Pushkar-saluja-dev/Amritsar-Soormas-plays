import re

html = open('index.html', 'r', encoding='utf-8').read()

# We need to replace the path definition inside the drawPath function.
# Let's extract the old exact hand-drawn path block.
old_block = """// Exact hand-drawn bouncing path stitched across 4 slides
            const d = `M ${w*0.5} ${h*0.05} 
                       Q ${w*0.8} ${h*0.1}, ${w*0.98} ${h*0.4} 
                       Q ${w*0.6} ${h*0.7}, ${w*0.05} ${h*0.95} 
                       Q ${w*0.02} ${h*0.5}, ${w*0.15} ${h*0.05} 
                       Q ${w*0.05} ${h*0.2}, ${w*0.02} ${h*0.4} 
                       Q ${w*0.15} ${h*0.3}, ${w*0.25} ${h*0.3} 
                       Q ${w*0.25} ${h*0.6}, ${w*0.35} ${h*0.95} 
                       Q ${w*0.55} ${h*0.7}, ${w*0.75} ${h*0.95} 
                       Q ${w*0.65} ${h*0.4}, ${w*0.45} ${h*0.05} 
                       Q ${w*0.48} ${h*0.15}, ${w*0.5} ${h*0.3} 
                       Q ${w*0.6} ${h*0.15}, ${w*0.7} ${h*0.3} 
                       Q ${w*0.8} ${h*0.15}, ${w*0.9} ${h*0.3} 
                       Q ${w*0.95} ${h*0.3}, ${w*0.98} ${h*0.4} 
                       Q ${w*0.85} ${h*0.6}, ${w*0.7} ${h*0.75} 
                       Q ${w*0.75} ${h*0.85}, ${w*0.75} ${h*0.95}`;"""

new_block = """// A sweeping S-curve: Top Right -> Mid Left -> Mid Right -> Bottom Left
            const d = `M ${w*0.85} ${h*0.25} C ${w*0.1} ${h*0.25}, ${w*0.1} ${h*0.5}, ${w*0.5} ${h*0.5} C ${w*0.9} ${h*0.5}, ${w*0.9} ${h*0.75}, ${w*0.15} ${h*0.75}`;"""

if old_block in html:
    html = html.replace(old_block, new_block)
else:
    print("Could not find the block to replace!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Reverted to original path.")
