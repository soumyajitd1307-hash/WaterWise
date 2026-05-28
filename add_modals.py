import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update categoryTips with detailed descriptions
details = {
    "Shorter Showers": "Reducing your shower time from 10 minutes to 5 minutes cuts your water usage by 50%. Setting a 5-minute timer or playing a short 2-song playlist can make this habit easy to adopt. Over a year, this small change saves enough water to fill a large swimming pool!",
    "Low-Flow Showerhead": "Standard showerheads use 10-15 L/min. Low-flow aerated models use just 5-7 L/min by mixing air with the water to maintain strong pressure. This one-time installation pays for itself in just a few months through reduced water and water-heating bills.",
    "Bucket the Cold Water": "It often takes a minute or two for hot water to reach the showerhead. By placing a bucket in the shower while the water warms up, you can collect up to 10 litres of clean water per shower. Use this to flush the toilet, water plants, or mop floors.",
    
    "Dual-Flush Mechanism": "A dual-flush toilet has two buttons: one for liquid waste (using ~3 litres) and one for solid waste (using ~6 litres). Since the majority of flushes are for liquid waste, this simple mechanism reduces household toilet water consumption by nearly 50% compared to traditional single-flush models.",
    "Check for Leaks": "Toilet leaks are often silent and can waste up to 700 litres a day! Put a few drops of food colouring in the toilet tank and wait 15 minutes without flushing. If color seeps into the bowl, the flapper valve needs replacing—an easy and cheap DIY fix.",
    "Bottle in the Tank": "If you have an older, high-volume toilet (9-12 L per flush), you can reduce its usage by placing a sealed plastic bottle filled with water (and a few pebbles for weight) into the tank away from moving parts. This displaces water, saving ~1 litre per flush.",
    
    "Turn Off While Scrubbing": "A running tap dispenses about 6 litres of water every minute. By wetting your hands, turning off the tap to lather and scrub with soap for the recommended 20 seconds, and only turning it back on to rinse, you save at least 2 litres of water every single time you wash your hands.",
    "Soap First, Then Water": "Many people turn the tap on before picking up the soap. Try changing the order: grab the soap, start lathering, and only turn the tap on when you're ready to rinse. It seems small, but doing this multiple times a day adds up to massive savings.",
    "Aerate Your Tap": "Installing a low-flow aerator on your bathroom faucet is incredibly cheap and takes two minutes. It mixes air into the water stream, reducing the flow rate from 10 L/min down to as little as 2 L/min, without sacrificing the feeling of high pressure.",
    
    "Soak Dishes": "Instead of leaving the tap running while you scrub dishes (which wastes up to 20 litres per session), fill one basin or a large pot with warm, soapy water for scrubbing, and use another for rinsing. This method gets dishes equally clean while slashing water use.",
    "Wash Veggies in a Bowl": "Rinsing vegetables under a running tap wastes several litres of water. Fill a bowl with clean water and scrub your produce in there. As a bonus, the leftover water is nutrient-rich and perfect for watering your indoor plants!",
    "Keep Drinking Water in the Fridge": "Waiting for the tap to run cold wastes up to 2 litres of perfectly good drinking water every time. By keeping a pitcher of water in the refrigerator, you have instant access to ice-cold water with zero waste.",
    
    "Full Loads Only": "Washing machines use roughly the same amount of water (about 50-70 litres) whether you put in one shirt or a massive pile of towels. To maximize efficiency, always wait until you have a full load before running a cycle.",
    "Use Cold Water": "About 90% of the energy used by a washing machine goes toward heating the water. Modern detergents are designed to work brilliantly in cold water (20°C). Switching to cold washes saves massive amounts of energy and helps your clothes last longer.",
    "High-Efficiency Machine": "If your washing machine is old, consider upgrading to a Front-Loading High-Efficiency (HE) model. Top-loaders require the drum to fill entirely with water, while HE front-loaders tumble clothes through a much smaller pool of water, using 40-50% less water per load.",
    
    "Water at Dusk or Dawn": "Watering your garden in the middle of a hot day means up to 30% of the water evaporates before it even reaches the roots. Watering in the early morning or late evening ensures the water penetrates deeply into the soil, keeping plants healthier.",
    "Rainwater Harvesting": "A single millimeter of rain on a 100 sqm roof yields 100 litres of water! Setting up a simple rain barrel beneath your downspout allows you to capture this free, unchlorinated water, which is naturally better for your plants than tap water.",
    "Drip Irrigation": "Sprinklers often overwater areas and lose water to wind and evaporation. A drip irrigation system slowly delivers water directly to the base of each plant. This encourages deep root growth, prevents fungal diseases, and uses 50% less water than sprinklers."
}

