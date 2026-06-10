#!/usr/bin/env python3
"""
Android Locked Screen – Global SEO Site Builder
Affiliate: https://www.linkconnector.com/ta.php?lc=007949070197004532&atid=androidlockscreen
Deploy: https://brightlane.github.io/androidlockedscreen/
"""

import os, json, textwrap
from pathlib import Path

BASE = Path(__file__).parent
AFFILIATE = "https://www.linkconnector.com/ta.php?lc=007949070197004532&atid=androidlockscreen"
SITE_URL  = "https://brightlane.github.io/androidlockedscreen"
YEAR      = "2026"

# ── Shared CTA Button ────────────────────────────────────────────────────────
def cta(text="Download Dr.Fone Free", extra_class=""):
    return f'<a href="{AFFILIATE}" class="btn {extra_class}" target="_blank" rel="noopener">{text}</a>'

# ── hreflang block ───────────────────────────────────────────────────────────
LANG_CODES = [
    ("en",""),("de","lang/de"),("fr","lang/fr"),("es","lang/es"),
    ("pt","lang/pt"),("it","lang/it"),("ja","lang/ja"),("zh","lang/zh"),
    ("ko","lang/ko"),("ru","lang/ru"),("ar","lang/ar"),("hi","lang/hi"),
    ("id","lang/id"),("nl","lang/nl"),("pl","lang/pl"),("tr","lang/tr"),
    ("sv","lang/sv"),("fil","lang/fil"),("vi","lang/vi"),("th","lang/th"),
]

def hreflang_tags():
    tags = ""
    for code, path in LANG_CODES:
        url = SITE_URL if path=="" else f"{SITE_URL}/{path}/"
        tags += f'  <link rel="alternate" hreflang="{code}" href="{url}">\n'
    tags += f'  <link rel="alternate" hreflang="x-default" href="{SITE_URL}/">\n'
    return tags

# ── Language strip ───────────────────────────────────────────────────────────
LANG_LABELS = [
    ("en","English",""),("de","Deutsch","lang/de"),("fr","Français","lang/fr"),
    ("es","Español","lang/es"),("pt","Português","lang/pt"),("it","Italiano","lang/it"),
    ("ja","日本語","lang/ja"),("zh","中文","lang/zh"),("ko","한국어","lang/ko"),
    ("ru","Русский","lang/ru"),("ar","العربية","lang/ar"),("hi","हिन्दी","lang/hi"),
    ("id","Indonesia","lang/id"),("nl","Nederlands","lang/nl"),("pl","Polski","lang/pl"),
    ("tr","Türkçe","lang/tr"),("sv","Svenska","lang/sv"),("fil","Filipino","lang/fil"),
    ("vi","Tiếng Việt","lang/vi"),("th","ภาษาไทย","lang/th"),
]
def lang_strip():
    items = ""
    for code, label, path in LANG_LABELS:
        href = f"{SITE_URL}/{path}/" if path else f"{SITE_URL}/"
        items += f'<a href="{href}" class="lpill">{label}</a>'
    return f'<div class="lang-strip"><div class="lscroll">{items}</div></div>'

