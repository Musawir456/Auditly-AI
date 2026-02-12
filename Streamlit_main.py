<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Auditly X Enterprise Platform</title>

<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial}

body{
background:#0f172a;
color:white;
}

nav{
display:flex;
justify-content:space-between;
padding:20px 40px;
background:#111827;
}

nav h2{color:#3b82f6}

nav ul{
display:flex;
gap:20px;
list-style:none;
}

nav ul li{
cursor:pointer;
}

nav ul li:hover{color:#3b82f6}

.section{
display:none;
padding:60px 40px;
}

.active{display:block}

button{
padding:10px 25px;
margin-top:15px;
background:#2563eb;
border:none;
color:white;
border-radius:6px;
cursor:pointer;
}

textarea{
width:100%;
height:150px;
margin-top:20px;
padding:10px;
border-radius:8px;
}

pre{
background:#111827;
padding:20px;
border-radius:10px;
}
</style>
</head>

<body>

<nav>
<h2>Auditly X</h2>
<ul>
<li onclick="showSection('home')">Home</li>
<li onclick="showSection('audit')">AI Auditor</li>
<li onclick="showSection('chess')">Chess</li>
</ul>
</nav>

<!-- HOME -->
<div id="home" class="section active">
<h1>Enterprise AI Platform</h1>
<p>Compliance • Risk • Strategy</p>
<button onclick="showSection('audit')">Launch</button>
</div>

<!-- AUDIT -->
<div id="audit" class="section">
<h2>AI Document Audit</h2>
<textarea id="doc"></textarea>
<button onclick="runAudit()">Run Audit</button>
<div id="result"></div>
</div>

<!-- CHESS -->
<div id="chess" class="section">
<h2>Simple Chess Simulation</h2>
<pre id="board"></pre>
<button onclick="randomMove()">AI Move</button>
</div>

<script>
function showSection(id){
document.querySelectorAll(".section").forEach(s=>s.classList.remove("active"));
document.getElementById(id).classList.add("active");
}

function runAudit(){
let score=Math.floor(Math.random()*100);
let risk="Low";
if(score>70) risk="High";
else if(score>40) risk="Medium";

document.getElementById("result").innerHTML=
"<h3>Risk Score: "+score+"</h3><p>Status: "+risk+"</p>";
}

/* SIMPLE CHESS BOARD (Manual Logic) */
let board = [
["r","n","b","q","k","b","n","r"],
["p","p","p","p","p","p","p","p"],
[".","",".",".",".",".",".","."],
[".","",".",".",".",".",".","."],
[".","",".",".",".",".",".","."],
[".","",".",".",".",".",".","."],
["P","P","P","P","P","P","P","P"],
["R","N","B","Q","K","B","N","R"]
];

function renderBoard(){
let text="";
for(let row of board){
text+=row.join(" ")+"\n";
}
document.getElementById("board").innerText=text;
}

function randomMove(){
let row=Math.floor(Math.random()*8);
let col=Math.floor(Math.random()*8);
board[row][col]="*";
renderBoard();
}

renderBoard();
</script>

</body>
</html>