for title, desc in details.items():
    # We will inject `detailedDesc: '...'` into the object right after the title.
    # The title looks like: title:'Shorter Showers',
    html = html.replace(
        f"title:'{title}'",
        f"title:'{title}',detailedDesc:'{desc.replace(chr(39), chr(92)+chr(39))}'"
    )

# 2. Add Animations Data
animations_data = """
const animationsData = {
  shower: `<svg viewBox="0 0 200 200" width="100%" height="100%">
    <style>
      .drop { animation: dropAnim 1.5s infinite ease-in; opacity:0; }
      .d1 { animation-delay: 0s; } .d2 { animation-delay: 0.5s; } .d3 { animation-delay: 1s; }
      @keyframes dropAnim { 0% { transform: translateY(0); opacity: 0; } 20% { opacity: 1; } 80% { opacity: 1; } 100% { transform: translateY(60px); opacity: 0; } }
      .head { fill: var(--glass); stroke: var(--aqua); stroke-width: 4; }
    </style>
    <!-- Showerhead -->
    <path class="head" d="M120 40 L80 40 L60 70 L140 70 Z" rx="5" stroke-linejoin="round"/>
    <path class="head" d="M100 0 L100 40" />
    <!-- Drops -->
    <circle cx="80" cy="80" r="4" fill="var(--aqua)" class="drop d1"/>
    <circle cx="100" cy="80" r="4" fill="var(--aqua)" class="drop d2"/>
    <circle cx="120" cy="80" r="4" fill="var(--aqua)" class="drop d3"/>
  </svg>`,
  
  toilet: `<svg viewBox="0 0 200 200" width="100%" height="100%">
    <style>
      .flush { animation: flushAnim 3s infinite ease-in-out; transform-origin: center; }
      @keyframes flushAnim { 0%, 100% { transform: scale(0.8); opacity: 0.2; } 50% { transform: scale(1.1); opacity: 0.8; } }
      .tank { fill: var(--glass); stroke: var(--aqua); stroke-width: 4; }
    </style>
    <!-- Toilet Tank -->
    <rect x="70" y="40" width="60" height="50" rx="4" class="tank"/>
    <rect x="90" y="30" width="20" height="10" rx="2" class="tank"/>
    <!-- Toilet Bowl -->
    <path class="tank" d="M75 90 L125 90 C 135 130, 115 150, 100 150 C 85 150, 65 130, 75 90 Z"/>
    <!-- Water swirl -->
    <ellipse cx="100" cy="115" rx="15" ry="5" fill="none" stroke="var(--aqua)" stroke-width="3" class="flush"/>
  </svg>`,
  
  handwash: `<svg viewBox="0 0 200 200" width="100%" height="100%">
    <style>
      .flow { animation: flowAnim 2s infinite ease-in-out; stroke-dasharray: 10 10; }
      @keyframes flowAnim { from { stroke-dashoffset: 20; } to { stroke-dashoffset: 0; } }
      .faucet { fill: var(--glass); stroke: var(--aqua); stroke-width: 4; }
    </style>
    <!-- Faucet -->
    <path class="faucet" d="M140 40 L90 40 C 70 40, 70 70, 70 70 L70 90 L50 90" stroke-linecap="round" fill="none"/>
    <!-- Handles -->
    <circle cx="140" cy="40" r="8" class="faucet"/>
    <path class="faucet" d="M50 85 L50 95" />
    <!-- Water stream -->
    <line x1="60" y1="95" x2="60" y2="150" stroke="var(--aqua)" stroke-width="6" class="flow" stroke-linecap="round"/>
  </svg>`,
  
  kitchen: `<svg viewBox="0 0 200 200" width="100%" height="100%">
    <style>
      .bubbleAnim { animation: bAnim 3s infinite ease-in; opacity:0; }
      .b1 { animation-delay: 0s; } .b2 { animation-delay: 1s; } .b3 { animation-delay: 2s; }
      @keyframes bAnim { 0% { transform: translateY(0) scale(0.5); opacity: 0; } 50% { opacity: 0.6; } 100% { transform: translateY(-40px) scale(1.2); opacity: 0; } }
      .sink { fill: var(--glass); stroke: var(--aqua); stroke-width: 4; }
    </style>
    <!-- Sink Basin -->
    <path class="sink" d="M40 80 L160 80 L140 140 L60 140 Z" stroke-linejoin="round"/>
    <!-- Water level -->
    <line x1="50" y1="110" x2="150" y2="110" stroke="var(--aqua)" stroke-width="2" stroke-dasharray="8 4"/>
    <!-- Bubbles -->
    <circle cx="80" cy="130" r="6" fill="none" stroke="var(--aqua)" stroke-width="2" class="bubbleAnim b1"/>
    <circle cx="120" cy="120" r="4" fill="none" stroke="var(--aqua)" stroke-width="2" class="bubbleAnim b2"/>
    <circle cx="100" cy="135" r="8" fill="none" stroke="var(--aqua)" stroke-width="2" class="bubbleAnim b3"/>
  </svg>`,
  
  laundry: `<svg viewBox="0 0 200 200" width="100%" height="100%">
    <style>
      .spin { animation: spinAnim 4s infinite linear; transform-origin: 100px 105px; }
      @keyframes spinAnim { 100% { transform: rotate(360deg); } }
      .machine { fill: var(--glass); stroke: var(--aqua); stroke-width: 4; }
    </style>
    <!-- Washing Machine Body -->
    <rect x="50" y="30" width="100" height="130" rx="8" class="machine"/>
    <!-- Dial -->
    <circle cx="130" cy="45" r="4" fill="var(--aqua)"/>
    <line x1="50" y1="60" x2="150" y2="60" stroke="var(--aqua)" stroke-width="4"/>
    <!-- Drum -->
    <circle cx="100" cy="110" r="35" class="machine"/>
    <circle cx="100" cy="110" r="25" fill="none" stroke="var(--aqua)" stroke-width="2" stroke-dasharray="10 5" class="spin"/>
  </svg>`,
  
  garden: `<svg viewBox="0 0 200 200" width="100%" height="100%">
    <style>
      .grow { animation: growAnim 3s infinite ease-in-out; transform-origin: bottom center; }
      @keyframes growAnim { 0%, 100% { transform: scaleY(0.9) skewX(2deg); } 50% { transform: scaleY(1.1) skewX(-2deg); } }
      .pot { fill: var(--glass); stroke: var(--aqua); stroke-width: 4; }
      .plant { fill: none; stroke: #34d399; stroke-width: 4; stroke-linecap: round; }
    </style>
    <!-- Pot -->
    <path class="pot" d="M70 150 L130 150 L140 100 L60 100 Z" stroke-linejoin="round"/>
    <!-- Plant -->
    <g class="grow">
      <path class="plant" d="M100 100 Q 90 70, 100 40" />
      <path class="plant" d="M100 80 Q 70 70, 80 50" />
      <path class="plant" d="M100 60 Q 130 50, 120 30" />
    </g>
  </svg>`
};
"""

