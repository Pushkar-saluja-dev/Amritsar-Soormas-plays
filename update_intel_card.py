import re
from bs4 import BeautifulSoup

html_content = open('index.html', 'r', encoding='utf-8').read()
soup = BeautifulSoup(html_content, 'html.parser')

css_tag = soup.find(id='custom-cards-css')
if css_tag:
    css = css_tag.string
    
    # We will completely replace the CSS for custom-card-5
    # First, let's remove everything from "/* Card 5: Answers (mf1-3) */" onwards, 
    # then append the new CSS for Card 5.
    css_parts = css.split('/* Card 5: Answers (mf1-3) */')
    base_css = css_parts[0]
    
    new_card_5_css = """
/* Card 5: Answers (mf1-3) */
.custom-card-5 {
  width: 100%;
  aspect-ratio: 451 / 452;
  padding: 6% 8%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.custom-card-5-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8%;
}
.custom-card-5-icon {
  width: 16px;
  height: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.custom-card-5-icon svg {
  width: 100%;
  height: 100%;
  fill: #1a1a1a;
}
.custom-card-5-top {
  font-size: 14px;
  font-weight: 700;
  color: #1a1a1a;
}
.custom-card-5-title {
  font-size: 16px;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 12%;
  color: #1a1a1a;
}
.custom-card-5-skeletons {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: auto;
}
.custom-card-5-skeleton {
  height: 8px;
  background: #bfdbfe;
  border-radius: 4px;
}
.custom-card-5-skeleton.long { width: 90%; }
.custom-card-5-skeleton.medium { width: 75%; }
.custom-card-5-skeleton.short { width: 65%; }

.custom-card-5-footer-text {
  font-size: 11px;
  color: #94a3b8;
  margin-bottom: 10px;
}
.custom-card-5-footer-icons {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4%;
}
.custom-card-5-footer-icons-left,
.custom-card-5-footer-icons-right {
  display: flex;
  gap: 12px;
}
.custom-card-5-footer-icon {
  width: 14px;
  height: 14px;
  fill: none;
  stroke: #475569;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}
</style>
"""
    css_tag.string.replace_with(base_css + new_card_5_css.replace('</style>', ''))

# Now replace the HTML for Card 5
card5_html = """
    <div class="mf1-hero-connector mf1-3 custom-card custom-card-5">
        <div>
            <div class="custom-card-5-header">
                <div class="custom-card-5-icon">
                    <svg viewBox="0 0 24 24"><path d="M12 2L14.4 9.6L22 12L14.4 14.4L12 22L9.6 14.4L2 12L9.6 9.6L12 2Z" fill="currentColor"/></svg>
                </div>
                <div class="custom-card-5-top">TEAM INTEL</div>
            </div>
            <div class="custom-card-5-title">THE SOORMA SQUAD</div>
            <div class="custom-card-5-skeletons">
                <div class="custom-card-5-skeleton long"></div>
                <div class="custom-card-5-skeleton medium"></div>
                <div class="custom-card-5-skeleton short"></div>
            </div>
        </div>
        <div>
            <div class="custom-card-5-footer-text">Was this helpful?</div>
            <div class="custom-card-5-footer-icons">
                <div class="custom-card-5-footer-icons-left">
                    <svg class="custom-card-5-footer-icon" viewBox="0 0 24 24"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg>
                    <svg class="custom-card-5-footer-icon" viewBox="0 0 24 24"><path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h3a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-3"></path></svg>
                </div>
                <div class="custom-card-5-footer-icons-right">
                    <svg class="custom-card-5-footer-icon" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    <svg class="custom-card-5-footer-icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                </div>
            </div>
        </div>
    </div>
"""

old_card5 = soup.find('div', class_=lambda c: c and 'mf1-3' in c and 'custom-card-5' in c)
if old_card5:
    old_card5.replace_with(BeautifulSoup(card5_html, 'html.parser'))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully replaced Card 5 with 1:1 original layout design.")
