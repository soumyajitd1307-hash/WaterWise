import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Fonts
html = html.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">\n<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
)

# CSS font replacements
html = re.sub(r"font-family:\s*'DM Sans',\s*sans-serif;", "font-family: 'Inter', sans-serif;", html)
html = re.sub(r"font-family:\s*'Playfair Display',\s*serif;", "font-family: 'Outfit', sans-serif;", html)
html = html.replace("family:'DM Sans'", "family:'Inter'")
html = html.replace('font-family="DM Sans"', 'font-family="Inter"')
html = html.replace("font-family:'DM Sans',sans-serif;", "font-family:'Inter',sans-serif;")
html = html.replace("font-family:'Playfair Display',serif;", "font-family:'Outfit',sans-serif;")

# 2. Change textContent to innerHTML for elements that will receive FontAwesome icons in JS
textContentToInnerHTML = [
    's.textContent=label;',
    "document.getElementById('resultsSubtitle').textContent=",
    'fire.textContent=flames;',
    'msg.textContent=',
    'b.textContent=',
    "document.getElementById('gaugeNum').textContent=",
    "document.getElementById('healthScoreLabel').textContent=",
    'btn.textContent='
]
for target in textContentToInnerHTML:
    html = html.replace(target, target.replace('textContent', 'innerHTML'))

# Remove emojis from Chart.js labels (Canvas text doesn't support HTML tags easily)
html = html.replace("'Shower 🚿'", "'Shower'")
html = html.replace("'Toilet 🚽'", "'Toilet'")
html = html.replace("'Handwash 🧼'", "'Handwash'")
html = html.replace("'Kitchen 🍽️'", "'Kitchen'")
html = html.replace("'Laundry 👕'", "'Laundry'")
html = html.replace("'Outdoor 🌿'", "'Outdoor'")

# 3. Emojis map to FontAwesome
emoji_map = {
    '💧': '<i class="fa-solid fa-droplet"></i>',
    '📊': '<i class="fa-solid fa-chart-simple"></i>',
    '🚿': '<i class="fa-solid fa-shower"></i>',
    '🚽': '<i class="fa-solid fa-toilet"></i>',
    '🧼': '<i class="fa-solid fa-hands-bubbles"></i>',
    '🍽️': '<i class="fa-solid fa-utensils"></i>',
    '👕': '<i class="fa-solid fa-shirt"></i>',
    '🌿': '<i class="fa-solid fa-leaf"></i>',
    '🚰': '<i class="fa-solid fa-faucet"></i>',
    '👨‍👩‍👧‍👦': '<i class="fa-solid fa-users"></i>',
    '🏆': '<i class="fa-solid fa-trophy"></i>',
    '🔥': '<i class="fa-solid fa-fire"></i>',
    '📅': '<i class="fa-solid fa-calendar-day"></i>',
    '📆': '<i class="fa-solid fa-calendar-week"></i>',
    '🗓️': '<i class="fa-solid fa-calendar-days"></i>',
    '🌟': '<i class="fa-solid fa-star"></i>',
    '✅': '<i class="fa-solid fa-check"></i>',
    '⚠️': '<i class="fa-solid fa-triangle-exclamation"></i>',
    '🚨': '<i class="fa-solid fa-bell"></i>',
    '🪥': '<i class="fa-solid fa-tooth"></i>',
    '🧽': '<i class="fa-solid fa-sponge"></i>',
    '🪣': '<i class="fa-solid fa-bucket"></i>',
    '🔧': '<i class="fa-solid fa-wrench"></i>',
    '🚗': '<i class="fa-solid fa-car"></i>',
    '💪': '<i class="fa-solid fa-dumbbell"></i>',
    '📋': '<i class="fa-solid fa-clipboard"></i>',
    '♻️': '<i class="fa-solid fa-recycle"></i>',
    '📉': '<i class="fa-solid fa-arrow-trend-down"></i>',
    '🔒': '<i class="fa-solid fa-lock"></i>',
    '💡': '<i class="fa-solid fa-lightbulb"></i>',
    '💚': '<i class="fa-solid fa-heart"></i>',
    '🥗': '<i class="fa-solid fa-bowl-food"></i>',
    '🏠': '<i class="fa-solid fa-house"></i>',
    '⚖️': '<i class="fa-solid fa-scale-balanced"></i>',
    '🇮🇳': '<i class="fa-solid fa-flag"></i>',
    '🌍': '<i class="fa-solid fa-globe"></i>',
    '🏥': '<i class="fa-solid fa-notes-medical"></i>',
    '🖼️': '<i class="fa-solid fa-image"></i>',
    '⏱️': '<i class="fa-solid fa-stopwatch"></i>',
    '🥦': '<i class="fa-solid fa-carrot"></i>',
    '🧊': '<i class="fa-solid fa-snowflake"></i>',
    '🌡️': '<i class="fa-solid fa-temperature-half"></i>',
    '⚡': '<i class="fa-solid fa-bolt"></i>',
    '🌱': '<i class="fa-solid fa-seedling"></i>',
    '🎉': '<i class="fa-solid fa-wand-magic-sparkles"></i>',
    '🎯': '<i class="fa-solid fa-bullseye"></i>',
    '🔴': '<i class="fa-solid fa-circle-xmark"></i>',
    '🟡': '<i class="fa-solid fa-circle-exclamation"></i>',
    '🟠': '<i class="fa-solid fa-circle-exclamation"></i>',
    '🟢': '<i class="fa-solid fa-circle-check"></i>',
    '🔵': '<i class="fa-solid fa-circle-info"></i>',
    '🌊': '<i class="fa-solid fa-water"></i>',
    '🏄': '<i class="fa-solid fa-person-surfing"></i>',
    '⭐': '<i class="fa-solid fa-star"></i>',
    '✨': '<i class="fa-solid fa-sparkles"></i>'
}

for emoji, tag in emoji_map.items():
    html = html.replace(emoji, tag)

# 4. Add custom CSS overrides for icons so they scale perfectly
css_addition = """
  i.fa-solid { font-size: inherit; color: inherit; line-height: 1; }
  .input-icon i { font-size: 1.25rem; color: var(--aqua); }
  .tip-emoji i { font-size: 1.6rem; color: var(--aqua); }
  .ch-icon i { font-size: 1.6rem; color: var(--aqua); }
  .proj-icon i { font-size: 1.8rem; color: var(--aqua); }
  .hero-tag i { margin-right: 6px; }
  .streak-fire-wrap { gap: 6px !important; color: #fb923c !important; }
</style>
"""
html = html.replace('</style>', css_addition)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done updating fonts and emojis to icons!")
