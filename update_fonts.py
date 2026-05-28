import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Google Fonts link
# Old: <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
html = re.sub(
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter.*?rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Syne:wght@400;500;600;700;800&display=swap" rel="stylesheet">',
    html
)

# Replace CSS font families
# Old: font-family: 'Inter', sans-serif; -> font-family: 'Plus Jakarta Sans', sans-serif;
# Old: font-family: 'Outfit', sans-serif; -> font-family: 'Syne', sans-serif;
# Old: font-family="Inter" -> font-family="Plus Jakarta Sans"

html = html.replace("font-family: 'Inter', sans-serif;", "font-family: 'Plus Jakarta Sans', sans-serif;")
html = html.replace("font-family: 'Outfit', sans-serif;", "font-family: 'Syne', sans-serif;")
html = html.replace("family:'Inter'", "family:'Plus Jakarta Sans'")
html = html.replace('font-family="Inter"', 'font-family="Plus Jakarta Sans"')
html = html.replace("font-family:'Inter',sans-serif;", "font-family:'Plus Jakarta Sans',sans-serif;")
html = html.replace("font-family:'Outfit',sans-serif;", "font-family:'Syne',sans-serif;")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fonts updated to Syne and Plus Jakarta Sans!")
