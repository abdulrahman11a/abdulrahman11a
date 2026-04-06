#!/usr/bin/env python3
"""Generate dynamic header SVG with time-based greeting."""

from datetime import datetime, timezone, timedelta
import os

# Egypt timezone = UTC+2 (EET) or UTC+3 (EEST in summer)
# Using UTC+2 as base
egypt_tz = timezone(timedelta(hours=2))
now = datetime.now(egypt_tz)
hour = now.hour

# Dynamic greeting
if 5 <= hour < 12:
    greeting = "Good Morning"
elif 12 <= hour < 17:
    greeting = "Good Afternoon"

elif 17 <= hour < 21:
    greeting = "Good Evening"

else:
    greeting = "Good Night"

name = "Abdulrahman Fikry"
title = ".NET Developer | DevOps Engineer"

svg = f'''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0a0f0d"/>
      <stop offset="50%" style="stop-color:#0d2818"/>
      <stop offset="100%" style="stop-color:#0a0f0d"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bg)" rx="12"/>

  <!-- Animated particles -->
  <circle cx="60"  cy="40"  r="2"   fill="#00ff88" opacity="0.5"><animate attributeName="cy" values="40;160;40"   dur="4s"   repeatCount="indefinite"/><animate attributeName="opacity" values="0.5;0.1;0.5" dur="4s" repeatCount="indefinite"/></circle>
  <circle cx="150" cy="100" r="1.5" fill="#00ff88" opacity="0.3"><animate attributeName="cy" values="100;30;100"  dur="3s"   repeatCount="indefinite"/><animate attributeName="opacity" values="0.3;0.7;0.3" dur="3s" repeatCount="indefinite"/></circle>
  <circle cx="700" cy="60"  r="2"   fill="#00ff88" opacity="0.4"><animate attributeName="cy" values="60;160;60"   dur="5s"   repeatCount="indefinite"/><animate attributeName="opacity" values="0.4;0.1;0.4" dur="5s" repeatCount="indefinite"/></circle>
  <circle cx="760" cy="120" r="1.5" fill="#00cc66" opacity="0.3"><animate attributeName="cy" values="120;40;120"  dur="3.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.3;0.6;0.3" dur="3.5s" repeatCount="indefinite"/></circle>
  <circle cx="320" cy="25"  r="1"   fill="#00ff88" opacity="0.2"><animate attributeName="cy" values="25;175;25"   dur="6s"   repeatCount="indefinite"/><animate attributeName="opacity" values="0.2;0.5;0.2" dur="6s" repeatCount="indefinite"/></circle>
  <circle cx="480" cy="170" r="1.5" fill="#00ff88" opacity="0.25"><animate attributeName="cy" values="170;20;170"  dur="4.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.25;0.5;0.25" dur="4.5s" repeatCount="indefinite"/></circle>
  <circle cx="580" cy="50"  r="1"   fill="#00cc66" opacity="0.3"><animate attributeName="cy" values="50;150;50"   dur="3.8s" repeatCount="indefinite"/></circle>
  <circle cx="200" cy="160" r="2"   fill="#00ff88" opacity="0.2"><animate attributeName="cy" values="160;30;160"  dur="5.5s" repeatCount="indefinite"/></circle>

  <!-- Green accent line top -->
  <line x1="60" y1="18" x2="740" y2="18" stroke="#00ff88" stroke-width="0.5" opacity="0.3"/>
  <!-- Green accent line bottom -->
  <line x1="60" y1="182" x2="740" y2="182" stroke="#00ff88" stroke-width="0.5" opacity="0.3"/>

  <!-- Corner brackets -->
  <text x="20" y="36" font-family="monospace" font-size="20" fill="#00ff88" opacity="0.6">[</text>
  <text x="768" y="36" font-family="monospace" font-size="20" fill="#00ff88" opacity="0.6">]</text>

  <!-- Greeting line -->
  <text x="400" y="58" text-anchor="middle" font-family="'Segoe UI', monospace" font-size="15" fill="#6a9a7a" letter-spacing="2" filter="url(#glow)">{greeting}, visitor!</text>

  <!-- Name -->
  <text x="400" y="108" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="38" font-weight="bold" fill="#00ff88" filter="url(#glow)">
    {name}
  </text>

  <!-- Title -->
  <text x="400" y="142" text-anchor="middle" font-family="'Courier New', monospace" font-size="15" fill="#8b949e" letter-spacing="1">
    {title}
  </text>

  <!-- Location + greeting_ar -->
  <text x="400" y="170" text-anchor="middle" font-family="'Segoe UI', Arial" font-size="12" fill="#444f48">
    🇪🇬 Egypt  ·  {greeting_ar}
  </text>
</svg>'''

os.makedirs("dynamic-svg", exist_ok=True)
with open("dynamic-svg/header.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print(f"✅ Generated header.svg — greeting: {greeting} ({hour}:xx Egypt time)")
