import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .reveal CSS
old_reveal = """.reveal { opacity:0; transform:translateY(30px); transition:opacity .6s ease-out,transform .6s ease-out; }
  .reveal.visible { opacity:1; transform:translateY(0); }"""

new_reveal = """.reveal { opacity:0; transform:translateY(40px) scale(0.96); transition:opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1); }
  .reveal.visible { opacity:1; transform:translateY(0) scale(1); }
  .ch-card-enter { animation: slideFadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards; opacity: 0; transform: translateY(20px); }
  @keyframes slideFadeIn { to { opacity: 1; transform: translateY(0); } }"""

html = html.replace(old_reveal, new_reveal)

# Upgrade health bar transition for a bouncy spring effect
html = html.replace('transition:width 1s cubic-bezier(0.4,0,0.2,1)', 'transition:width 1.2s cubic-bezier(0.34, 1.56, 0.64, 1)')
# Upgrade calc-grid cards
html = html.replace('transition: border-color .2s,transform .15s,box-shadow .2s;', 'transition: border-color .3s, transform .2s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow .3s;')

# 2. Update renderChallenges to add staggered animations
old_ch_card_html = """return `<div class="ch-card${done?' ch-done':''}${locked?' ch-locked':''}">"""
new_ch_card_html = """return `<div class="ch-card ch-card-enter${done?' ch-done':''}${locked?' ch-locked':''}" style="animation-delay: ${idx * 0.08}s">"""

# renderChallenges uses map(ch=> { ... return `<div class="ch-card ...`
html = html.replace("grid.innerHTML=filtered.map(ch=>{", "grid.innerHTML=filtered.map((ch, idx)=>{")
html = html.replace(old_ch_card_html, new_ch_card_html)

# 3. Update IntersectionObserver to stagger elements appearing simultaneously
old_observer = """const revealObserver=new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');revealObserver.unobserve(e.target);}});
},{threshold:0.12,rootMargin:'0px 0px -40px 0px'});"""

new_observer = """let revealQueue = [];
let revealTimeout = null;
const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if(e.isIntersecting) {
      revealQueue.push(e.target);
      revealObserver.unobserve(e.target);
    }
  });
  if(revealQueue.length > 0 && !revealTimeout) {
    revealTimeout = setTimeout(() => {
      revealQueue.forEach((el, i) => {
        if(!el.style.transitionDelay && el.classList.contains('tip-card') || el.classList.contains('input-card')) {
          el.style.transitionDelay = (i * 0.1) + 's';
        }
        el.classList.add('visible');
      });
      revealQueue = [];
      revealTimeout = null;
    }, 50);
  }
}, {threshold:0.12, rootMargin:'0px 0px -40px 0px'});"""

html = html.replace(old_observer, new_observer)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Dynamic transitions improved successfully!")