# ── Global CSS ───────────────────────────────────────────────────────────────
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',Arial,sans-serif;background:#f7f9fc;color:#1a1a2e;line-height:1.7}
a{color:#0066cc;text-decoration:none}
a:hover{text-decoration:underline}
header{background:linear-gradient(135deg,#0f3460 0%,#16213e 100%);color:#fff;padding:18px 0;position:sticky;top:0;z-index:100;box-shadow:0 2px 12px rgba(0,0,0,.3)}
.hinner{max-width:1100px;margin:0 auto;padding:0 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px}
.logo{font-size:1.3rem;font-weight:700;color:#fff;letter-spacing:-0.5px}
.logo span{color:#e94560}
nav a{color:#ddd;margin-left:18px;font-size:.92rem}
nav a:hover{color:#fff;text-decoration:none}
.lang-strip{background:#16213e;border-bottom:1px solid #0f3460;padding:8px 0}
.lscroll{max-width:1100px;margin:0 auto;padding:0 20px;display:flex;gap:8px;overflow-x:auto;scrollbar-width:thin}
.lpill{background:#0f3460;color:#aac;padding:4px 12px;border-radius:20px;font-size:.8rem;white-space:nowrap;transition:.2s}
.lpill:hover{background:#e94560;color:#fff;text-decoration:none}
.hero{background:linear-gradient(135deg,#0f3460 0%,#16213e 60%,#1a1a2e 100%);color:#fff;padding:80px 20px 60px;text-align:center}
.hero h1{font-size:clamp(1.8rem,4vw,3rem);font-weight:800;margin-bottom:16px;line-height:1.2}
.hero p{font-size:1.15rem;max-width:680px;margin:0 auto 32px;color:#c0cfe0}
.btn{display:inline-block;background:#e94560;color:#fff!important;padding:14px 32px;border-radius:8px;font-weight:700;font-size:1rem;transition:.2s;text-decoration:none!important;margin:6px}
.btn:hover{background:#c73652;transform:translateY(-2px);box-shadow:0 6px 20px rgba(233,69,96,.4)}
.btn-sec{background:transparent;border:2px solid #fff;color:#fff!important}
.btn-sec:hover{background:#fff;color:#0f3460!important}
main{max-width:1100px;margin:0 auto;padding:40px 20px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px;margin:32px 0}
.card{background:#fff;border-radius:12px;padding:28px;box-shadow:0 2px 12px rgba(0,0,0,.07);transition:.2s}
.card:hover{transform:translateY(-4px);box-shadow:0 8px 28px rgba(0,0,0,.12)}
.card .icon{font-size:2.4rem;margin-bottom:14px}
.card h3{font-size:1.1rem;font-weight:700;margin-bottom:8px;color:#0f3460}
.card p{font-size:.93rem;color:#555}
.steps{counter-reset:step;margin:24px 0}
.step{display:flex;gap:20px;margin-bottom:28px;align-items:flex-start}
.step-num{background:#e94560;color:#fff;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:1.1rem;flex-shrink:0}
.step-body h3{font-weight:700;margin-bottom:6px;color:#0f3460}
.step-body p{color:#555;font-size:.95rem}
h2{font-size:1.7rem;font-weight:800;color:#0f3460;margin:48px 0 16px}
h2:first-child{margin-top:0}
.badge-row{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0}
.badge{background:#e8f0fe;color:#0f3460;padding:6px 16px;border-radius:20px;font-size:.88rem;font-weight:600}
.brands{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:12px;margin:20px 0}
.brand-card{background:#fff;border:1.5px solid #e0e7ff;border-radius:10px;padding:16px;text-align:center;font-weight:600;font-size:.92rem;color:#0f3460;transition:.2s}
.brand-card:hover{border-color:#e94560;color:#e94560;text-decoration:none}
table{width:100%;border-collapse:collapse;margin:24px 0;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.06)}
th{background:#0f3460;color:#fff;padding:14px 16px;text-align:left;font-size:.93rem}
td{padding:12px 16px;border-bottom:1px solid #eef;font-size:.93rem}
tr:last-child td{border-bottom:none}
tr:nth-child(even) td{background:#f7f9fc}
.faq{margin:24px 0}
.faq-item{background:#fff;border-radius:10px;margin-bottom:12px;box-shadow:0 1px 6px rgba(0,0,0,.06);overflow:hidden}
.faq-q{padding:18px 22px;font-weight:700;cursor:pointer;color:#0f3460;display:flex;justify-content:space-between;align-items:center}
.faq-q::after{content:"▼";font-size:.8rem;color:#e94560}
.faq-a{padding:0 22px 18px;color:#555;font-size:.94rem;display:block}
.trust-bar{background:#fff;border-radius:12px;padding:24px;display:flex;flex-wrap:wrap;gap:20px;justify-content:center;margin:32px 0;box-shadow:0 2px 12px rgba(0,0,0,.06)}
.trust-item{text-align:center;font-size:.88rem;color:#444}
.trust-item strong{display:block;font-size:1.4rem;color:#0f3460;font-weight:800}
.cta-box{background:linear-gradient(135deg,#0f3460,#16213e);color:#fff;border-radius:16px;padding:40px;text-align:center;margin:48px 0}
.cta-box h2{color:#fff;margin:0 0 12px}
.cta-box p{color:#c0cfe0;margin-bottom:24px}
footer{background:#16213e;color:#aac;text-align:center;padding:28px 20px;font-size:.88rem;margin-top:60px}
footer a{color:#7799cc}
@media(max-width:600px){.hero h1{font-size:1.6rem}.hinner{flex-direction:column;align-items:flex-start}nav{margin-top:6px}nav a:first-child{margin-left:0}}
"""

# ── Base HTML template ───────────────────────────────────────────────────────
def page(title, desc, keywords, body, lang="en", canonical=""):
    canon = canonical if canonical else SITE_URL+"/"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="website">
<link rel="canonical" href="{canon}">
{hreflang_tags()}<style>{CSS}</style>
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"WebPage",
  "name":"{title}",
  "description":"{desc}",
  "url":"{canon}"
}}
</script>
</head>
<body>
<header>
<div class="hinner">
<a class="logo" href="{SITE_URL}/"><span>🔓</span> AndroidLockedScreen</a>
<nav>
<a href="{SITE_URL}/">Home</a>
<a href="{SITE_URL}/samsung/">Samsung</a>
<a href="{SITE_URL}/frp/">FRP Bypass</a>
<a href="{SITE_URL}/forgot-password/">Forgot Password</a>
<a href="{SITE_URL}/global/">🌍 Global</a>
</nav>
</div>
</header>
{lang_strip()}
{body}
<footer>
<p>© {YEAR} AndroidLockedScreen.com &nbsp;|&nbsp; <a href="{AFFILIATE}" target="_blank">Download Dr.Fone</a> &nbsp;|&nbsp; <a href="{SITE_URL}/global/">Global Versions</a></p>
<p style="margin-top:8px;font-size:.8rem;color:#668">For informational purposes only. Use responsibly and only on devices you own or have permission to unlock.</p>
</footer>
</body></html>"""

# ── HOMEPAGE ─────────────────────────────────────────────────────────────────
def build_home():
    body = f"""
<div class="hero">
  <h1>Unlock Your Android Lock Screen — Fast, Safe &amp; Easy</h1>
  <p>Forgot your PIN, pattern, password, or fingerprint? Dr.Fone removes any Android lock in minutes — no data loss on supported Samsung devices.</p>
  {cta("🔓 Download Dr.Fone Free")} {cta("See How It Works","btn-sec")}
</div>

<main>
<div class="trust-bar">
  <div class="trust-item"><strong>50M+</strong>Users Helped</div>
  <div class="trust-item"><strong>2000+</strong>Device Models</div>
  <div class="trust-item"><strong>29+</strong>Android Brands</div>
  <div class="trust-item"><strong>4.5★</strong>User Rating</div>
  <div class="trust-item"><strong>7-Day</strong>Money-Back</div>
</div>

<h2>Why You're Locked Out — and How to Fix It</h2>
<p>Millions of Android users get locked out every day. Whether you forgot your PIN after a long vacation, your fingerprint sensor stopped responding, or you bought a second-hand phone that's still locked — there's a solution that takes under 5 minutes.</p>

<div class="cards">
  <div class="card"><div class="icon">🔢</div><h3>Forgotten PIN or Password</h3><p>Can't remember the digits you set months ago? Dr.Fone removes it completely without wiping your photos, contacts, or apps.</p></div>
  <div class="card"><div class="icon">✋</div><h3>Pattern Lock Bypass</h3><p>Swiped the wrong pattern too many times? Unlock any Android pattern lock in under 3 minutes.</p></div>
  <div class="card"><div class="icon">👆</div><h3>Fingerprint Not Working</h3><p>Wet hands, screen protectors, or sensor glitches — remove the biometric lock and set up fresh fingerprints.</p></div>
  <div class="card"><div class="icon">🔐</div><h3>Google FRP Lock</h3><p>Stuck on Google account verification after a factory reset? Bypass FRP on Samsung, Xiaomi, Huawei &amp; more.</p></div>
  <div class="card"><div class="icon">📱</div><h3>Second-Hand Phone Locked</h3><p>Bought a used Android that's still locked to the previous owner's account? Get full access in minutes.</p></div>
  <div class="card"><div class="icon">😶</div><h3>Face Unlock Disabled</h3><p>Face recognition refuses to work? Clear it and set up a new biometric without losing any data.</p></div>
</div>

<h2>How to Unlock Your Android in 3 Steps</h2>
<div class="steps">
  <div class="step"><div class="step-num">1</div><div class="step-body"><h3>Download &amp; Install Dr.Fone</h3><p>Free download for Windows and Mac. Install takes under 2 minutes. No technical knowledge needed.</p></div></div>
  <div class="step"><div class="step-num">2</div><div class="step-body"><h3>Connect Your Phone via USB</h3><p>Select "Screen Unlock" → "Android" → "Unlock Android Screen". Dr.Fone detects your device automatically.</p></div></div>
  <div class="step"><div class="step-num">3</div><div class="step-body"><h3>Unlock Complete</h3><p>Follow the on-screen guide. Your phone is unlocked in 2–5 minutes. Set a new PIN or biometric right away.</p></div></div>
</div>
{cta("🔓 Unlock My Android Now")}

<h2>Supported Android Brands</h2>
<div class="brands">
  <a href="{SITE_URL}/brands/samsung/" class="brand-card">Samsung</a>
  <a href="{SITE_URL}/brands/huawei/" class="brand-card">Huawei</a>
  <a href="{SITE_URL}/brands/xiaomi/" class="brand-card">Xiaomi</a>
  <a href="{SITE_URL}/brands/oppo/" class="brand-card">OPPO</a>
  <a href="{SITE_URL}/brands/vivo/" class="brand-card">Vivo</a>
  <a href="{SITE_URL}/brands/lg/" class="brand-card">LG</a>
  <a href="{SITE_URL}/brands/motorola/" class="brand-card">Motorola</a>
  <a href="{SITE_URL}/brands/oneplus/" class="brand-card">OnePlus</a>
  <div class="brand-card">Nokia</div>
  <div class="brand-card">Sony</div>
  <div class="brand-card">Realme</div>
  <div class="brand-card">ZTE</div>
  <div class="brand-card">Lenovo</div>
  <div class="brand-card">Asus</div>
  <div class="brand-card">Google Pixel</div>
  <div class="brand-card">TCL</div>
</div>

<h2>What Lock Types Can Dr.Fone Remove?</h2>
<div class="badge-row">
  <span class="badge">PIN Lock</span>
  <span class="badge">Password Lock</span>
  <span class="badge">Pattern Lock</span>
  <span class="badge">Fingerprint Lock</span>
  <span class="badge">Face Unlock</span>
  <span class="badge">Google FRP</span>
  <span class="badge">Samsung FRP</span>
  <span class="badge">MDM Lock</span>
</div>

<h2>Frequently Asked Questions</h2>
<div class="faq">
  <div class="faq-item"><div class="faq-q">Will I lose my data when unlocking?</div><div class="faq-a">For most Samsung devices, Dr.Fone can unlock without any data loss. For other brands, a factory reset may be required — but Dr.Fone also includes a backup tool to save your data first.</div></div>
  <div class="faq-item"><div class="faq-q">Does it work on the latest Android versions?</div><div class="faq-a">Yes. Dr.Fone supports Android 16 and all earlier versions, including Android 15, 14, 13, and 12.</div></div>
  <div class="faq-item"><div class="faq-q">Is Dr.Fone safe to use?</div><div class="faq-a">Absolutely. Wondershare Dr.Fone is trusted by over 50 million users globally. It uses encrypted connections and never uploads your personal data.</div></div>
  <div class="faq-item"><div class="faq-q">Can I unlock without a computer?</div><div class="faq-a">The desktop software provides the most reliable results. You'll need a Windows or Mac computer and a USB cable to connect your Android device.</div></div>
  <div class="faq-item"><div class="faq-q">What if my phone brand isn't listed?</div><div class="faq-a">Dr.Fone supports 29+ brands and 2000+ device models. Download the free trial to check compatibility with your specific device model before purchasing.</div></div>
</div>

<div class="cta-box">
  <h2>Ready to Unlock Your Android?</h2>
  <p>Free download — try it before you buy. 7-day money-back guarantee if it doesn't work for your device.</p>
  {cta("🔓 Download Dr.Fone Free")}
</div>
</main>"""
    return page(
        f"Android Locked Screen Unlock — Remove PIN, Pattern &amp; FRP ({YEAR})",
        "Locked out of your Android? Remove PIN, password, pattern, fingerprint &amp; FRP lock in minutes with Dr.Fone. Supports Samsung, Huawei, Xiaomi, 29+ brands.",
        "android locked screen unlock, android lock screen removal, forgot android pin, bypass android lock, remove android password, android frp bypass, unlock android phone",
        body
    )

# ── SAMSUNG PAGE ─────────────────────────────────────────────────────────────
def build_samsung():
    body = f"""
<div class="hero">
  <h1>Unlock Samsung Locked Screen — No Data Loss</h1>
  <p>Dr.Fone removes Samsung PIN, pattern, password &amp; FRP — with a unique no-data-loss feature for Samsung Galaxy devices.</p>
  {cta("🔓 Unlock Samsung Now")}
</div>
<main>
<h2>Why Samsung Users Choose Dr.Fone</h2>
<div class="cards">
  <div class="card"><div class="icon">💾</div><h3>No Data Loss</h3><p>Exclusive Samsung technology preserves all your photos, contacts, and apps during the unlock process.</p></div>
  <div class="card"><div class="icon">⚡</div><h3>3-Minute Unlock</h3><p>From plugging in your USB cable to full access — the entire process takes around 3 minutes.</p></div>
  <div class="card"><div class="icon">✅</div><h3>Supports Android 16</h3><p>Works on the latest Samsung Galaxy S26, S25, S24, Note 20, A series, Z Fold &amp; Flip series.</p></div>
  <div class="card"><div class="icon">🔐</div><h3>FRP Bypass Included</h3><p>Bypass Google FRP / Samsung FRP after factory reset — even if you don't remember the original Google account.</p></div>
</div>
<h2>Supported Samsung Models</h2>
<div class="badge-row">
  <span class="badge">Galaxy S26/S25/S24/S23</span>
  <span class="badge">Galaxy S22/S21/S20</span>
  <span class="badge">Galaxy Note 20/10/9</span>
  <span class="badge">Galaxy A52/A71/A53</span>
  <span class="badge">Galaxy Z Fold 5/6</span>
  <span class="badge">Galaxy Z Flip 5/6</span>
  <span class="badge">Galaxy Tab Series</span>
  <span class="badge">Snapdragon Variants</span>
</div>
<h2>How to Unlock Samsung Without Data Loss</h2>
<div class="steps">
  <div class="step"><div class="step-num">1</div><div class="step-body"><h3>Launch Dr.Fone, Select Screen Unlock</h3><p>Open Dr.Fone on your PC/Mac. Go to Toolbox → Screen Unlock → Android.</p></div></div>
  <div class="step"><div class="step-num">2</div><div class="step-body"><h3>Select Samsung &amp; "Remove Without Data Loss"</h3><p>Choose your Samsung model. Select the "Remove without Data Loss" option to protect your files.</p></div></div>
  <div class="step"><div class="step-num">3</div><div class="step-body"><h3>Enter Download Mode</h3><p>Follow on-screen instructions to put your Samsung in Download Mode. Dr.Fone handles the rest automatically.</p></div></div>
  <div class="step"><div class="step-num">4</div><div class="step-body"><h3>Unlock Complete — All Data Intact</h3><p>Your Samsung is unlocked in under 5 minutes. All photos, contacts, and apps are preserved.</p></div></div>
</div>
{cta("🔓 Unlock Samsung Free Trial")}
</main>"""
    return page(
        f"Unlock Samsung Locked Screen Without Data Loss ({YEAR}) | Dr.Fone",
        "Unlock Samsung Galaxy locked screen without losing data. Remove PIN, pattern, password &amp; FRP on Galaxy S/A/Note/Z series. Free trial available.",
        "unlock samsung locked screen, samsung frp bypass, samsung pin unlock, samsung pattern unlock, galaxy locked screen, samsung screen unlock no data loss",
        body, canonical=f"{SITE_URL}/samsung/"
    )

# ── FRP PAGE ─────────────────────────────────────────────────────────────────
def build_frp():
    body = f"""
<div class="hero">
  <h1>Android FRP Bypass — Unlock Google Account Lock</h1>
  <p>Stuck on "This device was reset" screen? Bypass Google FRP (Factory Reset Protection) on any Android phone in minutes.</p>
  {cta("🔓 Bypass FRP Now")}
</div>
<main>
<h2>What Is Google FRP Lock?</h2>
<p>Factory Reset Protection (FRP) is a security feature on Android 5.1+ that activates after a factory reset. It requires you to verify the Google account that was previously synced to the device. If you've forgotten that account — or bought a second-hand phone — you're locked out.</p>
<h2>What Causes FRP Lock?</h2>
<div class="cards">
  <div class="card"><div class="icon">🔄</div><h3>Factory Reset Without Sign-Out</h3><p>Performing a hard reset without first removing your Google account triggers FRP on the next boot.</p></div>
  <div class="card"><div class="icon">📱</div><h3>Bought a Second-Hand Phone</h3><p>The previous owner forgot to remove their Google account before selling. Their FRP lock remains active.</p></div>
  <div class="card"><div class="icon">🔑</div><h3>Forgotten Google Account</h3><p>You remember the phone but not the Gmail address or password linked to it.</p></div>
  <div class="card"><div class="icon">💀</div><h3>Deceased Owner's Device</h3><p>A family member's device needs to be accessed but the credentials are unknown.</p></div>
</div>
<h2>How to Bypass FRP with Dr.Fone</h2>
<div class="steps">
  <div class="step"><div class="step-num">1</div><div class="step-body"><h3>Download Dr.Fone &amp; Select FRP Unlock</h3><p>Install Dr.Fone on your computer. Select "Screen Unlock" → "Android" → "Remove Google FRP Lock".</p></div></div>
  <div class="step"><div class="step-num">2</div><div class="step-body"><h3>Choose Your Device Brand</h3><p>Select Samsung, Xiaomi, Huawei, OPPO, Vivo, or your specific brand. Dr.Fone shows the correct method.</p></div></div>
  <div class="step"><div class="step-num">3</div><div class="step-body"><h3>Follow On-Screen Instructions</h3><p>Dr.Fone guides you through enabling USB debugging or using an EDL cable for Samsung Snapdragon devices.</p></div></div>
  <div class="step"><div class="step-num">4</div><div class="step-body"><h3>FRP Removed — Device Unlocked</h3><p>The Google account lock is permanently removed. Set up a new Google account and start fresh.</p></div></div>
</div>
{cta("🔓 Bypass Google FRP Free Trial")}
<h2>FRP Bypass by Brand</h2>
<table>
  <tr><th>Brand</th><th>FRP Support</th><th>Method</th><th>Data Loss?</th></tr>
  <tr><td>Samsung Snapdragon</td><td>✅ 100% Success</td><td>EDL Cable</td><td>No</td></tr>
  <tr><td>Samsung Exynos</td><td>✅ Full Support</td><td>Download Mode</td><td>No</td></tr>
  <tr><td>Xiaomi / MIUI</td><td>✅ Supported</td><td>ADB Method</td><td>May vary</td></tr>
  <tr><td>Huawei / Honor</td><td>✅ Supported</td><td>USB Method</td><td>May vary</td></tr>
  <tr><td>OPPO / Realme</td><td>✅ Supported</td><td>Recovery Mode</td><td>May vary</td></tr>
  <tr><td>Vivo</td><td>✅ Supported</td><td>ADB Method</td><td>May vary</td></tr>
</table>
</main>"""
    return page(
        f"Android FRP Bypass — Remove Google Account Lock ({YEAR}) | Dr.Fone",
        "Bypass Google FRP lock on any Android phone. Remove Factory Reset Protection on Samsung, Xiaomi, Huawei, OPPO &amp; more. 100% working method.",
        "android frp bypass, google frp unlock, factory reset protection bypass, remove google account lock android, samsung frp bypass, frp lock removal",
        body, canonical=f"{SITE_URL}/frp/"
    )

# ── FORGOT PASSWORD PAGE ─────────────────────────────────────────────────────
def build_forgot():
    body = f"""
<div class="hero">
  <h1>Forgot Android Phone Password? Here's the Fix</h1>
  <p>Completely forgot your Android PIN, pattern, or password? Regain full access in under 5 minutes — no Google account needed.</p>
  {cta("🔓 Recover Access Now")}
</div>
<main>
<h2>Why Android Passwords Are Easy to Forget</h2>
<p>Modern Android devices encourage biometric authentication — fingerprint and face unlock — so most users only set a PIN or password as a backup. After weeks of only using your fingerprint, it's completely natural to forget the 4-digit PIN you set last year. Dr.Fone removes it permanently so you can set a new, memorable one.</p>
<h2>5 Situations Dr.Fone Can Fix</h2>
<div class="cards">
  <div class="card"><div class="icon">🧠</div><h3>Completely Forgot the PIN</h3><p>No need to remember — Dr.Fone bypasses it entirely. Works even after too many failed attempts.</p></div>
  <div class="card"><div class="icon">📵</div><h3>Phone Disabled After Wrong Attempts</h3><p>"Phone is disabled, try again in 30 minutes" — Dr.Fone skips the waiting and unlocks immediately.</p></div>
  <div class="card"><div class="icon">🛒</div><h3>Bought a Used / Refurbished Phone</h3><p>Second-hand phone still locked to someone else's PIN? Get full unrestricted access in minutes.</p></div>
  <div class="card"><div class="icon">💔</div><h3>Broken Touchscreen</h3><p>Screen won't respond to swipes or taps, so you can't enter your PIN? Dr.Fone unlocks via USB from your PC.</p></div>
  <div class="card"><div class="icon">🔒</div><h3>MDM / Work Lock</h3><p>Company MDM profile preventing personal use? Dr.Fone can help remove enterprise device management locks.</p></div>
  <div class="card"><div class="icon">🌊</div><h3>Water Damaged Device</h3><p>Water-damaged touchscreen can't register input? Connect via USB and unlock remotely through Dr.Fone.</p></div>
</div>
{cta("🔓 Unlock Forgotten Password")}
<h2>Free Alternatives (Limited)</h2>
<p>Before purchasing, try these free methods — they work in specific situations:</p>
<table>
  <tr><th>Method</th><th>Works When</th><th>Data Loss?</th></tr>
  <tr><td>Google Find My Device</td><td>Phone online &amp; signed in</td><td>Yes (remote erase)</td></tr>
  <tr><td>Samsung Find My Mobile</td><td>Samsung account set up</td><td>No</td></tr>
  <tr><td>Factory Reset (Recovery Mode)</td><td>Always</td><td>Yes — all data wiped</td></tr>
  <tr><td>Dr.Fone Screen Unlock</td><td>Any situation</td><td>No (Samsung) / varies</td></tr>
</table>
</main>"""
    return page(
        f"Forgot Android Password? Unlock in 5 Minutes ({YEAR}) | Dr.Fone",
        "Forgot your Android PIN, password or pattern? Remove the lock in 5 minutes with Dr.Fone. No data loss on Samsung. Works on 2000+ Android models.",
        "forgot android password, forgot android pin, forgot android pattern, android locked out, bypass android lock screen, unlock android forgot password",
        body, canonical=f"{SITE_URL}/forgot-password/"
    )

# ── NO DATA LOSS PAGE ────────────────────────────────────────────────────────
def build_no_data_loss():
    body = f"""
<div class="hero">
  <h1>Unlock Android Without Losing Data</h1>
  <p>Most unlock methods wipe your phone. Dr.Fone is the only tool that can remove Samsung locks while keeping every photo, contact, and app intact.</p>
  {cta("🔓 Unlock Without Data Loss")}
</div>
<main>
<h2>Why Most Methods Delete Your Data</h2>
<p>A standard factory reset is the easiest way to remove a lock screen — but it permanently deletes everything. Dr.Fone's patented technology bypasses the lock at the firmware level without triggering a data wipe on supported Samsung devices.</p>
<h2>What's Preserved After Unlocking</h2>
<div class="cards">
  <div class="card"><div class="icon">🖼️</div><h3>Photos &amp; Videos</h3><p>All media stored on internal storage and SD card remains untouched after the unlock process.</p></div>
  <div class="card"><div class="icon">👥</div><h3>Contacts &amp; Messages</h3><p>Your entire contact list, SMS history, and call logs are preserved and accessible immediately.</p></div>
  <div class="card"><div class="icon">📲</div><h3>Apps &amp; App Data</h3><p>All installed applications and their saved data, accounts, and preferences remain intact.</p></div>
  <div class="card"><div class="icon">📧</div><h3>Email &amp; Accounts</h3><p>Google, Samsung, and third-party accounts stay signed in after unlocking.</p></div>
</div>
<h2>No-Data-Loss Support by Device</h2>
<table>
  <tr><th>Device Type</th><th>No Data Loss?</th><th>Notes</th></tr>
  <tr><td>Samsung Galaxy S Series</td><td>✅ Yes</td><td>S10 through S26</td></tr>
  <tr><td>Samsung Galaxy A Series</td><td>✅ Yes</td><td>Most models</td></tr>
  <tr><td>Samsung Galaxy Note Series</td><td>✅ Yes</td><td>Note 9 through Note 20</td></tr>
  <tr><td>Samsung Galaxy Z Series</td><td>✅ Yes</td><td>Fold and Flip</td></tr>
  <tr><td>Other Android Brands</td><td>⚠️ Partial</td><td>Backup first recommended</td></tr>
</table>
{cta("🔓 Try Free — No Data Lost")}
</main>"""
    return page(
        f"Unlock Android Without Losing Data ({YEAR}) | Dr.Fone",
        "Remove Android lock screen without losing photos, contacts or apps. Dr.Fone's no-data-loss unlock works on Samsung Galaxy S, A, Note, and Z series.",
        "unlock android without data loss, remove android lock screen keep data, bypass android lock no data loss, samsung unlock no data loss",
        body, canonical=f"{SITE_URL}/no-data-loss/"
    )

# ── FREE DOWNLOAD PAGE ───────────────────────────────────────────────────────
def build_download():
    body = f"""
<div class="hero">
  <h1>Download Dr.Fone — Android Screen Unlock</h1>
  <p>Free download for Windows &amp; Mac. Try before you buy — see if your device is fully supported before purchasing a license.</p>
  {cta("⬇️ Free Download")}
</div>
<main>
<h2>What's Included in the Free Trial</h2>
<div class="cards">
  <div class="card"><div class="icon">✅</div><h3>Device Compatibility Check</h3><p>See whether your exact phone model is fully supported before spending a penny.</p></div>
  <div class="card"><div class="icon">🔍</div><h3>Lock Type Detection</h3><p>Dr.Fone automatically detects what type of lock is on your device and shows the best removal method.</p></div>
  <div class="card"><div class="icon">📋</div><h3>Step-by-Step Preview</h3><p>Walk through the full unlock process and see exactly what will happen before committing.</p></div>
  <div class="card"><div class="icon">💰</div><h3>7-Day Money-Back</h3><p>If Dr.Fone doesn't unlock your device after purchase, Wondershare offers a full refund — no questions asked.</p></div>
</div>
<h2>System Requirements</h2>
<table>
  <tr><th>Platform</th><th>Requirement</th></tr>
  <tr><td>Windows</td><td>Windows 7/8/10/11 (32-bit or 64-bit)</td></tr>
  <tr><td>Mac</td><td>macOS 10.12 or later</td></tr>
  <tr><td>RAM</td><td>Minimum 256 MB (512 MB recommended)</td></tr>
  <tr><td>Hard Disk</td><td>200 MB free space</td></tr>
  <tr><td>USB Port</td><td>Required to connect Android device</td></tr>
</table>
<div class="cta-box">
  <h2>Ready to Get Your Phone Back?</h2>
  <p>Download takes under 60 seconds. Installation is straightforward for any user level.</p>
  {cta("⬇️ Download Dr.Fone Free")}
</div>
</main>"""
    return page(
        f"Download Dr.Fone Android Screen Unlock — Free Trial ({YEAR})",
        "Download Wondershare Dr.Fone Screen Unlock for Android free. Available for Windows &amp; Mac. Free trial — check compatibility before you buy.",
        "download drfone android, dr.fone free download, android unlock software download, wondershare drfone download",
        body, canonical=f"{SITE_URL}/free-download/"
    )

# ── PATTERN LOCK PAGE ────────────────────────────────────────────────────────
def build_pattern():
    body = f"""
<div class="hero">
  <h1>Remove Android Pattern Lock — Instant Bypass</h1>
  <p>Swiped the wrong pattern too many times? Or just can't remember it? Dr.Fone removes any Android pattern lock in under 3 minutes.</p>
  {cta("🔓 Remove Pattern Lock")}
</div>
<main>
<h2>Why Pattern Locks Get Forgotten</h2>
<p>Pattern locks seem easy to remember when you set them — but after weeks of using fingerprint unlock, the pattern becomes unfamiliar. Dr.Fone completely removes the pattern lock so you can set a new, simpler one.</p>
<h2>Pattern Lock vs Other Lock Types</h2>
<table>
  <tr><th>Lock Type</th><th>Forgettable?</th><th>Dr.Fone Removes?</th></tr>
  <tr><td>Pattern Lock</td><td>High</td><td>✅ Yes</td></tr>
  <tr><td>PIN Lock</td><td>Medium</td><td>✅ Yes</td></tr>
  <tr><td>Password Lock</td><td>Medium</td><td>✅ Yes</td></tr>
  <tr><td>Fingerprint</td><td>Low</td><td>✅ Yes</td></tr>
  <tr><td>Face Unlock</td><td>Low</td><td>✅ Yes</td></tr>
</table>
{cta("🔓 Bypass Pattern Lock Free")}
</main>"""
    return page(
        f"Remove Android Pattern Lock — Bypass in 3 Minutes ({YEAR})",
        "Forgot your Android pattern lock? Remove any pattern lock in under 3 minutes with Dr.Fone. Works on all Android brands without factory reset.",
        "android pattern lock bypass, remove android pattern lock, forgot android pattern, unlock android pattern, bypass pattern lock android",
        body, canonical=f"{SITE_URL}/pattern/"
    )

# ── FINGERPRINT PAGE ─────────────────────────────────────────────────────────
def build_fingerprint():
    body = f"""
<div class="hero">
  <h1>Android Fingerprint Lock Not Working? Fix It Now</h1>
  <p>Fingerprint sensor not recognizing your touch? Dr.Fone removes the biometric lock so you can re-enroll fresh fingerprints on your Android device.</p>
  {cta("🔓 Fix Fingerprint Lock")}
</div>
<main>
<h2>Why Fingerprint Locks Fail</h2>
<div class="cards">
  <div class="card"><div class="icon">💧</div><h3>Wet or Dirty Fingers</h3><p>Moisture, lotion, or oil on your fingertip prevents the sensor from accurately reading your print.</p></div>
  <div class="card"><div class="icon">🛡️</div><h3>Screen Protector Blocking</h3><p>Thick or poorly positioned screen protectors interfere with under-display fingerprint sensors on modern phones.</p></div>
  <div class="card"><div class="icon">🔄</div><h3>Software Update Bug</h3><p>Android system updates occasionally break fingerprint sensor calibration, requiring a fresh re-enroll.</p></div>
  <div class="card"><div class="icon">🤕</div><h3>Injury or Changed Skin</h3><p>Cuts, burns, or dry skin changes your fingerprint profile, making the sensor unable to match.</p></div>
</div>
<h2>Solution: Remove &amp; Re-Enroll</h2>
<p>The fastest fix is to remove the current fingerprint lock entirely using Dr.Fone, then set up a fresh fingerprint when the phone is unlocked. This resolves all sensor calibration and matching issues instantly.</p>
{cta("🔓 Remove Fingerprint Lock")}
</main>"""
    return page(
        f"Android Fingerprint Lock Not Working — Fix in Minutes ({YEAR})",
        "Android fingerprint not working? Remove the biometric lock with Dr.Fone and re-enroll fresh fingerprints. Works on all Android phones.",
        "android fingerprint not working, remove android fingerprint lock, bypass fingerprint android, android biometric lock fix",
        body, canonical=f"{SITE_URL}/fingerprint/"
    )

# ── VS COMPETITORS PAGE ──────────────────────────────────────────────────────
def build_vs():
    body = f"""
<div class="hero">
  <h1>Dr.Fone vs Other Android Unlock Tools</h1>
  <p>How does Dr.Fone compare to free and paid alternatives? We break down the differences so you can make the right choice.</p>
  {cta("🔓 Try Dr.Fone Free")}
</div>
<main>
<h2>Comparison: Dr.Fone vs Alternatives</h2>
<table>
  <tr><th>Feature</th><th>Dr.Fone</th><th>Google Find My Device</th><th>Factory Reset</th><th>iMyFone LockWiper</th></tr>
  <tr><td>No Data Loss (Samsung)</td><td>✅ Yes</td><td>❌ No</td><td>❌ No</td><td>⚠️ Partial</td></tr>
  <tr><td>Works Offline</td><td>✅ Yes</td><td>❌ No</td><td>✅ Yes</td><td>✅ Yes</td></tr>
  <tr><td>FRP Bypass</td><td>✅ Yes</td><td>❌ No</td><td>❌ No</td><td>✅ Yes</td></tr>
  <tr><td>29+ Brands Supported</td><td>✅ Yes</td><td>❌ Android only</td><td>✅ Yes</td><td>⚠️ Fewer</td></tr>
  <tr><td>Android 16 Support</td><td>✅ Yes</td><td>✅ Yes</td><td>✅ Yes</td><td>⚠️ Varies</td></tr>
  <tr><td>Price</td><td>Free Trial</td><td>Free</td><td>Free</td><td>Paid</td></tr>
  <tr><td>Money-Back Guarantee</td><td>✅ 7 Days</td><td>N/A</td><td>N/A</td><td>⚠️ Varies</td></tr>
</table>
<h2>Verdict</h2>
<p>For Samsung users who need no data loss, Dr.Fone is unmatched. For all other Android brands, Dr.Fone's broad compatibility and FRP support make it the most versatile paid solution. The free trial lets you verify compatibility before purchasing.</p>
{cta("🔓 Download Dr.Fone Free Trial")}
</main>"""
    return page(
        f"Dr.Fone vs Other Android Unlock Tools — Comparison ({YEAR})",
        "Compare Dr.Fone Screen Unlock against Google Find My Device, factory reset, and iMyFone. Which Android unlock tool is best for your situation?",
        "dr.fone vs alternatives, best android unlock tool, android screen unlock comparison, drfone review",
        body, canonical=f"{SITE_URL}/vs-competitors/"
    )

# ── GLOBAL PAGE ──────────────────────────────────────────────────────────────
def build_global():
    regions = [
        ("🇺🇸 English","lang/de","en"),
        ("🇩🇪 Deutsch","lang/de","de"),
        ("🇫🇷 Français","lang/fr","fr"),
        ("🇪🇸 Español","lang/es","es"),
        ("🇧🇷 Português","lang/pt","pt"),
        ("🇮🇹 Italiano","lang/it","it"),
        ("🇯🇵 日本語","lang/ja","ja"),
        ("🇨🇳 中文","lang/zh","zh"),
        ("🇰🇷 한국어","lang/ko","ko"),
        ("🇷🇺 Русский","lang/ru","ru"),
        ("🇸🇦 العربية","lang/ar","ar"),
        ("🇮🇳 हिन्दी","lang/hi","hi"),
        ("🇮🇩 Indonesia","lang/id","id"),
        ("🇳🇱 Nederlands","lang/nl","nl"),
        ("🇵🇱 Polski","lang/pl","pl"),
        ("🇹🇷 Türkçe","lang/tr","tr"),
        ("🇸🇪 Svenska","lang/sv","sv"),
        ("🇵🇭 Filipino","lang/fil","fil"),
        ("🇻🇳 Tiếng Việt","lang/vi","vi"),
        ("🇹🇭 ภาษาไทย","lang/th","th"),
    ]
    cards = ""
    for label, path, code in regions:
        url = f"{SITE_URL}/{path}/"
        cards += f'<a href="{url}" class="brand-card" style="font-size:1.05rem;padding:20px">{label}</a>'
    body = f"""
<div class="hero">
  <h1>🌍 Android Lock Screen Unlock — Global Versions</h1>
  <p>AndroidLockedScreen is available in 20 languages. Choose your language for a fully localized experience.</p>
</div>
<main>
<h2>Select Your Language / Region</h2>
<div class="brands" style="grid-template-columns:repeat(auto-fit,minmax(160px,1fr))">{cards}</div>
<div class="cta-box">
  <h2>Download Dr.Fone — Available Worldwide</h2>
  <p>Works in every country. Windows &amp; Mac. Free trial available globally.</p>
  {cta("🔓 Download Free")}
</div>
</main>"""
    return page("Android Locked Screen — Global Language Versions | Dr.Fone",
        "Android locked screen unlock guide available in 20 languages. English, Deutsch, Français, Español, Português, 日本語, 中文, 한국어 &amp; more.",
        "android locked screen global, unlock android worldwide, android lock screen multilingual",
        body, canonical=f"{SITE_URL}/global/")

# ── LANGUAGE PAGES ────────────────────────────────────────────────────────────
LANG_PAGES = {
    "de": {
        "lang":"de","title":f"Android Gesperrten Bildschirm Entsperren — Dr.Fone ({YEAR})",
        "desc":"Android PIN, Muster oder Passwort vergessen? Dr.Fone entsperrt jeden Android-Bildschirm in Minuten. Kein Datenverlust bei Samsung.",
        "kw":"android gesperrter bildschirm, android entsperren, android pin vergessen, android muster entfernen, samsung entsperren",
        "h1":"Android Gesperrten Bildschirm Entsperren",
        "p":"PIN, Muster oder Passwort vergessen? Dr.Fone entfernt jede Android-Bildschirmsperre in wenigen Minuten — ohne Datenverlust bei Samsung-Geräten.",
        "feat":[("🔢","PIN &amp; Passwort","Jede Ziffernkombination oder alphanumerisches Passwort wird sofort entfernt."),
                ("✋","Muster-Sperre","Geschwungenes Entsperrmuster vergessen? Dr.Fone umgeht es vollständig."),
                ("🔐","Google FRP","FRP-Sperre nach Werksreset? Wird für Samsung, Xiaomi, Huawei und mehr entfernt."),
                ("💾","Kein Datenverlust","Alle Fotos, Kontakte und Apps bleiben bei unterstützten Samsung-Geräten erhalten.")]
    },
    "fr": {
        "lang":"fr","title":f"Déverrouiller Écran Android Bloqué — Dr.Fone ({YEAR})",
        "desc":"Oublié votre PIN, schéma ou mot de passe Android? Dr.Fone déverrouille n'importe quel écran Android en quelques minutes. Sans perte de données sur Samsung.",
        "kw":"déverrouiller android, écran android bloqué, oublié pin android, contourner verrouillage android, samsung déverrouiller",
        "h1":"Déverrouiller l'Écran Android Bloqué",
        "p":"PIN, schéma ou mot de passe oublié? Dr.Fone supprime n'importe quel verrouillage d'écran Android en quelques minutes — sans perte de données sur Samsung.",
        "feat":[("🔢","PIN &amp; Mot de Passe","Supprime instantanément tout code PIN ou mot de passe alphanumérique."),
                ("✋","Schéma de Déverrouillage","Schéma oublié? Dr.Fone le contourne complètement."),
                ("🔐","FRP Google","Verrou FRP après réinitialisation? Supprimé pour Samsung, Xiaomi, Huawei et plus."),
                ("💾","Sans Perte de Données","Toutes les photos, contacts et applications restent intacts sur Samsung.")]
    },
    "es": {
        "lang":"es","title":f"Desbloquear Pantalla Android Bloqueada — Dr.Fone ({YEAR})",
        "desc":"¿Olvidaste el PIN, patrón o contraseña de Android? Dr.Fone desbloquea cualquier pantalla Android en minutos. Sin pérdida de datos en Samsung.",
        "kw":"desbloquear android, pantalla android bloqueada, olvidé pin android, bypass pantalla android, samsung desbloquear, frp bypass android",
        "h1":"Desbloquear Pantalla Android Bloqueada",
        "p":"¿PIN, patrón o contraseña olvidados? Dr.Fone elimina cualquier bloqueo de pantalla Android en minutos — sin pérdida de datos en Samsung.",
        "feat":[("🔢","PIN y Contraseña","Elimina cualquier PIN o contraseña alfanumérica de inmediato."),
                ("✋","Patrón de Desbloqueo","¿Olvidaste el patrón? Dr.Fone lo omite completamente en 3 minutos."),
                ("🔐","FRP de Google","¿Bloqueo FRP tras restablecimiento? Eliminado en Samsung, Xiaomi, Huawei y más."),
                ("💾","Sin Pérdida de Datos","Fotos, contactos y apps intactos en dispositivos Samsung compatibles.")]
    },
    "pt": {
        "lang":"pt","title":f"Desbloquear Tela Android Bloqueada — Dr.Fone ({YEAR})",
        "desc":"Esqueceu o PIN, padrão ou senha do Android? Dr.Fone desbloqueia qualquer tela Android em minutos. Sem perda de dados no Samsung.",
        "kw":"desbloquear android, tela android bloqueada, esqueci pin android, bypass android, samsung desbloquear, frp bypass",
        "h1":"Desbloquear Tela Android Bloqueada",
        "p":"PIN, padrão ou senha esquecidos? Dr.Fone remove qualquer bloqueio de tela Android em minutos — sem perda de dados no Samsung.",
        "feat":[("🔢","PIN e Senha","Remove qualquer PIN ou senha alfanumérica instantaneamente."),
                ("✋","Padrão de Desbloqueio","Padrão esquecido? Dr.Fone ignora completamente em 3 minutos."),
                ("🔐","FRP do Google","Bloqueio FRP após reset? Removido no Samsung, Xiaomi, Huawei e mais."),
                ("💾","Sem Perda de Dados","Fotos, contatos e apps intactos em dispositivos Samsung suportados.")]
    },
    "it": {
        "lang":"it","title":f"Sbloccare Schermo Android Bloccato — Dr.Fone ({YEAR})",
        "desc":"Dimenticato PIN, sequenza o password Android? Dr.Fone sblocca qualsiasi schermo Android in pochi minuti. Senza perdita di dati su Samsung.",
        "kw":"sbloccare android, schermo android bloccato, dimenticato pin android, bypassare blocco android, samsung sbloccare",
        "h1":"Sbloccare lo Schermo Android Bloccato",
        "p":"PIN, sequenza o password dimenticati? Dr.Fone rimuove qualsiasi blocco schermo Android in pochi minuti — senza perdita di dati su Samsung.",
        "feat":[("🔢","PIN e Password","Rimuove immediatamente qualsiasi PIN o password alfanumerica."),
                ("✋","Sequenza di Sblocco","Sequenza dimenticata? Dr.Fone la ignora completamente in 3 minuti."),
                ("🔐","FRP Google","Blocco FRP dopo il ripristino? Rimosso su Samsung, Xiaomi, Huawei e altri."),
                ("💾","Nessuna Perdita di Dati","Foto, contatti e app intatti sui dispositivi Samsung supportati.")]
    },
    "ja": {
        "lang":"ja","title":f"Androidロック画面を解除 — Dr.Fone ({YEAR})",
        "desc":"AndroidのPIN・パターン・パスワードを忘れた？Dr.FoneがすべてのAndroidロックを数分で解除。Samsung端末はデータ損失なし。",
        "kw":"android ロック解除, android 画面ロック, pin 忘れた android, パターン ロック 解除, samsung ロック解除, frp バイパス",
        "h1":"Androidロック画面を解除する",
        "p":"PIN・パターン・パスワードを忘れましたか？Dr.Foneは数分以内にAndroidの画面ロックを解除します。Samsung端末ではデータ損失なし。",
        "feat":[("🔢","PIN・パスワード","数字のPINや英数字パスワードを即座に削除。"),
                ("✋","パターンロック","パターンを忘れた？Dr.Foneが3分以内に完全にバイパス。"),
                ("🔐","Google FRP","工場出荷時リセット後のFRPロック？Samsung・Xiaomi・Huaweiなどで解除。"),
                ("💾","データ損失なし","対応Samsung端末では写真・連絡先・アプリをすべて保持。")]
    },
    "zh": {
        "lang":"zh","title":f"解锁Android锁屏 — Dr.Fone ({YEAR})",
        "desc":"忘记了Android PIN、图案或密码？Dr.Fone几分钟内解锁任意Android屏幕。三星设备无数据丢失。",
        "kw":"android解锁, 安卓锁屏解锁, 忘记android密码, 绕过android锁屏, 三星解锁, frp解锁",
        "h1":"解锁Android锁屏",
        "p":"忘记了PIN码、图案或密码？Dr.Fone几分钟内解除任意Android屏幕锁定——三星设备无数据丢失。",
        "feat":[("🔢","PIN和密码","立即删除任意数字PIN或字母数字密码。"),
                ("✋","图案锁","忘记解锁图案？Dr.Fone在3分钟内完全绕过。"),
                ("🔐","谷歌FRP","恢复出厂设置后的FRP锁？支持三星、小米、华为等品牌。"),
                ("💾","无数据丢失","支持的三星设备上照片、联系人和应用全部保留。")]
    },
    "ko": {
        "lang":"ko","title":f"Android 잠금 화면 해제 — Dr.Fone ({YEAR})",
        "desc":"Android PIN, 패턴, 비밀번호를 잊어버렸나요? Dr.Fone이 몇 분 안에 모든 Android 잠금을 해제합니다. Samsung 기기는 데이터 손실 없음.",
        "kw":"안드로이드 잠금 해제, android 화면 잠금, 핀 잊어버렸어 android, 패턴 잠금 해제, 삼성 잠금 해제, frp 우회",
        "h1":"Android 잠금 화면 해제",
        "p":"PIN, 패턴, 비밀번호를 잊어버렸나요? Dr.Fone이 몇 분 안에 모든 Android 화면 잠금을 해제합니다. Samsung 기기는 데이터 손실 없음.",
        "feat":[("🔢","PIN &amp; 비밀번호","모든 숫자 PIN 또는 영숫자 비밀번호를 즉시 제거."),
                ("✋","패턴 잠금","패턴을 잊었나요? Dr.Fone이 3분 이내에 완전히 우회."),
                ("🔐","Google FRP","공장 초기화 후 FRP 잠금? Samsung, Xiaomi, Huawei 등 지원."),
                ("💾","데이터 손실 없음","지원되는 Samsung 기기에서 사진, 연락처, 앱 모두 보존.")]
    },
    "ru": {
        "lang":"ru","title":f"Разблокировать Android — Снять Блокировку Экрана ({YEAR})",
        "desc":"Забыли PIN, рисунок или пароль Android? Dr.Fone разблокирует любой Android за несколько минут. Без потери данных на Samsung.",
        "kw":"разблокировать android, снять блокировку экрана android, забыл пин android, обход блокировки android, разблокировка samsung, frp обход",
        "h1":"Разблокировать Заблокированный Экран Android",
        "p":"Забыли PIN, рисунок или пароль? Dr.Fone снимает любую блокировку экрана Android за несколько минут — без потери данных на Samsung.",
        "feat":[("🔢","PIN и Пароль","Мгновенно удаляет любой PIN или буквенно-цифровой пароль."),
                ("✋","Графический Ключ","Забыли рисунок? Dr.Fone полностью обходит его за 3 минуты."),
                ("🔐","Google FRP","Блокировка FRP после сброса? Снимается для Samsung, Xiaomi, Huawei и др."),
                ("💾","Без Потери Данных","Фото, контакты и приложения сохраняются на поддерживаемых Samsung.")]
    },
    "ar": {
        "lang":"ar","title":f"فتح شاشة أندرويد المقفلة — Dr.Fone ({YEAR})",
        "desc":"نسيت رمز PIN أو النمط أو كلمة مرور أندرويد؟ Dr.Fone يفتح أي قفل شاشة أندرويد في دقائق. بدون فقدان البيانات على سامسونج.",
        "kw":"فتح قفل أندرويد, إزالة قفل الشاشة, نسيت رمز PIN أندرويد, تجاوز قفل أندرويد, سامسونج فتح القفل",
        "h1":"فتح شاشة أندرويد المقفلة",
        "p":"نسيت رمز PIN أو النمط أو كلمة المرور؟ يزيل Dr.Fone أي قفل شاشة أندرويد في دقائق — بدون فقدان البيانات على أجهزة سامسونج.",
        "feat":[("🔢","PIN وكلمة المرور","يزيل فوراً أي رمز PIN أو كلمة مرور."),
                ("✋","نمط الفتح","نسيت النمط؟ يتجاوزه Dr.Fone كلياً في 3 دقائق."),
                ("🔐","قفل FRP من Google","قفل FRP بعد إعادة الضبط؟ يُزال لسامسونج وشاومي وهواوي والمزيد."),
                ("💾","بدون فقدان البيانات","تبقى الصور وجهات الاتصال والتطبيقات سليمة على أجهزة سامسونج المدعومة.")]
    },
    "hi": {
        "lang":"hi","title":f"Android लॉक स्क्रीन अनलॉक करें — Dr.Fone ({YEAR})",
        "desc":"Android PIN, पैटर्न या पासवर्ड भूल गए? Dr.Fone कुछ ही मिनटों में किसी भी Android स्क्रीन लॉक को हटाता है। Samsung पर डेटा हानि नहीं।",
        "kw":"android अनलॉक, android स्क्रीन लॉक हटाएं, pin भूल गए android, android लॉक बाईपास, samsung अनलॉक, frp बाईपास",
        "h1":"Android लॉक स्क्रीन अनलॉक करें",
        "p":"PIN, पैटर्न या पासवर्ड भूल गए? Dr.Fone कुछ ही मिनटों में किसी भी Android स्क्रीन लॉक को हटाता है — Samsung पर डेटा हानि नहीं।",
        "feat":[("🔢","PIN और पासवर्ड","तुरंत कोई भी PIN या अल्फ़ान्यूमेरिक पासवर्ड हटाएं।"),
                ("✋","पैटर्न लॉक","पैटर्न भूल गए? Dr.Fone 3 मिनट में पूरी तरह बाईपास करता है।"),
                ("🔐","Google FRP","फ़ैक्टरी रीसेट के बाद FRP लॉक? Samsung, Xiaomi, Huawei आदि पर हटाया जाता है।"),
                ("💾","डेटा हानि नहीं","समर्थित Samsung उपकरणों पर फ़ोटो, संपर्क और ऐप सुरक्षित रहते हैं।")]
    },
    "id": {
        "lang":"id","title":f"Buka Kunci Layar Android — Dr.Fone ({YEAR})",
        "desc":"Lupa PIN, pola, atau kata sandi Android? Dr.Fone membuka kunci layar Android apa pun dalam beberapa menit. Tanpa kehilangan data di Samsung.",
        "kw":"buka kunci android, layar android terkunci, lupa pin android, bypass kunci android, samsung buka kunci, frp bypass",
        "h1":"Buka Kunci Layar Android yang Terkunci",
        "p":"Lupa PIN, pola, atau kata sandi? Dr.Fone menghapus kunci layar Android apa pun dalam beberapa menit — tanpa kehilangan data di Samsung.",
        "feat":[("🔢","PIN &amp; Kata Sandi","Hapus PIN atau kata sandi alfanumerik secara instan."),
                ("✋","Pola Kunci","Lupa polanya? Dr.Fone melewatinya sepenuhnya dalam 3 menit."),
                ("🔐","Google FRP","Kunci FRP setelah reset pabrik? Dihapus untuk Samsung, Xiaomi, Huawei, dan lainnya."),
                ("💾","Tanpa Kehilangan Data","Foto, kontak, dan aplikasi tetap aman di perangkat Samsung yang didukung.")]
    },
    "nl": {
        "lang":"nl","title":f"Android Vergrendeld Scherm Ontgrendelen — Dr.Fone ({YEAR})",
        "desc":"Android PIN, patroon of wachtwoord vergeten? Dr.Fone ontgrendelt elk Android-scherm in minuten. Zonder dataverlies op Samsung.",
        "kw":"android ontgrendelen, vergrendeld android scherm, pin vergeten android, android slot verwijderen, samsung ontgrendelen",
        "h1":"Android Vergrendeld Scherm Ontgrendelen",
        "p":"PIN, patroon of wachtwoord vergeten? Dr.Fone verwijdert elke Android-schermvergrendeling in minuten — zonder dataverlies op Samsung.",
        "feat":[("🔢","PIN &amp; Wachtwoord","Verwijdert onmiddellijk elke PIN of alfanumeriek wachtwoord."),
                ("✋","Patroonvergrendeling","Patroon vergeten? Dr.Fone omzeilt het volledig in 3 minuten."),
                ("🔐","Google FRP","FRP-vergrendeling na fabrieksreset? Verwijderd voor Samsung, Xiaomi, Huawei en meer."),
                ("💾","Geen Dataverlies","Foto's, contacten en apps blijven intact op ondersteunde Samsung-apparaten.")]
    },
    "pl": {
        "lang":"pl","title":f"Odblokowanie Zablokowanego Ekranu Android — Dr.Fone ({YEAR})",
        "desc":"Zapomniałeś PINu, wzoru lub hasła Android? Dr.Fone odblokuje każdy ekran Android w kilka minut. Bez utraty danych na Samsungu.",
        "kw":"odblokuj android, zablokowany ekran android, zapomniałem pin android, ominąć blokadę android, samsung odblokuj",
        "h1":"Odblokowanie Zablokowanego Ekranu Android",
        "p":"Zapomniałeś PINu, wzoru lub hasła? Dr.Fone usuwa każdą blokadę ekranu Android w kilka minut — bez utraty danych na Samsungu.",
        "feat":[("🔢","PIN i Hasło","Natychmiast usuwa dowolny PIN lub hasło alfanumeryczne."),
                ("✋","Blokada Wzorem","Zapomniałeś wzoru? Dr.Fone całkowicie go omija w 3 minuty."),
                ("🔐","Google FRP","Blokada FRP po resecie? Usunięta dla Samsunga, Xiaomi, Huawei i innych."),
                ("💾","Bez Utraty Danych","Zdjęcia, kontakty i aplikacje zachowane na obsługiwanych urządzeniach Samsung.")]
    },
    "tr": {
        "lang":"tr","title":f"Android Kilitli Ekranı Aç — Dr.Fone ({YEAR})",
        "desc":"Android PIN, desen veya şifreni mi unuttun? Dr.Fone dakikalar içinde herhangi bir Android ekran kilidini kaldırır. Samsung'da veri kaybı yok.",
        "kw":"android ekran kilidi aç, android kilidi kaldır, pin unuttum android, android bypass, samsung kilit aç, frp bypass",
        "h1":"Android Kilitli Ekranı Aç",
        "p":"PIN, desen veya şifreni mi unuttun? Dr.Fone, dakikalar içinde herhangi bir Android ekran kilidini kaldırır — Samsung'da veri kaybı yok.",
        "feat":[("🔢","PIN ve Şifre","Her türlü PIN veya alfanümerik şifreyi anında kaldırır."),
                ("✋","Desen Kilidi","Deseni mi unuttun? Dr.Fone 3 dakika içinde tamamen atlar."),
                ("🔐","Google FRP","Fabrika sıfırlaması sonrası FRP kilidi? Samsung, Xiaomi, Huawei ve daha fazlası için kaldırılır."),
                ("💾","Veri Kaybı Yok","Desteklenen Samsung cihazlarda fotoğraflar, kişiler ve uygulamalar korunur.")]
    },
    "sv": {
        "lang":"sv","title":f"Lås Upp Android Låst Skärm — Dr.Fone ({YEAR})",
        "desc":"Glömt Android PIN, mönster eller lösenord? Dr.Fone låser upp vilken Android-skärm som helst på minuter. Utan dataförlust på Samsung.",
        "kw":"lås upp android, android låst skärm, glömt pin android, android lås ta bort, samsung lås upp",
        "h1":"Lås Upp Android Låst Skärm",
        "p":"Glömt PIN, mönster eller lösenord? Dr.Fone tar bort vilket Android-skärmlås som helst på minuter — utan dataförlust på Samsung.",
        "feat":[("🔢","PIN och Lösenord","Tar bort valfri PIN eller alfanumeriskt lösenord omedelbart."),
                ("✋","Mönsterlås","Glömt mönstret? Dr.Fone kringgår det helt på 3 minuter."),
                ("🔐","Google FRP","FRP-lås efter fabriksåterställning? Tas bort för Samsung, Xiaomi, Huawei med mera."),
                ("💾","Ingen Dataförlust","Foton, kontakter och appar bevaras på stödda Samsung-enheter.")]
    },
    "fil": {
        "lang":"fil","title":f"I-unlock ang Naka-lock na Android Screen — Dr.Fone ({YEAR})",
        "desc":"Nakalimutan ang Android PIN, pattern, o password? I-unlock ng Dr.Fone ang anumang Android screen lock sa ilang minuto. Walang data loss sa Samsung.",
        "kw":"i-unlock android, naka-lock android screen, nakalimutan pin android, bypass android lock, samsung i-unlock",
        "h1":"I-unlock ang Naka-lock na Android Screen",
        "p":"Nakalimutan ang PIN, pattern, o password? Inalis ng Dr.Fone ang anumang Android screen lock sa ilang minuto — walang data loss sa Samsung.",
        "feat":[("🔢","PIN at Password","Agad na inalis ang anumang PIN o alphanumeric password."),
                ("✋","Pattern Lock","Nakalimutan ang pattern? Nililampasan ito ng Dr.Fone sa loob ng 3 minuto."),
                ("🔐","Google FRP","FRP lock pagkatapos ng factory reset? Inalis para sa Samsung, Xiaomi, Huawei at iba pa."),
                ("💾","Walang Data Loss","Ang mga larawan, contact, at app ay nananatiling buo sa mga sinusuportahang Samsung device.")]
    },
    "vi": {
        "lang":"vi","title":f"Mở Khóa Màn Hình Android — Dr.Fone ({YEAR})",
        "desc":"Quên PIN, hình vẽ hoặc mật khẩu Android? Dr.Fone mở khóa bất kỳ màn hình Android nào trong vài phút. Không mất dữ liệu trên Samsung.",
        "kw":"mở khóa android, màn hình android bị khóa, quên pin android, bypass khóa android, samsung mở khóa, frp bypass",
        "h1":"Mở Khóa Màn Hình Android Bị Khóa",
        "p":"Quên PIN, hình vẽ hoặc mật khẩu? Dr.Fone xóa bất kỳ khóa màn hình Android nào trong vài phút — không mất dữ liệu trên Samsung.",
        "feat":[("🔢","PIN và Mật Khẩu","Xóa ngay lập tức bất kỳ PIN hoặc mật khẩu chữ số nào."),
                ("✋","Khóa Hình Vẽ","Quên hình vẽ? Dr.Fone vượt qua hoàn toàn trong 3 phút."),
                ("🔐","Google FRP","Khóa FRP sau reset nhà máy? Được xóa cho Samsung, Xiaomi, Huawei và nhiều hơn."),
                ("💾","Không Mất Dữ Liệu","Ảnh, danh bạ và ứng dụng được giữ nguyên trên các thiết bị Samsung được hỗ trợ.")]
    },
    "th": {
        "lang":"th","title":f"ปลดล็อกหน้าจอ Android — Dr.Fone ({YEAR})",
        "desc":"ลืม PIN รูปแบบ หรือรหัสผ่าน Android? Dr.Fone ปลดล็อกหน้าจอ Android ใดๆ ในไม่กี่นาที ไม่สูญเสียข้อมูลบน Samsung",
        "kw":"ปลดล็อก android, หน้าจอ android ถูกล็อก, ลืม pin android, bypass android lock, samsung ปลดล็อก, frp bypass",
        "h1":"ปลดล็อกหน้าจอ Android ที่ถูกล็อก",
        "p":"ลืม PIN รูปแบบ หรือรหัสผ่าน? Dr.Fone ลบการล็อกหน้าจอ Android ใดๆ ในไม่กี่นาที — ไม่สูญเสียข้อมูลบน Samsung",
        "feat":[("🔢","PIN และรหัสผ่าน","ลบ PIN หรือรหัสผ่านตัวอักษรและตัวเลขใดๆ ทันที"),
                ("✋","ล็อกรูปแบบ","ลืมรูปแบบ? Dr.Fone ข้ามได้อย่างสมบูรณ์ใน 3 นาที"),
                ("🔐","Google FRP","ล็อก FRP หลังรีเซ็ตโรงงาน? ถูกลบสำหรับ Samsung, Xiaomi, Huawei และอื่นๆ"),
                ("💾","ไม่สูญเสียข้อมูล","รูปภาพ รายชื่อ และแอปยังคงสมบูรณ์บนอุปกรณ์ Samsung ที่รองรับ")]
    },
}

def build_lang_page(code, data):
    feats = ""
    for icon, title, desc in data["feat"]:
        feats += f'<div class="card"><div class="icon">{icon}</div><h3>{title}</h3><p>{desc}</p></div>'
    body = f"""
<div class="hero">
  <h1>{data['h1']}</h1>
  <p>{data['p']}</p>
  {cta("🔓 Download Dr.Fone")}
</div>
<main>
<h2>Features</h2>
<div class="cards">{feats}</div>
<div class="trust-bar">
  <div class="trust-item"><strong>50M+</strong>Users</div>
  <div class="trust-item"><strong>2000+</strong>Devices</div>
  <div class="trust-item"><strong>29+</strong>Brands</div>
  <div class="trust-item"><strong>7-Day</strong>Money-Back</div>
</div>
<div class="cta-box">
  <h2>{data['h1']}</h2>
  <p>{data['p']}</p>
  {cta("🔓 Download Dr.Fone Free")}
</div>
</main>"""
    return page(data["title"], data["desc"], data["kw"], body, lang=data["lang"],
                canonical=f"{SITE_URL}/lang/{code}/")

# ── BRAND PAGES ───────────────────────────────────────────────────────────────
BRANDS = {
    "samsung":{"name":"Samsung","models":"Galaxy S26, S25, S24, S23, Note 20, A52, Z Fold, Z Flip","kw":"samsung locked screen unlock, samsung frp bypass, unlock samsung galaxy"},
    "huawei": {"name":"Huawei","models":"P50, P40, Mate 40, Nova 9, Y Series","kw":"huawei locked screen unlock, huawei frp bypass, unlock huawei phone"},
    "xiaomi": {"name":"Xiaomi / Redmi","models":"Xiaomi 14, 13, Redmi Note 12, POCO X5","kw":"xiaomi locked screen unlock, xiaomi frp bypass, unlock xiaomi phone, redmi unlock"},
    "oppo":   {"name":"OPPO","models":"OPPO Find X6, Reno 10, A96, F21","kw":"oppo locked screen unlock, oppo frp bypass, unlock oppo phone"},
    "vivo":   {"name":"Vivo","models":"Vivo X90, V27, Y76, iQOO 11","kw":"vivo locked screen unlock, vivo frp bypass, unlock vivo phone"},
    "lg":     {"name":"LG","models":"LG V60, G8, Velvet, Stylo 6","kw":"lg locked screen unlock, lg frp bypass, unlock lg phone"},
    "motorola":{"name":"Motorola","models":"Moto G52, Edge 30, One 5G, G Power","kw":"motorola locked screen unlock, motorola frp bypass, unlock motorola phone"},
    "oneplus": {"name":"OnePlus","models":"OnePlus 12, 11, Nord CE 3, 10 Pro","kw":"oneplus locked screen unlock, oneplus frp bypass, unlock oneplus phone"},
}

def build_brand(slug, data):
    body = f"""
<div class="hero">
  <h1>Unlock {data['name']} Locked Screen — Dr.Fone</h1>
  <p>Locked out of your {data['name']} phone? Remove PIN, pattern, password &amp; FRP lock in minutes with Dr.Fone. Supports {data['models']}.</p>
  {cta(f"🔓 Unlock {data['name']} Now")}
</div>
<main>
<h2>Supported {data['name']} Models</h2>
<div class="badge-row">{"".join(f'<span class="badge">{m.strip()}</span>' for m in data["models"].split(","))}</div>
<h2>How to Unlock {data['name']}</h2>
<div class="steps">
  <div class="step"><div class="step-num">1</div><div class="step-body"><h3>Download Dr.Fone</h3><p>Install on Windows or Mac. Select Screen Unlock → Android.</p></div></div>
  <div class="step"><div class="step-num">2</div><div class="step-body"><h3>Connect Your {data['name']} via USB</h3><p>Select {data['name']} as your device brand. Choose the appropriate unlock method.</p></div></div>
  <div class="step"><div class="step-num">3</div><div class="step-body"><h3>Unlock Complete</h3><p>Follow on-screen instructions. Your {data['name']} is unlocked in 2–5 minutes.</p></div></div>
</div>
{cta(f"🔓 Unlock {data['name']} Free Trial")}
</main>"""
    return page(
        f"Unlock {data['name']} Locked Screen — Remove PIN, FRP ({YEAR}) | Dr.Fone",
        f"Locked out of your {data['name']}? Remove PIN, pattern, password &amp; FRP in minutes with Dr.Fone. Supports {data['models']}.",
        data["kw"], body, canonical=f"{SITE_URL}/brands/{slug}/"
    )

# ── SITEMAP ───────────────────────────────────────────────────────────────────
def build_sitemap(urls):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        lines.append(f"  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>")
    lines.append("</urlset>")
    return "\n".join(lines)

# ── ROBOTS.TXT ────────────────────────────────────────────────────────────────
ROBOTS = f"""User-agent: *
Allow: /
Sitemap: {SITE_URL}/sitemap.xml
"""

# ── WRITE ALL FILES ───────────────────────────────────────────────────────────
def write(path, content):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(content, encoding="utf-8")

def main():
    root = BASE
    urls = []

    # Home
    write(root/"index.html", build_home()); urls.append(f"{SITE_URL}/")
    # Core pages
    for slug, fn in [("samsung",build_samsung),("frp",build_frp),("forgot-password",build_forgot),
                     ("no-data-loss",build_no_data_loss),("free-download",build_download),
                     ("pattern",build_pattern),("fingerprint",build_fingerprint),
                     ("vs-competitors",build_vs),("global",build_global)]:
        write(root/slug/"index.html", fn()); urls.append(f"{SITE_URL}/{slug}/")
    # Language pages
    for code, data in LANG_PAGES.items():
        write(root/"lang"/code/"index.html", build_lang_page(code, data))
        urls.append(f"{SITE_URL}/lang/{code}/")
    # Brand pages
    for slug, data in BRANDS.items():
        write(root/"brands"/slug/"index.html", build_brand(slug, data))
        urls.append(f"{SITE_URL}/brands/{slug}/")
    # Sitemap & robots
    write(root/"sitemap.xml", build_sitemap(urls))
    write(root/"robots.txt", ROBOTS)

    total = len(list(root.rglob("*.html"))) + 2
    print(f"✅ Built {total} files across {len(urls)} pages")
    print(f"   Languages: {len(LANG_PAGES)}")
    print(f"   Brands: {len(BRANDS)}")
    print(f"   Core pages: 9")

if __name__ == "__main__":
    main()
