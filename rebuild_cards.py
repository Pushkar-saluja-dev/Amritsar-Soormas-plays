import re
from bs4 import BeautifulSoup

html_content = open('index.html', 'r', encoding='utf-8').read()
soup = BeautifulSoup(html_content, 'html.parser')

css = """
<style id="custom-cards-css">
.custom-card {
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.12);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: #1a1a1a;
  box-sizing: border-box;
}
.custom-card-placeholder {
  background: #e2e8f0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #64748b;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  text-align: center;
}

/* Card 1: Video (mf1-1) */
.custom-card-1 {
  width: 100%;
  aspect-ratio: 874 / 652;
  padding: 4%;
}
.custom-card-1 .custom-card-placeholder {
  flex: 1;
  border-radius: 8px;
  margin-bottom: 4%;
}
.custom-card-1-footer {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 0 4px 4px 4px;
}
.custom-card-1-icon {
  width: 16px;
  height: 16px;
  background: #0061FE; /* Dropbox blue placeholder color */
  border-radius: 4px;
}
.custom-card-1-text {
  display: flex;
  flex-direction: column;
}
.custom-card-1-title {
  font-size: 11px;
  font-weight: 700;
  line-height: 1.2;
}
.custom-card-1-sub {
  font-size: 9px;
  color: #64748b;
}

/* Card 2: Document (mf1-4) */
.custom-card-2 {
  width: 100%;
  aspect-ratio: 518 / 728;
  padding: 6%;
}
.custom-card-2-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8%;
}
.custom-card-2-icon {
  width: 16px;
  height: 16px;
  background: #4285F4; /* Docs blue */
  border-radius: 2px;
}
.custom-card-2-title {
  font-size: 12px;
  font-weight: 700;
}
.custom-card-2-toolbar {
  display: flex;
  gap: 4px;
  margin-bottom: 12%;
  border-bottom: 1px solid #e2e8f0;
  padding-bottom: 6%;
}
.custom-card-2-tool {
  width: 12px;
  height: 12px;
  background: #cbd5e1;
  border-radius: 2px;
}
.custom-card-2-body {
  font-size: 10px;
  line-height: 1.6;
  color: #334155;
}
.custom-card-2-body strong {
  color: #0f172a;
  font-size: 11px;
  display: block;
  margin-bottom: 8%;
}

/* Card 3: Avatars (mf1-5) */
.custom-card-3 {
  width: 100%;
  aspect-ratio: 422 / 159;
  border-radius: 40px;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 4% 6%;
  gap: -10px;
}
.custom-card-3-avatars {
  display: flex;
  flex: 1;
}
.custom-card-3-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #cbd5e1;
  border: 2px solid white;
  margin-left: -8px;
}
.custom-card-3-avatar:first-child { margin-left: 0; }
.custom-card-3-badge {
  background: #f1f5f9;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 700;
  color: #334155;
  margin-left: auto;
}

/* Card 4: Photo (mf1-2) */
.custom-card-4 {
  width: 100%;
  aspect-ratio: 584 / 816;
}
.custom-card-4-header {
  padding: 6% 6% 4% 6%;
}
.custom-card-4-top {
  font-size: 9px;
  color: #64748b;
  margin-bottom: 2px;
  text-transform: uppercase;
}
.custom-card-4-title {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 2px;
}
.custom-card-4-sub {
  font-size: 8px;
  color: #94a3b8;
}
.custom-card-4-placeholder-wrapper {
  padding: 0 6% 6% 6%;
  flex: 1;
  display: flex;
}
.custom-card-4 .custom-card-placeholder {
  flex: 1;
  border-radius: 8px;
}

/* Card 5: Answers (mf1-3) */
.custom-card-5 {
  width: 100%;
  aspect-ratio: 451 / 452;
  padding: 8%;
}
.custom-card-5-header {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 8%;
}
.custom-card-5-icon {
  width: 14px;
  height: 14px;
  background: #10b981; /* Green sparkle */
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
}
.custom-card-5-top {
  font-size: 11px;
  font-weight: 700;
}
.custom-card-5-title {
  font-size: 13px;
  font-weight: 800;
  margin-bottom: 10%;
}
.custom-card-5-skeleton {
  height: 6px;
  background: #e2e8f0;
  border-radius: 3px;
  margin-bottom: 6%;
}
.custom-card-5-skeleton.short { width: 60%; }
.custom-card-5-skeleton.medium { width: 80%; }
.custom-card-5-skeleton.long { width: 100%; background: #bfdbfe; }
</style>
"""

