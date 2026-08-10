with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

override_style = """
<style>
.mf1-connector-innie.mf1-connector-0 {
    background-image: url('Branding_stuff/dbx-cover-soormas.svg') !important;
}
</style>
"""

if "dbx-cover-soormas.svg" not in html:
    html = html.replace('</head>', override_style + '</head>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML updated with innie override style.")
else:
    print("HTML already contains the innie override style.")
