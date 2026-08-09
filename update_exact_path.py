import re

html = open('index.html', 'r', encoding='utf-8').read()

old_path = """// Sharp bouncing ricochet path
            const d = `M ${w*0.85} ${h*0.25} 
                       L ${w*0.85} ${h*0.65} 
                       L ${w*0.15} ${h*0.95} 
                       L ${w*0.05} ${h*0.45} 
                       L ${w*0.50} ${h*0.05} 
                       L ${w*0.90} ${h*0.60} 
                       L ${w*0.25} ${h*0.85}`;"""

new_path = """// Exact hand-drawn bouncing path stitched across 4 slides
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

html = html.replace(old_path, new_path)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated to exact hand-drawn path.")