# Insert CSS into head
if not soup.find(id='custom-cards-css'):
    soup.head.append(BeautifulSoup(css, 'html.parser'))

# Replace Card 1 (mf1-1)
card1_a = soup.find('a', class_=lambda c: c and 'mf1-1' in c)
if card1_a:
    card1_html = """
    <div class="mf1-hero-connector mf1-1 custom-card custom-card-1">
        <div class="custom-card-placeholder">IMAGE TO BE ADDED</div>
        <div class="custom-card-1-footer">
            <div class="custom-card-1-icon"></div>
            <div class="custom-card-1-text">
                <div class="custom-card-1-title">MATCHDAY MOMENT</div>
                <div class="custom-card-1-sub">SOORMAS_MATCHDAY_2026_16x9</div>
            </div>
        </div>
    </div>
    """
    card1_a.replace_with(BeautifulSoup(card1_html, 'html.parser'))

# Replace Card 2 (mf1-4)
card2_img = soup.find('img', class_=lambda c: c and 'mf1-4' in c)
if card2_img:
    card2_html = """
    <div class="mf1-hero-connector mf1-4 custom-card custom-card-2">
        <div class="custom-card-2-header">
            <div class="custom-card-2-icon"></div>
            <div class="custom-card-2-title">2026 TEAM BRIEF</div>
        </div>
        <div class="custom-card-2-toolbar">
            <div class="custom-card-2-tool"></div><div class="custom-card-2-tool"></div><div class="custom-card-2-tool"></div>
        </div>
        <div class="custom-card-2-body">
            <strong>AMRITSAR SOORMAS<br>2026 SEASON</strong>
            Team<br>
            Squad<br>
            Matchday<br>
            Campaign
        </div>
    </div>
    """
    card2_img.replace_with(BeautifulSoup(card2_html, 'html.parser'))

# Replace Card 3 (mf1-5)
card3_img = soup.find('img', class_=lambda c: c and 'mf1-5' in c)
if card3_img:
    card3_html = """
    <div class="mf1-hero-connector mf1-5 custom-card custom-card-3">
        <div class="custom-card-3-avatars">
            <div class="custom-card-3-avatar"></div>
            <div class="custom-card-3-avatar"></div>
            <div class="custom-card-3-avatar"></div>
        </div>
        <div class="custom-card-3-badge">TEAM</div>
    </div>
    """
    card3_img.replace_with(BeautifulSoup(card3_html, 'html.parser'))

# Replace Card 4 (mf1-2)
card4_img = soup.find('img', class_=lambda c: c and 'mf1-2' in c)
if card4_img:
    card4_html = """
    <div class="mf1-hero-connector mf1-2 custom-card custom-card-4">
        <div class="custom-card-4-header">
            <div class="custom-card-4-top">SOORMAS MEDIA</div>
            <div class="custom-card-4-title">MATCHDAY PHOTOS</div>
            <div class="custom-card-4-sub">AMRITSAR SOORMAS — 2026</div>
        </div>
        <div class="custom-card-4-placeholder-wrapper">
            <div class="custom-card-placeholder">IMAGE TO BE ADDED</div>
        </div>
    </div>
    """
    card4_img.replace_with(BeautifulSoup(card4_html, 'html.parser'))

# Replace Card 5 (mf1-3)
card5_img = soup.find('img', class_=lambda c: c and 'mf1-3' in c)
if card5_img:
    card5_html = """
    <div class="mf1-hero-connector mf1-3 custom-card custom-card-5">
        <div class="custom-card-5-header">
            <div class="custom-card-5-icon"></div>
            <div class="custom-card-5-top">TEAM INTEL</div>
        </div>
        <div class="custom-card-5-title">THE SOORMA SQUAD</div>
        <div class="custom-card-5-skeleton long"></div>
        <div class="custom-card-5-skeleton medium"></div>
        <div class="custom-card-5-skeleton short"></div>
    </div>
    """
    card5_img.replace_with(BeautifulSoup(card5_html, 'html.parser'))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully replaced all 5 cards with HTML/CSS components.")