# Inject animationsData before `const categoryTips`
html = html.replace('const categoryTips={', animations_data + '\nconst categoryTips={')


# 3. Update showAnalysisTips to make tip cards clickable and pass data
# Old line: return tips.slice(0,1).map(t=>`
# We want: return tips.slice(0,1).map((t, idx)=>`
# And add onclick to the tip-card div
old_card_code = """return tips.slice(0,1).map(t=>`
      <div class="tip-card" style="background:var(--glass);border:1px solid var(--border);border-radius:14px;padding:16px;backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);box-shadow:var(--glass-depth),var(--glass-edge)">"""

new_card_code = """return tips.slice(0,1).map((t, idx)=>`
      <div class="tip-card" onclick="openTipModal('${cat}', ${idx})" style="background:var(--glass);border:1px solid var(--border);border-radius:14px;padding:16px;backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);box-shadow:var(--glass-depth),var(--glass-edge);cursor:pointer;transition:transform 0.2s, border-color 0.2s;" onmouseover="this.style.transform='translateY(-2px)';this.style.borderColor='rgba(34,211,238,0.4)'" onmouseout="this.style.transform='translateY(0)';this.style.borderColor='var(--border)'">"""

html = html.replace(old_card_code, new_card_code)


# 4. Add the Modal HTML and JS Logic
modal_html_js = """
<!-- TIP MODAL -->
<div id="tipModalOverlay" style="display:none; position:fixed; inset:0; background:rgba(6,14,31,0.85); z-index:9999; backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); align-items:center; justify-content:center; padding:24px; opacity:0; transition:opacity 0.3s;">
  <div id="tipModalCard" style="background:rgba(14,52,96,0.6); border:1px solid var(--border); border-radius:24px; max-width:500px; width:100%; box-shadow:0 24px 60px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.06); transform:translateY(20px); transition:transform 0.3s; overflow:hidden;">
    <div style="position:relative; height:180px; background:radial-gradient(circle at center, rgba(34,211,238,0.1), transparent); border-bottom:1px solid rgba(255,255,255,0.05); display:flex; align-items:center; justify-content:center; overflow:hidden;" id="tipModalAnimWrap">
      <!-- SVG goes here -->
    </div>
    <div style="padding:24px 32px 32px;">
      <h3 id="tipModalTitle" style="font-family:'Syne', sans-serif; font-size:1.6rem; color:var(--white); margin-bottom:12px; font-weight:700;"></h3>
      <p id="tipModalDesc" style="font-family:'Plus Jakarta Sans', sans-serif; font-size:0.95rem; line-height:1.7; color:rgba(240,249,255,0.7);"></p>
      <div style="margin-top:24px; text-align:right;">
        <button onclick="closeTipModal()" class="cta-btn-ghost" style="padding:10px 24px; font-size:0.9rem;">Got it</button>
      </div>
    </div>
    <button onclick="closeTipModal()" style="position:absolute; top:16px; right:16px; background:rgba(255,255,255,0.1); border:none; width:32px; height:32px; border-radius:50%; color:var(--white); cursor:pointer; font-size:1.1rem; display:flex; align-items:center; justify-content:center; transition:background 0.2s;"><i class="fa-solid fa-xmark"></i></button>
  </div>
</div>

<script>
function openTipModal(category, index) {
  const overlay = document.getElementById('tipModalOverlay');
  const card = document.getElementById('tipModalCard');
  const tip = categoryTips[category][index];
  
  document.getElementById('tipModalTitle').innerHTML = tip.icon + ' ' + tip.title;
  document.getElementById('tipModalDesc').textContent = tip.detailedDesc || tip.text;
  
  // Inject animation
  document.getElementById('tipModalAnimWrap').innerHTML = animationsData[category] || '';
  
  overlay.style.display = 'flex';
  // Trigger reflow
  void overlay.offsetWidth;
  overlay.style.opacity = '1';
  card.style.transform = 'translateY(0)';
}

function closeTipModal() {
  const overlay = document.getElementById('tipModalOverlay');
  const card = document.getElementById('tipModalCard');
  overlay.style.opacity = '0';
  card.style.transform = 'translateY(20px)';
  setTimeout(() => {
    overlay.style.display = 'none';
  }, 300);
}

// Close on outside click
document.getElementById('tipModalOverlay').addEventListener('click', function(e) {
  if(e.target === this) closeTipModal();
});
</script>
"""

# Inject before </body>
html = html.replace('</body>', modal_html_js + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Modals and animations integrated successfully!")
