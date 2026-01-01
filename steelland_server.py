#!/usr/bin/env python3
"""
steelland_server_full.py
Full combined server: medium-detailed pages (Option B), embedded SVG flag/emblem,
Join form saved to applications.json, and password-protected advanced admin dashboard.

Run:
    python3 steelland_server_full.py
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json, os, datetime, http.cookies, io, csv, uuid

HOST = "localhost"
PORT = 9000
DATA_FILE = "applications.json"

# Admin credentials
ADMIN_USER = "admin"
ADMIN_PASS = "haniel@"
SESSION_COOKIE = "steelland_admin_sess"

# Ensure data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=2)

# -------------------------
# INDEX HTML (site with medium-detailed pages)
# -------------------------
INDEX_HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Steelland — Republic of Craft & Innovation</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  *{box-sizing:border-box}
  body{margin:0;font-family:Inter,system-ui,Arial,sans-serif;background:#07121a;color:#e8f8ff;}
  header{padding:28px;text-align:center;background:linear-gradient(135deg,#0b4460,#082b3a);box-shadow:0 6px 30px rgba(0,120,200,.06)}
  .brand{font-size:34px;font-weight:800}
  .subtitle{opacity:.85;margin-top:6px}
  nav#top{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;padding:12px;background:rgba(2,12,18,.45);position:sticky;top:96px;z-index:49}
  nav#top a{color:#cfeefc;text-decoration:none;padding:8px 12px;border-radius:10px;font-weight:600;cursor:pointer}
  nav#top a.active{background:rgba(10,120,180,.12);color:#fff}
  main{max-width:1100px;margin:24px auto;padding:18px}
  section{display:none;animation:fadeIn .28s both}
  section.active{display:block}
  @keyframes fadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
  .card{background:linear-gradient(180deg,rgba(6,12,16,.65),rgba(6,12,16,.55));padding:18px;border-radius:12px;box-shadow:0 8px 40px rgba(0,120,220,.04);margin-bottom:18px}
  h2{color:#8ee6ff;margin:6px 0 12px}
  p,li{color:#dff6ff;line-height:1.6}
  .flag,.emblem{display:block;margin:18px auto;max-width:92%}
  label{display:block;margin:8px 0 6px;font-weight:700}
  input,textarea,select{width:100%;padding:10px;border-radius:8px;border:none;background:#07202a;color:#e7fbff}
  button.btn{margin-top:12px;padding:10px 16px;border-radius:8px;border:none;background:linear-gradient(90deg,#0090ff,#00e4ff);color:#001;font-weight:800;cursor:pointer}
  footer{text-align:center;padding:18px;color:#8fcfe0;opacity:.9;margin-top:26px}
  .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;margin-top:12px}
  .muted{opacity:.78;color:#a9dff0}
  .small{font-size:13px;color:#cfe}
  nav#quick{position:fixed;bottom:14px;left:50%;transform:translateX(-50%);z-index:50}
  nav#quick a{margin:4px;padding:8px 10px;background:#0b3d52;color:#dff;text-decoration:none;border-radius:6px}
</style>
</head>
<body>
  <header>
    <div class="brand">⚙️ Steelland</div>
    <div class="subtitle">Forged to Endure — Republic of Craft & Innovation</div>
  </header>

  <nav id="top">
    <a onclick="show('home')" id="link-home">Home</a>
    <a onclick="show('history')" id="link-history">History</a>
    <a onclick="show('government')" id="link-government">Government</a>
    <a onclick="show('economy')" id="link-economy">Economy</a>
    <a onclick="show('military')" id="link-military">Military</a>
    <a onclick="show('culture')" id="link-culture">Culture</a>
    <a onclick="show('language')" id="link-language">Language</a>
    <a onclick="show('symbols')" id="link-symbols">National Symbols</a>
    <a onclick="show('holidays')" id="link-holidays">Holidays</a>
    <a onclick="show('geography')" id="link-geography">Geography</a>
    <a onclick="show('cities')" id="link-cities">Cities</a>
    <a onclick="show('currency')" id="link-currency">Currency</a>
    <a onclick="show('transport')" id="link-transport">Transport</a>
    <a onclick="show('technology')" id="link-technology">Technology</a>
    <a onclick="show('education')" id="link-education">Education</a>
    <a onclick="show('timeline')" id="link-timeline">Timeline</a>
    <a onclick="show('founders')" id="link-founders">Founders</a>
    <a onclick="show('anthem')" id="link-anthem">Anthem</a>
    <a onclick="show('law')" id="link-law">Law & Order</a>
    <a onclick="show('citizenship')" id="link-citizenship">Citizenship</a>
    <a onclick="show('join')" id="link-join">Join</a>
  </nav>

  <main>
    <!-- HOME -->
    <section id="home" class="active">
      <div class="card">
        <h2>Welcome to Steelland</h2>
        <p class="muted">A nation forged upon precision, innovation and community. Steelland grew from cooperative foundries into a republic where craft, research and civic design guide the common good.</p>
        <!-- embedded SVG flag -->
        <svg class="flag" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3 2" width="420" height="280" role="img" aria-label="Steelland flag">
          <rect width="1" height="2" x="0" fill="#138a3a"/>
          <rect width="1" height="2" x="1" fill="#ffffff"/>
          <rect width="1" height="2" x="2" fill="#1565c0"/>
        </svg>

        <!-- embedded SVG emblem -->
        <svg class="emblem" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="260" height="260" role="img" aria-label="Steelland emblem">
          <defs><linearGradient id="g1" x1="0" x2="1"><stop offset="0" stop-color="#4e5457"/><stop offset="1" stop-color="#bfc6c9"/></linearGradient></defs>
          <path d="M10,10 L90,10 L80,75 L50,95 L20,75 Z" fill="url(#g1)" stroke="#222"/>
          <circle cx="50" cy="40" r="20" fill="#0b2030"/>
          <circle cx="50" cy="40" r="14" fill="#0b2030" stroke="#bbb"/>
          <polygon points="50,22 52,28 59,28 53,32 55,38 50,34 45,38 47,32 41,28 48,28" fill="#d4af37"/>
        </svg>

        <p>Explore the sections to learn about Steelland's history, government, economy, culture and how to join. The Join form will save applications to the server for review by the Council.</p>
      </div>
    </section>

    <!-- HISTORY (medium detail) -->
    <section id="history">
      <div class="card">
        <h2>History of Steelland</h2>
        <p>Steelland began as a ring of independent foundries and small craft towns clustered near rich ore deposits. Over time, the trades recognized the value of shared standards and cooperative infrastructure: rail links, canalways, and a common apprenticeship code. The Covenant of Anvils formalized this cooperation and set the early rules for trade and technical standards.</p>
        <p>Industrial advances, including alloy breakthroughs and mechanized foundry techniques, accelerated urbanization and research institutions. The modern era is characterized by public research partnerships, vocational education systems, and policies that balance industrial capacity with environmental stewardship.</p>
      </div>
    </section>

    <!-- GOVERNMENT -->
    <section id="government">
      <div class="card">
        <h2>Government</h2>
        <p>Steelland is a Technocratic Republic governed by the Council of Builders — professionals selected by regional guilds and civic districts. The Assembly of Guilds advises and reviews legislation, while the High Court of Craft handles technical and standards disputes. Ministries focus on infrastructure, research funding, civil welfare and external relations.</p>
        <p>Decision-making emphasizes evidence, long-term planning and public consultation. Transparency is supported by published technical reports and open workshops where citizens can inspect projects and standards documents.</p>
      </div>
    </section>

    <!-- ECONOMY -->
    <section id="economy">
      <div class="card">
        <h2>Economy</h2>
        <p>Key sectors include metallurgy, precision manufacturing, robotics and energy systems. Guild cooperatives partner with public research institutes to commercialize innovations and maintain quality standards. Apprenticeship pipelines and technical academies ensure a steady supply of skilled workers.</p>
        <p>Exports center on engineered alloys, industrial tooling, automation components and infrastructure design. Fiscal policy prioritizes infrastructure investment and R&D over speculative finance.</p>
      </div>
    </section>

    <!-- MILITARY -->
    <section id="military">
      <div class="card">
        <h2>Military</h2>
        <p>The Steel Guard emphasizes defense, resilience and civil engineering support. Units specialize in infrastructure protection, rapid repair, humanitarian engineering and cyber defense for industrial control systems. Training focuses on logistics, safety and civilian protection rather than power projection.</p>
        <p>The Guard coordinates with civil agencies for disaster response, maintaining redundancy in critical systems such as power, water and transport corridors.</p>
      </div>
    </section>

    <!-- CULTURE -->
    <section id="culture">
      <div class="card">
        <h2>Culture & Traditions</h2>
        <p>Steelland celebrates craftsmanship: public workshops, the Forging Festival and apprenticeship ceremonies are central to civic life. Folk traditions blend utilitarian art and industrial aesthetics — metalwork exhibitions coexist with public music rooted in workshop rhythms.</p>
        <p>Community projects and joint-build events foster social cohesion; education emphasizes making, repair and collaborative problem-solving.</p>
      </div>
    </section>

    <!-- LANGUAGE -->
    <section id="language">
      <div class="card">
        <h2>Language</h2>
        <p>The official standard is Steelen — a constructed register optimized for clarity in technical and legal contexts. It simplifies grammar and provides precise engineering terms for unambiguous documentation. Citizens are often multilingual for trade and diplomacy.</p>
        <p>Steelen complements local dialects and trade tongues used in border regions and export markets.</p>
      </div>
    </section>

    <!-- SYMBOLS -->
    <section id="symbols">
      <div class="card">
        <h2>National Symbols</h2>
        <p>The flag's vertical tricolor (green, white, blue) represents renewal, unity and knowledge. The emblem blends a shield and gear motif to represent protective craftsmanship and communal honor. Coins and notes use motifs of forges, gears and bridges to celebrate builders.</p>
        <p>The national motto, <em>Forged to Endure</em>, is displayed at civic ceremonies and on public buildings.</p>
      </div>
    </section>

    <!-- HOLIDAYS -->
    <section id="holidays">
      <div class="card">
        <h2>Holidays</h2>
        <p>Major holidays include Founders' Day (commemorating the Covenant of Anvils), the Forging Festival (public exhibitions and apprentice graduations) and Day of Endeavor (awards for civic projects). Public calendars blend work cycles with celebration to preserve craft traditions.</p>
        <p>Community workshops organize open days and competitions on festival weekends to showcase innovation and training.</p>
      </div>
    </section>

    <!-- GEOGRAPHY -->
    <section id="geography">
      <div class="card">
        <h2>Geography</h2>
        <p>Steelland spans mountain ranges rich in ore, river valleys used for mills and coastal ports for trade. Urban planning emphasizes transit corridors, green belts and protected extraction zones to balance production and environment. Terrain shapes settlement: foundry towns cluster near ore veins while research campuses occupy plateau regions.</p>
      </div>
    </section>

    <!-- CITIES -->
    <section id="cities">
      <div class="card">
        <h2>Cities</h2>
        <p>The capital Forgehaven hosts government and major research institutes. Rivermark is known for river logistics and mills; Ironport is the export hub with shipyards and heavy fabrication. Each city integrates manufacturing, public research, housing and cultural spaces to minimize commute and improve quality of life.</p>
      </div>
    </section>

    <!-- CURRENCY -->
    <section id="currency">
      <div class="card">
        <h2>Currency — The Steelon</h2>
        <p>The Steelon supports national trade and is designed with strong anti-counterfeit features (micro-etches, holographic seals and polymer threads). Coins use durable lightweight alloy with civic motifs. Monetary policy funds infrastructure and apprenticeship programs.</p>
      </div>
    </section>

    <!-- TRANSPORT -->
    <section id="transport">
      <div class="card">
        <h2>Transport</h2>
        <p>Steelland's transport network centers on reliable rail corridors, electric trams and engineered canals. A layered logistics network prioritizes maintenance schedules, redundancy and cargo throughput to keep industry moving even in disruption.</p>
      </div>
    </section>

    <!-- TECHNOLOGY -->
    <section id="technology">
      <div class="card">
        <h2>Technology</h2>
        <p>Investments focus on sustainable metallurgy, automation, smart grids and industrial cyber security. Public-private research prototypes priority projects that reduce emissions, increase material efficiency and extend product lifetimes.</p>
      </div>
    </section>

    <!-- EDUCATION -->
    <section id="education">
      <div class="card">
        <h2>Education</h2>
        <p>Education emphasizes apprenticeship, vocational schools and technical academies. Research universities focus on applied engineering and collaborative industry partnerships. Scholarships support broad participation and lifetime learning for workforce mobility.</p>
      </div>
    </section>

    <!-- TIMELINE -->
    <section id="timeline">
      <div class="card">
        <h2>Timeline</h2>
        <ol>
          <li>Year 0 — Covenant of Anvils: Foundries unite</li>
          <li>Year 27 — National rail network inaugurated</li>
          <li>Year 58 — Materials Revolution (advanced alloys)</li>
          <li>Year 72 — Energy independence</li>
          <li>Year 100 — Modern governance & research era</li>
        </ol>
      </div>
    </section>

    <!-- FOUNDERS -->
    <section id="founders">
      <div class="card">
        <h2>Founders</h2>
        <p>Key founding figures were master-builders, metallurgists and civic architects who formed the first guild councils. Their charters emphasized quality, mutual aid and public standards, which remain cornerstones of Steelland's institutions.</p>
      </div>
    </section>

    <!-- ANTHEM -->
    <section id="anthem">
      <div class="card">
        <h2>National Anthem</h2>
        <p>The anthem, a stirring march honoring labor and shared endeavor, is performed at civic ceremonies and Founders' Day. Music blends brass and percussion to evoke steady progress and communal rhythm.</p>
      </div>
    </section>

    <!-- LAW & ORDER -->
    <section id="law">
      <div class="card">
        <h2>Law & Order</h2>
        <p>Legal systems focus on engineering safety, labor protections and transparent governance. The High Court of Craft resolves disputes involving technical standards, patents and public safety concerns. Laws aim to balance civic liberties with community responsibilities.</p>
      </div>
    </section>

    <!-- CITIZENSHIP -->
    <section id="citizenship">
      <div class="card">
        <h2>Citizenship Requirements</h2>
        <p>Applicants must demonstrate commitment to community, a skill or planned contribution, acceptable conduct and adherence to civic values. Panels of guild representatives and civic officers review applications for fit and contribution potential.</p>
      </div>
    </section>

    <!-- JOIN (form) -->
    <section id="join">
      <div class="card">
        <h2>Join Steelland — Application</h2>
        <p class="muted">Applications are reviewed by the Council of Builders. Provide accurate information — motivation and skills strongly influence review.</p>

        <form id="joinForm">
          <div class="grid">
            <div>
              <label>Full Name</label><input name="name" id="name" required placeholder="Full legal name">
            </div>
            <div>
              <label>Age</label><input name="age" id="age" type="number" min="10" required>
            </div>
            <div>
              <label>Email</label><input name="email" id="email" type="email" required placeholder="name@example.com">
            </div>
            <div>
              <label>Country / Region</label><input name="country" id="country" placeholder="Country or region">
            </div>
          </div>

          <label>Occupation / Skill</label><input name="skill" id="skill" placeholder="Engineer, Researcher, Artisan, etc.">

          <div class="grid">
            <div>
              <label>Years of Experience</label><input name="experience" id="experience" type="number" min="0">
            </div>
            <div>
              <label>Languages</label><input name="languages" id="languages" placeholder="English, Steelen, ...">
            </div>
          </div>

          <label>Motivation — Why do you want to join?</label>
          <textarea name="motivation" id="motivation" rows="5" required></textarea>

          <label style="margin-top:10px;"><input type="checkbox" name="oath" id="oath" value="yes" required> I accept Steelland's values and civic responsibilities.</label>

          <div style="text-align:center; margin-top:14px;">
            <button class="btn" type="button" onclick="submitApplication()">Submit Application</button>
          </div>
        </form>

        <div id="joinResult" style="display:none; margin-top:12px; padding:12px; background:#063527; border-radius:8px;">
          ✅ Application submitted — thank you. The Council will review your submission.
        </div>
      </div>
    </section>

  </main>

  <footer>© Steelland — Forged in Code & Craft</footer>

  <nav id="quick">
    <a href="/admin-login">Admin</a>
  </nav>

<script>
// Navigation & state
function show(id){
  document.querySelectorAll("main section").forEach(s=>s.classList.remove("active"));
  var el = document.getElementById(id);
  if(!el) el = document.getElementById("home");
  el.classList.add("active");
  document.querySelectorAll("nav#top a").forEach(a=>a.classList.remove("active"));
  var link = document.getElementById("link-" + id);
  if(link) link.classList.add("active");
  history.replaceState(null,"","#"+id);
  window.scrollTo(0,0);
}
window.addEventListener("load", ()=> {
  var h = location.hash ? location.hash.replace("#","") : "home";
  show(h);
});

// Submit application via JSON to /apply
async function submitApplication(){
  var f = document.getElementById("joinForm");
  var data = {};
  new FormData(f).forEach((v,k)=> data[k]=v);
  data.oath = !!data.oath;
  if(!data.name || !data.age || !data.email || !data.motivation){
    alert("Please fill required fields: name, age, email, motivation.");
    return;
  }
  try {
    let res = await fetch("/apply", {
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body: JSON.stringify(data)
    });
    if(res.ok){
      f.style.display="none";
      document.getElementById("joinResult").style.display="block";
    } else {
      let txt = await res.text();
      alert("Server error: " + txt);
    }
  } catch(e){
    alert("Network error: " + e);
  }
}
</script>
</body>
</html>
"""

