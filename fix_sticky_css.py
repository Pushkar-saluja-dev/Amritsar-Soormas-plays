import re

html = open('index.html', 'r', encoding='utf-8').read()

sticky_roster_css = """
/* Soorma Roster Sections - Sticky Scroll Mode */
.soorma-roster-section {
  position: relative;
  background-color: #000;
  color: #fff;
  height: 400vh; /* 4 slides */
  width: 100%;
  padding: 0;
  display: block;
  font-family: Inter, sans-serif;
}

.soorma-roster-sticky {
  position: sticky;
  top: 0;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  background-color: #000;
}

.soorma-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.8s ease, transform 0.8s ease;
  pointer-events: none;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0 5%;
}

.soorma-slide.active {
  opacity: 1;
  pointer-events: all;
  transform: translateY(0);
}

.soorma-slide.incoming {
  transform: translateY(20px);
}

.soorma-slide.outgoing {
  transform: translateY(-20px);
}

/* MARQUEE */
#slide-marquee {
  justify-content: center;
}
.soorma-marquee-bg-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: clamp(80px, 15vw, 240px);
  font-weight: 900;
  color: #1a1a1a;
  white-space: nowrap;
  line-height: 0.8;
  z-index: 0;
  letter-spacing: -0.05em;
  text-align: center;
}
.soorma-marquee-content {
  position: relative;
  z-index: 10;
  display: flex;
  width: 100%;
  max-width: 1400px;
  align-items: center;
  justify-content: space-between;
}
.soorma-marquee-left {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 30px;
}
.soorma-marquee-meta {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.soorma-marquee-meta span {
  font-size: 11px;
  color: #f97316; /* Orange accent */
  letter-spacing: 2px;
  text-transform: uppercase;
  font-weight: 700;
}
.soorma-marquee-meta strong {
  font-size: 16px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
}
.pulse-dot {
  width: 8px;
  height: 8px;
  background: #ef4444;
  border-radius: 50%;
  box-shadow: 0 0 10px #ef4444;
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(239, 68, 68, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
}

.soorma-marquee-stats {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 8px 16px;
  margin-top: 20px;
}
.soorma-marquee-stats span {
  font-size: 12px;
  color: #94a3b8;
  text-transform: uppercase;
  font-weight: 600;
}
.soorma-marquee-stats strong {
  font-size: 14px;
  font-weight: 700;
}

.soorma-marquee-center {
  flex: 2;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
.soorma-marquee-center-frame {
  position: relative;
  padding: 20px;
}
.soorma-marquee-center-frame::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  border: 1px solid #f97316;
  transform: rotate(-3deg);
  border-radius: 20px;
  z-index: -1;
  opacity: 0.5;
  transition: transform 0.5s ease;
}
.soorma-marquee-center:hover .soorma-marquee-center-frame::before {
  transform: rotate(0deg) scale(1.05);
  opacity: 1;
}
.soorma-marquee-img {
  width: 100%;
  max-width: 400px;
  height: auto;
  object-fit: contain;
  filter: drop-shadow(0 20px 40px rgba(0,0,0,0.5));
  transition: transform 0.5s ease;
}
.soorma-marquee-center:hover .soorma-marquee-img {
  transform: scale(1.05) translateY(-10px);
}

.soorma-marquee-right {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: flex-end;
}
.soorma-btn {
  padding: 16px 32px;
  border-radius: 40px;
  font-weight: 700;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 1px;
  text-decoration: none;
  transition: all 0.3s ease;
  text-align: center;
  min-width: 200px;
}
.soorma-btn-primary {
  background: #3b82f6;
  color: #fff;
  border: 1px solid #3b82f6;
}
.soorma-btn-primary:hover {
  background: #2563eb;
  transform: translateY(-2px);
}
.soorma-btn-secondary {
  background: transparent;
  color: #fff;
  border: 1px solid #475569;
}
.soorma-btn-secondary:hover {
  border-color: #f97316;
  color: #f97316;
}

/* TIERS COMMON */
.soorma-tier-title {
  font-size: 32px;
  font-weight: 800;
  color: #fff;
  margin-bottom: 60px;
  text-align: center;
  letter-spacing: 4px;
}
.soorma-grid {
  display: flex;
  gap: 24px;
  justify-content: center;
  flex-wrap: wrap;
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
}
.soorma-card {
  background: #111;
  border: 1px solid #222;
  border-radius: 24px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  transition: all 0.3s ease;
  width: 100%;
}
.soorma-card:hover {
  border-color: #f97316;
  transform: translateY(-5px);
  background: #1a1a1a;
}
.soorma-card-img-placeholder {
  width: 100%;
  aspect-ratio: 1;
  background: #262626;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #525252;
  font-size: 12px;
  font-weight: 600;
}
.soorma-card-name {
  font-size: 18px;
  font-weight: 700;
  color: #f8fafc;
}
.soorma-card-role {
  font-size: 12px;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* SPECIFIC GRIDS */
.iconic-card { max-width: 400px; }
.aplus-card { max-width: 320px; }
.squad-card { max-width: 250px; }

@media (max-width: 991px) {
  .soorma-marquee-content {
    flex-direction: column;
    text-align: center;
    gap: 40px;
  }
  .soorma-marquee-right { align-items: center; }
  .soorma-marquee-stats { justify-content: center; }
  .soorma-marquee-meta strong { justify-content: center; }
}
</style>"""

# Using regex to replace the old CSS block
# The old CSS starts with "/* Soorma Roster Sections */" and ends right before "</style>" which ends the custom-cards-css block
new_html = re.sub(r'/\* Soorma Roster Sections \*/.*?</style>', sticky_roster_css, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Replaced CSS")
