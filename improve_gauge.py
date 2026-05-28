import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update SVG styles to add filters and better needle
old_svg = """<svg class="gauge-svg" viewBox="0 0 220 220">
          <defs>
            <linearGradient id="gaugeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#34d399"/>
              <stop offset="50%" stop-color="#22d3ee"/>
              <stop offset="100%" stop-color="#f87171"/>
            </linearGradient>
          </defs>
          <path d="M 30 165 A 80 80 0 0 1 190 165" fill="none" stroke="rgba(34,211,238,0.06)" stroke-width="12" stroke-linecap="round"/>
          <path id="gaugeFill" d="M 30 165 A 80 80 0 0 1 190 165" fill="none" stroke="url(#gaugeGrad)" stroke-width="12" stroke-linecap="round" stroke-dasharray="251.2" stroke-dashoffset="251.2" style="transition:stroke-dashoffset 1.4s cubic-bezier(.4,0,.2,1)"/>
          <line id="gaugeNeedle" x1="110" y1="165" x2="110" y2="110" stroke="rgba(240,249,255,0.85)" stroke-width="2" stroke-linecap="round" style="transform-origin:110px 165px;transform:rotate(-90deg);transition:transform 1.4s cubic-bezier(.4,0,.2,1)"/>
          <circle cx="110" cy="165" r="4" fill="var(--aqua)"/>"""

new_svg = """<svg class="gauge-svg" viewBox="0 0 220 220">
          <defs>
            <linearGradient id="gaugeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#34d399"/>
              <stop offset="50%" stop-color="#22d3ee"/>
              <stop offset="100%" stop-color="#f87171"/>
            </linearGradient>
            <filter id="gaugeGlow" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="6" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
            <filter id="shadow">
              <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.3"/>
            </filter>
          </defs>
          <path d="M 30 165 A 80 80 0 0 1 190 165" fill="none" stroke="rgba(34,211,238,0.08)" stroke-width="16" stroke-linecap="round"/>
          <!-- Active fill with glow -->
          <path id="gaugeFill" d="M 30 165 A 80 80 0 0 1 190 165" fill="none" stroke="url(#gaugeGrad)" stroke-width="16" stroke-linecap="round" stroke-dasharray="251.2" stroke-dashoffset="251.2" style="transition:stroke-dashoffset 1.8s cubic-bezier(0.34, 1.56, 0.64, 1); filter: url(#gaugeGlow);"/>
          <!-- Stylish needle -->
          <g id="gaugeNeedle" style="transform-origin:110px 165px; transform:rotate(-90deg); transition:transform 1.8s cubic-bezier(0.34, 1.56, 0.64, 1); filter: url(#shadow);">
            <polygon points="107,165 113,165 110,95" fill="rgba(240,249,255,0.9)"/>
            <circle cx="110" cy="165" r="8" fill="#0b1d3a" stroke="url(#gaugeGrad)" stroke-width="3"/>
          </g>"""

html = html.replace(old_svg, new_svg)

# 2. Add count-up animation for gaugeNum in JS
old_animate_gauge = """function animateGauge(liters){
  const pct=Math.min(liters/300,1);
  document.getElementById('gaugeFill').style.strokeDashoffset=251.2*(1-pct);
  document.getElementById('gaugeNeedle').style.transform=`rotate(${-90+pct*180}deg)`;
  document.getElementById('gaugeNum').innerHTML=Math.round(liters)+' L';"""

new_animate_gauge = """function animateGauge(liters){
  const pct=Math.min(liters/300,1);
  document.getElementById('gaugeFill').style.strokeDashoffset=251.2*(1-pct);
  document.getElementById('gaugeNeedle').style.transform=`rotate(${-90+pct*180}deg)`;
  
  // Count-up animation for gaugeNum
  const numEl = document.getElementById('gaugeNum');
  let start = parseInt(numEl.textContent) || 0;
  let target = Math.round(liters);
  let duration = 1400; // ms
  let startTime = null;
  
  function step(timestamp) {
    if(!startTime) startTime = timestamp;
    let progress = (timestamp - startTime) / duration;
    // Cubic ease-out
    let easeOut = 1 - Math.pow(1 - progress, 3);
    if(progress < 1) {
      numEl.innerHTML = Math.round(start + (target - start) * easeOut) + ' L';
      requestAnimationFrame(step);
    } else {
      numEl.innerHTML = target + ' L';
    }
  }
  requestAnimationFrame(step);"""

html = html.replace(old_animate_gauge, new_animate_gauge)

# 3. Enhance CSS for gaugeNum and gaugeStatus to be livelier
old_gauge_css = ".gauge-num { font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 900; color: var(--white); letter-spacing: -0.02em; }"
new_gauge_css = ".gauge-num { font-family: 'Syne', sans-serif; font-size: 2.6rem; font-weight: 900; color: var(--aqua); letter-spacing: -0.02em; text-shadow: 0 0 20px rgba(34,211,238,0.4); transition: color 0.5s; }"
html = html.replace(old_gauge_css, new_gauge_css)

old_gauge_status_css = ".gauge-status { display: inline-flex; align-items: center; gap: 6px; padding: 6px 20px; border-radius: 999px; border: 1px solid transparent; font-size: 0.78rem; font-weight: 500; letter-spacing: 0.02em; margin-top: 4px; }"
new_gauge_status_css = ".gauge-status { display: inline-flex; align-items: center; gap: 8px; padding: 8px 24px; border-radius: 999px; border: 1px solid transparent; font-size: 0.85rem; font-weight: 600; letter-spacing: 0.02em; margin-top: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.3); transition: all 0.5s ease; }"
html = html.replace(old_gauge_status_css, new_gauge_status_css)

# Update color of gauge-num depending on the status
old_status_color = "s.innerHTML=label;s.style.background=bg;s.style.color=col;s.style.border=`1px solid ${col}40`;"
new_status_color = """s.innerHTML=label;s.style.background=bg;s.style.color=col;s.style.border=`1px solid ${col}40`;
  document.getElementById('gaugeNum').style.color=col;
  document.getElementById('gaugeNum').style.textShadow=`0 0 20px ${col}80`;"""
html = html.replace(old_status_color, new_status_color)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Gauge improved successfully!")
