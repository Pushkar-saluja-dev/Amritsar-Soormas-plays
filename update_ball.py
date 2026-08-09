import re

html = open('index.html', 'r', encoding='utf-8').read()

# Replace ball div with img
old_ball = '<div id="soorma-cricket-ball" style="position: absolute; width: 16px; height: 16px; background: #ef4444; border-radius: 50%; border: 2px solid #fff; box-shadow: 0 0 10px rgba(239, 68, 68, 0.8); z-index: 51; transform: translate(-50%, -50%); opacity: 0; transition: opacity 0.3s; pointer-events: none;"></div>'
new_ball = '<img src="Branding_stuff/cricket_ball.png" id="soorma-cricket-ball" style="position: absolute; width: 48px; height: 48px; z-index: 51; transform: translate(-50%, -50%); opacity: 0; transition: opacity 0.3s; pointer-events: none; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.5));" />'

html = html.replace(old_ball, new_ball)

# Replace the path in JS
old_path = "const d = `M ${w*0.85} ${h*0.25} C ${w*0.1} ${h*0.25}, ${w*0.1} ${h*0.5}, ${w*0.5} ${h*0.5} C ${w*0.9} ${h*0.5}, ${w*0.9} ${h*0.75}, ${w*0.15} ${h*0.75}`;"
new_path = """// A bumpy, looping path: Top Right -> Mid Left -> Mid Right -> Bottom Left
            const d = `M ${w*0.85} ${h*0.25} 
                       C ${w*0.5} ${h*0.05}, ${w*0.4} ${h*0.55}, ${w*0.15} ${h*0.4} 
                       C ${w*-0.1} ${h*0.25}, ${w*0.4} ${h*0.75}, ${w*0.85} ${h*0.55} 
                       C ${w*1.1} ${h*0.4}, ${w*0.5} ${h*0.95}, ${w*0.15} ${h*0.75}`;"""

html = html.replace(old_path, new_path)

# Add rotation to the ball in scroll listener
old_js_pos = """
                    const point = maskPath.getPointAtLength(currentLength);
                    ball.style.left = point.x + 'px';
                    ball.style.top = point.y + 'px';
"""

new_js_pos = """
                    const point = maskPath.getPointAtLength(currentLength);
                    ball.style.left = point.x + 'px';
                    ball.style.top = point.y + 'px';
                    ball.style.transform = `translate(-50%, -50%) rotate(${clampedProgress * 1440}deg)`;
"""

html = html.replace(old_js_pos, new_js_pos)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated ball and path successfully.")
