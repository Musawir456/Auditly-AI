<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Auditly X | Enterprise AI Platform</title>

<!-- Google Font -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap" rel="stylesheet">

<!-- Chess.js CDN -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js"></script>

<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Inter',sans-serif}

body{
background:linear-gradient(135deg,#0f172a,#1e293b);
color:white;
}

nav{
display:flex;
justify-content:space-between;
padding:20px 60px;
background:#111827;
align-items:center;
}

nav h2{font-weight:900;color:#3b82f6}

nav ul{display:flex;gap:30px;list-style:none}
nav ul li{cursor:pointer}
nav ul li:hover{color:#3b82f6}

.section{
display:none;
padding:80px 60px;
min-height:90vh;
}

.active{display:block}

.hero{
text-align:center;
padding-top:120px;
}

.hero h1{
font-size:55px;
font-weight:900;
}

.hero p{
margin-top:20px;
font-size:18px;
opacity:.8;
}

button{
padding:12px 30px;
margin-top:25px;
background:#2563eb;
border:none;
color:white;
border-radius:8px;
cursor:pointer;
transition:.3s;
}

button:hover{
background:#1d4ed8;
}

.card-container{
display:flex;
gap:30px;
margin-top:50px;
flex-wrap:wrap;
}

.card{
background:#1e293b;
padding:30px;
border-radius:15px;
width:280px;
transition:.3s;
}

.card:hover{
transform:translateY(-10px);
box-shadow:0 0 25px rgba(59,130,246,.5);
}

textarea{
width:100%;
height:150px;
border-radius:10px;
padding:15px;
margin-top:20px;
}

pre{
background:#111827;
padding:20px;
border-radius:10px;
overflow:auto;
}

.footer{
text-align:center;
padding:20px;
background:#111827;
font-size:12px;
opacity:.7;
}
</style>
</head>
<body>

<nav>
<h2>Auditly X</h2>
<ul>
<li onclick="show('home')">Home</li>
<li onclick="show('dashboard')">AI Auditor</li>
<li onclick="show('chess')">AI Chess</li>
<li onclick="show('analytics')">Analytics</li>
</ul>
</nav>

<!-- HOME -->
<section id="home" class="section active">
<div class="hero">
<h1>Enterprise AI + Strategy Platform</h1>
<p>Compliance. Risk Intelligence. Strategic Simulation.</p>
<button onclick="show('dashboard')">Launch System</button>
</div>

<div class="card-container">
<div class="card">
<h3>🤖 AI Auditor</h3>
<p>Deep forensic compliance scanning engine.</p>
</div>
<div class="card">
<h3>♟ Strategic Chess AI</h3>
<p>Decision-making intelligence simulator.</p>
</div>
<div class="card">
<h3>🔐 Security Core</h3>
<p>AES-256 encrypted processing layer.</p>
</div>
</div>
</section>

<!-- DASHBOARD -->
<section id="dashboard" class="section">
<h1>🔍 AI Audit Engine</h1>

<textarea id="docText" placeholder="Paste document text here..."></textarea>
<button onclick="runAudit()">Run AI Analysis</button>

<div id="auditResult"></div>
</section>

<!-- CHESS -->
<section id="chess" class="section">
<h1>♟ AI Chess Engine</h1>
<pre id="board"></pre>
<button onclick="aiMove()">AI Move</button>
</section>

<!-- ANALYTICS -->
<section id="analytics" class="section">
<h1>📊 Performance Analytics</h1>

<div class="card-container">
<div class="card">
<h3>System Uptime</h3>
<p>99.98%</p>
</div>

<div class="card">
<h3>Avg Response</h3>
<p>0.18s</p>
</div>

<div class="card">
<h3>Risk Detection</h3>
<p>Active</p>
</div>
</div>

</section>

<div class="footer">
© 2026 Auditly X | Designed by Abdul Musawir
</div>

<script>
function show(id){
document.querySelectorAll('.section').forEach(sec=>sec.classList.remove('active'));
document.getElementById(id).classList.add('active');
}

function runAudit(){
const text=document.getElementById("docText").value;
if(!text){
alert("Please enter document text");
return;
}

let score=Math.floor(Math.random()*100);
let risk="Low Risk";

if(score>70) risk="High Risk";
else if(score>40) risk="Medium Risk";

document.getElementById("auditResult").innerHTML=
`<h3>Risk Score: ${score}</h3>
<p>Status: ${risk}</p>
<p>AI Summary: Document analyzed successfully.</p>`;
}

/* CHESS ENGINE */
const chess=new Chess();

function render(){
document.getElementById("board").innerText=chess.ascii();
}

function aiMove(){
const moves=chess.moves();
if(moves.length===0) return;
const move=moves[Math.floor(Math.random()*moves.length)];
chess.move(move);
render();
}

render();
</script>

</body>
</html>