# -------------------------
# Admin dashboard HTML (advanced, with Chart.js)
# -------------------------
ADMIN_HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Steelland Admin Dashboard</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/simpledotcss@1.1.0/simple.min.css">
<style>
body{background:#07121a;color:#e8f8ff}
.container{max-width:1100px;margin:18px auto}
.header{display:flex;align-items:center;justify-content:space-between}
.controls{display:flex;gap:8px;align-items:center}
.card{background:#0b1620;padding:14px;border-radius:8px;margin-bottom:12px}
.table{width:100%;border-collapse:collapse}
.table th,.table td{padding:8px;border:1px solid #123;background:rgba(255,255,255,0.02)}
.button{background:#0b8dd3;color:#001;padding:8px 10px;border-radius:6px;border:none}
.small{font-size:13px;color:#9fd8ec}
.badge{background:#0b8dd3;color:#001;padding:6px 8px;border-radius:6px;font-weight:700}
.input{padding:8px;border-radius:6px;border:1px solid #234;background:#06141a;color:#eaf}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div>
      <h2>Steelland — Admin Dashboard</h2>
      <div class="small">Logged in as <strong>admin</strong></div>
    </div>
    <div class="controls">
      <button class="button" id="exportBtn">Export CSV</button>
      <button class="button" id="refreshBtn">Refresh</button>
      <a class="button" href="/admin-logout">Logout</a>
    </div>
  </div>

  <div class="card" style="display:flex;gap:18px;flex-wrap:wrap">
    <div style="flex:1;min-width:180px">
      <div class="small">Total applications</div>
      <div id="statTotal" class="badge">0</div>
    </div>
    <div style="flex:1;min-width:180px">
      <div class="small">Average age</div>
      <div id="statAvgAge" class="badge">—</div>
    </div>
    <div style="flex:1;min-width:180px">
      <div class="small">Most common skill</div>
      <div id="statTopSkill" class="badge">—</div>
    </div>
    <div style="flex:1;min-width:180px">
      <div class="small">Approved</div>
      <div id="statApproved" class="badge">0</div>
    </div>
  </div>

  <div class="card">
    <h3>Applications</h3>
    <div style="display:flex;gap:8px;align-items:center;margin-bottom:8px">
      <input id="searchInput" class="input" placeholder="Search name / email / skill" style="flex:1">
      <select id="filterSkill" class="input" style="width:220px">
        <option value="">-- filter by skill --</option>
      </select>
      <select id="filterStatus" class="input" style="width:160px">
        <option value="">-- status --</option>
        <option value="pending">pending</option>
        <option value="approved">approved</option>
        <option value="rejected">rejected</option>
      </select>
      <button id="clearFilters" class="button">Clear</button>
    </div>

    <table class="table" id="appsTable">
      <thead><tr><th>#</th><th>Name</th><th>Age</th><th>Email</th><th>Skill</th><th>Submitted</th><th>Status</th><th>Actions</th></tr></thead>
      <tbody id="appsBody"></tbody>
    </table>
  </div>

  <div class="card">
    <h3>Charts</h3>
    <div style="display:flex;gap:18px;flex-wrap:wrap">
      <div style="flex:1;min-width:300px">
        <canvas id="chartDaily" height="160"></canvas>
      </div>
      <div style="flex:1;min-width:300px">
        <canvas id="chartSkills" height="160"></canvas>
      </div>
    </div>
  </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
let apps = [];
let chartDaily=null, chartSkills=null;

// Utilities
function escapeHtml(s){ if(!s) return ''; return s.replace(/&/g,'&amp;').replace(/</g,'&lt;'); }

async function loadApps(){
  const res = await fetch('/api/apps');
  if(!res.ok){ alert('Unauthorized or server error'); return; }
  apps = await res.json();
  renderFilters();
  renderTable(apps);
  renderStats(apps);
  loadCharts();
}

function renderFilters(){
  const skillSet = new Set();
  apps.forEach(a=>{ if(a.skill) skillSet.add(a.skill); });
  const sel = document.getElementById('filterSkill');
  sel.innerHTML = '<option value="">-- filter by skill --</option>';
  Array.from(skillSet).sort().forEach(s=>{
    const o=document.createElement('option'); o.value=s; o.textContent=s; sel.appendChild(o);
  });
}

function renderTable(list){
  const tbody = document.getElementById('appsBody'); tbody.innerHTML='';
  list.forEach((a,i)=>{
    const tr=document.createElement('tr');
    tr.innerHTML = `<td>${i+1}</td>
      <td>${escapeHtml(a.name||'')}</td>
      <td>${a.age||''}</td>
      <td>${escapeHtml(a.email||'')}</td>
      <td>${escapeHtml(a.skill||'')}</td>
      <td>${a.submitted_at||''}</td>
      <td>${a.status||'pending'}</td>
      <td>
        <button onclick="updateStatus('${a.id}','approved')">Approve</button>
        <button onclick="updateStatus('${a.id}','rejected')">Reject</button>
        <button onclick="deleteApp('${a.id}')">Delete</button>
      </td>`;
    tbody.appendChild(tr);
  });
}

function renderStats(list){
  document.getElementById('statTotal').textContent = list.length;
  const ages = list.map(a=>parseFloat(a.age)).filter(n=>!isNaN(n));
  document.getElementById('statAvgAge').textContent = ages.length? (ages.reduce((s,n)=>s+n,0)/ages.length).toFixed(1) : '—';
  const approved = list.filter(a=>a.status==='approved').length;
  document.getElementById('statApproved').textContent = approved;
  const skillCount={};
  list.forEach(a=>{ if(a.skill){ skillCount[a.skill]=(skillCount[a.skill]||0)+1; }});
  let top='—', topc=0;
  Object.keys(skillCount).forEach(k=>{ if(skillCount[k]>topc){ top=k; topc=skillCount[k]; }});
  document.getElementById('statTopSkill').textContent = top;
}

async function loadCharts(){
  const res = await fetch('/api/stats');
  if(!res.ok) return;
  const data = await res.json();
  const ctx = document.getElementById('chartDaily').getContext('2d');
  if(chartDaily) chartDaily.destroy();
  chartDaily = new Chart(ctx,{ type:'line', data:{ labels:data.daily.labels, datasets:[{label:'Applications/day', data:data.daily.counts, fill:true}] } });
  const ctx2 = document.getElementById('chartSkills').getContext('2d');
  if(chartSkills) chartSkills.destroy();
  chartSkills = new Chart(ctx2,{ type:'bar', data:{ labels:data.skills.labels, datasets:[{label:'By skill', data:data.skills.counts}] }, options:{indexAxis:'y'} });
}

async function updateStatus(id,status){
  const res = await fetch('/api/update',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id,status})});
  if(res.ok) loadApps(); else alert('Update failed');
}

async function deleteApp(id){
  if(!confirm('Delete application?')) return;
  const res = await fetch('/api/delete',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id})});
  if(res.ok) loadApps(); else alert('Delete failed');
}

document.getElementById('refreshBtn').addEventListener('click', ()=> loadApps());
document.getElementById('exportBtn').addEventListener('click', ()=> window.location='/api/export');
document.getElementById('searchInput').addEventListener('input',(e)=>{
  const q=e.target.value.toLowerCase();
  const fSkill=document.getElementById('filterSkill').value;
  const fStatus=document.getElementById('filterStatus').value;
  const filtered = apps.filter(a=>{
    if(fSkill && a.skill!==fSkill) return false;
    if(fStatus && (a.status||'pending')!==fStatus) return false;
    return !q || ((a.name||'').toLowerCase().includes(q) || (a.email||'').toLowerCase().includes(q) || (a.skill||'').toLowerCase().includes(q));
  });
  renderTable(filtered);
});
document.getElementById('filterSkill').addEventListener('change', ()=> document.getElementById('searchInput').dispatchEvent(new Event('input')));
document.getElementById('filterStatus').addEventListener('change', ()=> document.getElementById('searchInput').dispatchEvent(new Event('input')));
document.getElementById('clearFilters').addEventListener('click', ()=>{ document.getElementById('searchInput').value=''; document.getElementById('filterSkill').value=''; document.getElementById('filterStatus').value=''; renderTable(apps); });

// Initial load
loadApps();
</script>
</body>
</html>
"""

# -------------------------
# Helper functions for loading/saving apps
# -------------------------
def load_apps():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            arr = json.load(f)
    except Exception:
        arr = []
    changed = False
    for a in arr:
        if 'id' not in a:
            a['id'] = str(uuid.uuid4())
            changed = True
        if 'status' not in a:
            a['status'] = 'pending'
            changed = True
        if 'submitted_at' not in a:
            a['submitted_at'] = datetime.datetime.utcnow().isoformat() + "Z"
            changed = True
    if changed:
        save_apps(arr)
    return arr

def save_apps(arr):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(arr, f, ensure_ascii=False, indent=2)

# compute stats for charts
def compute_stats(apps):
    counts_by_day = {}
    for a in apps:
        ts = a.get('submitted_at','')
        day = ts.split("T")[0] if "T" in ts else ts
        counts_by_day[day] = counts_by_day.get(day, 0) + 1
    days = sorted(counts_by_day.keys())
    labels = days
    counts = [counts_by_day[d] for d in days]
    skill_counts = {}
    for a in apps:
        s = (a.get('skill') or a.get('occupation') or '').strip()
        if s:
            skill_counts[s] = skill_counts.get(s, 0) + 1
    sk_labels = list(skill_counts.keys())
    sk_counts = [skill_counts[k] for k in sk_labels]
    return {"daily":{"labels":labels,"counts":counts},"skills":{"labels":sk_labels,"counts":sk_counts}}

# -------------------------
# HTTP request handler
# -------------------------
class Handler(BaseHTTPRequestHandler):
    def is_admin(self):
        cookie = self.headers.get("Cookie")
        if not cookie:
            return False
        c = http.cookies.SimpleCookie(cookie)
        val = c.get(SESSION_COOKIE)
        return val and val.value == "yes"

    def send_json(self,obj,code=200):
        self.send_response(code)
        self.send_header("Content-Type","application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(obj).encode("utf-8"))

    def do_GET(self):
        # Serve site
        if self.path in ("/", "/index.html", ""):
            self.send_response(200)
            self.send_header("Content-Type","text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(INDEX_HTML.encode("utf-8"))
            return

        # Admin login page
        if self.path == "/admin-login":
            html = """<!doctype html><html><head><meta charset="utf-8"><title>Admin Login</title></head>
            <body style="font-family:Arial;background:#07121a;color:#e8f8ff;padding:24px">
            <h2>Steelland Admin Login</h2>
            <form id="loginForm">
              <label>Username</label><br><input id="u" name="u"><br>
              <label>Password</label><br><input id="p" name="p" type="password"><br><br>
              <button type="button" onclick="login()">Login</button>
            </form>
            <div id="msg" style="color:#f88"></div>
            <script>
            async function login(){
              const u=document.getElementById('u').value;
              const p=document.getElementById('p').value;
              const res=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({u,p})});
              if(res.ok){ location.href='/admin'; } else { document.getElementById('msg').textContent='Login failed'; }
            }
            </script>
            </body></html>"""
            self.send_response(200)
            self.send_header("Content-Type","text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
            return

        # Admin dashboard (requires login)
        if self.path == "/admin":
            if not self.is_admin():
                self.send_response(302)
                self.send_header("Location","/admin-login")
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-Type","text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(ADMIN_HTML.encode("utf-8"))
            return

        # API: apps
        if self.path == "/api/apps":
            if not self.is_admin():
                self.send_json({"error":"unauthorized"},401); return
            apps = load_apps()
            self.send_json(apps)
            return

        # API: stats
        if self.path == "/api/stats":
            if not self.is_admin():
                self.send_json({"error":"unauthorized"},401); return
            apps = load_apps()
            stats = compute_stats(apps)
            self.send_json(stats)
            return

        # Export CSV
        if self.path == "/api/export":
            if not self.is_admin():
                self.send_response(401); self.end_headers(); return
            apps = load_apps()
            out = io.StringIO()
            writer = csv.writer(out)
            headers = ["id","name","age","email","country","skill","occupation","experience","languages","status","submitted_at","motivation"]
            writer.writerow(headers)
            for a in apps:
                writer.writerow([a.get(h,"") for h in headers])
            csv_bytes = out.getvalue().encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type","text/csv; charset=utf-8")
            self.send_header("Content-Disposition","attachment; filename=applications.csv")
            self.send_header("Content-Length", str(len(csv_bytes)))
            self.end_headers()
            self.wfile.write(csv_bytes)
            return

        # Logout
        if self.path == "/admin-logout":
            self.send_response(302)
            self.send_header("Set-Cookie", f"{SESSION_COOKIE}=no; Path=/; Max-Age=0")
            self.send_header("Location","/")
            self.end_headers()
            return

        # fallback -> redirect to root
        self.send_response(302)
        self.send_header("Location","/")
        self.end_headers()

    def do_POST(self):
        # API login
        if self.path == "/api/login":
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length).decode('utf-8') if length else ''
            try:
                data = json.loads(raw)
            except Exception:
                data = {}
            u = data.get("u","")
            p = data.get("p","")
            if u == ADMIN_USER and p == ADMIN_PASS:
                self.send_response(200)
                # set session cookie
                self.send_header("Set-Cookie", f"{SESSION_COOKIE}=yes; Path=/")
                self.end_headers()
                self.wfile.write(b'{"status":"ok"}')
                return
            else:
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b'{"error":"invalid"}')
                return

        # Update status (approve/reject)
        if self.path == "/api/update":
            if not self.is_admin():
                self.send_json({"error":"unauthorized"},401); return
            length = int(self.headers.get("Content-Length",0))
            raw = self.rfile.read(length).decode('utf-8') if length else ''
            data = json.loads(raw) if raw else {}
            id_ = data.get("id"); status = data.get("status")
            apps = load_apps()
            found=False
            for a in apps:
                if a.get("id")==id_:
                    a["status"]=status
                    found=True
                    break
            if found:
                save_apps(apps)
                self.send_json({"status":"ok"})
            else:
                self.send_json({"error":"not found"},404)
            return

        # Delete app
        if self.path == "/api/delete":
            if not self.is_admin():
                self.send_json({"error":"unauthorized"},401); return
            length = int(self.headers.get("Content-Length",0))
            raw = self.rfile.read(length).decode('utf-8') if length else ''
            data = json.loads(raw) if raw else {}
            id_ = data.get("id")
            apps = load_apps()
            new = [a for a in apps if a.get("id")!=id_]
            if len(new)==len(apps):
                self.send_json({"error":"not found"},404); return
            save_apps(new)
            self.send_json({"status":"deleted"})
            return

        # Client apply -> /apply
        if self.path == "/apply":
            length = int(self.headers.get("Content-Length",0))
            raw = self.rfile.read(length).decode('utf-8') if length else ''
            try:
                data = json.loads(raw) if raw else {}
            except Exception:
                data = {}
            apps = load_apps()
            entry = {
                "id": str(uuid.uuid4()),
                "name": (data.get("name") or "").strip(),
                "age": data.get("age",""),
                "email": (data.get("email") or "").strip(),
                "country": (data.get("country") or "").strip(),
                "occupation": (data.get("occupation") or "").strip(),
                "skill": (data.get("skill") or "").strip(),
                "experience": data.get("experience",""),
                "languages": data.get("languages",""),
                "motivation": (data.get("motivation") or "").strip(),
                "status": "pending",
                "submitted_at": datetime.datetime.utcnow().isoformat() + "Z"
            }
            if not entry["name"] or not entry["email"] or not entry["motivation"]:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Name, email and motivation are required")
                return
            apps.append(entry)
            save_apps(apps)
            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status":"ok","id":entry["id"]}).encode("utf-8"))
            return

        # fallback
        self.send_response(404)
        self.end_headers()

# -------------------------
# Run server
# -------------------------
def run():
    server = HTTPServer((HOST, PORT), Handler)
    print(f"🚀 Steelland server running at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        server.server_close()

if __name__ == "__main__":
    run()
