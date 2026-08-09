import re

html = open('index.html', 'r', encoding='utf-8').read()

# 1. Decrease scroll height
html = html.replace('height: 400vh;', 'height: 250vh;')

# 2. Inject SVG and ball into HTML
svg_and_ball = """
  <div class="soorma-roster-sticky">
      <!-- BALL TRAIL SVG -->
      <svg id="ball-svg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 50; pointer-events: none;">
          <defs>
              <mask id="trail-mask">
                  <path id="mask-path" fill="none" stroke="white" stroke-width="20" stroke-linecap="round"></path>
              </mask>
          </defs>
          <path id="ball-trail-dashed" fill="none" stroke="#f97316" stroke-width="3" stroke-dasharray="12, 12" mask="url(#trail-mask)" opacity="0.8"></path>
      </svg>
      <div id="soorma-cricket-ball" style="position: absolute; width: 16px; height: 16px; background: #ef4444; border-radius: 50%; border: 2px solid #fff; box-shadow: 0 0 10px rgba(239, 68, 68, 0.8); z-index: 51; transform: translate(-50%, -50%); opacity: 0; transition: opacity 0.3s; pointer-events: none;"></div>
"""
html = html.replace('<div class="soorma-roster-sticky">', svg_and_ball)

# 3. Replace the script block
new_script = """
  <script>
    document.addEventListener('DOMContentLoaded', () => {
        const rosterSection = document.querySelector('.soorma-roster-section');
        const slides = document.querySelectorAll('.soorma-slide');
        const ball = document.getElementById('soorma-cricket-ball');
        const maskPath = document.getElementById('mask-path');
        const dashedPath = document.getElementById('ball-trail-dashed');
        if (!rosterSection || slides.length === 0) return;
        
        let pathLength = 0;
        
        function drawPath() {
            const w = window.innerWidth;
            const h = window.innerHeight;
            // A sweeping S-curve: Top Right -> Mid Left -> Mid Right -> Bottom Left
            const d = `M ${w*0.85} ${h*0.25} C ${w*0.1} ${h*0.25}, ${w*0.1} ${h*0.5}, ${w*0.5} ${h*0.5} C ${w*0.9} ${h*0.5}, ${w*0.9} ${h*0.75}, ${w*0.15} ${h*0.75}`;
            
            maskPath.setAttribute('d', d);
            dashedPath.setAttribute('d', d);
            
            pathLength = maskPath.getTotalLength();
            maskPath.style.strokeDasharray = pathLength;
            maskPath.style.strokeDashoffset = pathLength;
        }
        
        drawPath();
        window.addEventListener('resize', drawPath);
        
        let activeIndex = 0;
        
        window.addEventListener('scroll', () => {
            const rect = rosterSection.getBoundingClientRect();
            const totalScrollable = rect.height - window.innerHeight;
            const scrolled = -rect.top;
            
            if (scrolled >= 0 && scrolled <= totalScrollable) {
                // Inside section
                const progress = scrolled / totalScrollable;
                
                // --- SLIDESHOW LOGIC ---
                let newIndex = Math.floor(progress * slides.length);
                if (newIndex >= slides.length) newIndex = slides.length - 1;
                
                if (newIndex !== activeIndex) {
                    slides.forEach((s, i) => {
                        s.classList.remove('active', 'incoming', 'outgoing');
                        if (i === newIndex) s.classList.add('active');
                        else if (i < newIndex) s.classList.add('outgoing');
                        else s.classList.add('incoming');
                    });
                    activeIndex = newIndex;
                }
                
                // --- BALL TRAIL LOGIC ---
                ball.style.opacity = 1;
                
                // We add a tiny buffer (e.g. progress spans from 0.05 to 0.95 visually) to ensure ball doesn't clip off edges instantly
                const clampedProgress = Math.min(Math.max(progress, 0.01), 0.99);
                
                const currentLength = pathLength * clampedProgress;
                maskPath.style.strokeDashoffset = pathLength - currentLength;
                
                const point = maskPath.getPointAtLength(currentLength);
                ball.style.left = point.x + 'px';
                ball.style.top = point.y + 'px';
                
            } else if (scrolled < 0) {
                // Above section
                ball.style.opacity = 0;
                if (activeIndex !== 0) {
                    slides.forEach(s => s.classList.remove('active', 'incoming', 'outgoing'));
                    slides[0].classList.add('active');
                    for (let i = 1; i < slides.length; i++) slides[i].classList.add('incoming');
                    activeIndex = 0;
                }
            } else {
                // Below section
                ball.style.opacity = 0;
                const lastIdx = slides.length - 1;
                if (activeIndex !== lastIdx) {
                    slides.forEach(s => s.classList.remove('active', 'incoming', 'outgoing'));
                    slides[lastIdx].classList.add('active');
                    for (let i = 0; i < lastIdx; i++) slides[i].classList.add('outgoing');
                    activeIndex = lastIdx;
                }
            }
        });
        
        // Trigger scroll once on load to position everything
        window.dispatchEvent(new Event('scroll'));
    });
  </script>
"""

# Replace old script with new script
html = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => {.*?const rosterSection = document\.querySelector\(\'\.soorma-roster-section\'\);.*?</script>', new_script, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Ball trail injected successfully.")
