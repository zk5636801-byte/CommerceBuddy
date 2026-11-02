(()=>{
const $=id=>document.getElementById(id);
const SUBJ=["Mixed Commerce","Economics","Business Studies","Business Law","Accountancy"];
const TIPS=["What is inflation?","Explain demand and supply","What is the accounting equation?","Difference between void and voidable contract","Simple interest on 5000 at 8% for 3 years","Current ratio assets 50000 liabilities 25000","Straight line depreciation cost 100000 scrap 10000 life 5","What is the marketing mix?"];
let subject=SUBJ[0],history=[],last="",muted=false,busy=false,rec=null,recOn=false,heard="",voices=[];
const synth=window.speechSynthesis,SR=window.SpeechRecognition||window.webkitSpeechRecognition;
function state(s,msg){$("orb").className="orb "+s;$("state").textContent=msg}
function micStatus(t,c){const m=$("mic");m.textContent="Mic: "+t;m.className="pill "+(c||"")}
function add(role,text,tag,cls,note){const d=document.createElement("div");d.className="msg "+role;
 if(tag){const t=document.createElement("span");t.className="tag "+(cls||"");t.textContent=tag;d.appendChild(t)}
 d.appendChild(document.createTextNode(text));
 if(note){const n=document.createElement("span");n.className="note";n.textContent=note;d.appendChild(n)}
 $("log").appendChild(d);$("log").scrollTop=$("log").scrollHeight}
async function health(){try{const r=await fetch("/api/health");const j=await r.json();
 $("mode").textContent=j.mode==="online"?"Online AI ("+j.model+")":"Offline Demo";$("mode").className="pill "+(j.mode==="online"?"on":"off")}
 catch(e){$("mode").textContent="Backend not running";$("mode").className="pill err"}}
function loadVoices(){voices=synth?synth.getVoices().filter(v=>/^en/i.test(v.lang)):[];const s=$("voice");s.innerHTML="";
 voices.sort((a,b)=>(/en-IN/i.test(b.lang)?1:0)-(/en-IN/i.test(a.lang)?1:0));
 voices.forEach((v,i)=>{const o=document.createElement("option");o.value=i;o.textContent=v.name+" ("+v.lang+")";s.appendChild(o)});
 if(!voices.length){const o=document.createElement("option");o.textContent="Default voice";s.appendChild(o)}}
function speak(text){if(!synth||muted||!text)return;synth.cancel();
 const u=new SpeechSynthesisUtterance(text.replace(/[|=]/g," "));u.lang="en-IN";u.rate=parseFloat($("rate").value);
 const v=voices[$("voice").value];if(v){u.voice=v;u.lang=v.lang}
 u.onstart=()=>state("speaking","Speaking...");u.onend=()=>state("idle","Ask me another question");u.onerror=()=>state("idle","Ask me another question");synth.speak(u)}
function stopSpeech(){if(synth)synth.cancel();if(!busy)state("idle","Speech stopped")}
async function ask(q){q=q.trim();if(!q||busy)return;
 busy=true;$("send").disabled=true;$("micbtn").disabled=true;if(synth)synth.cancel();
 add("u",q);$("q").value="";state("thinking","Thinking...");
 const ctl=new AbortController(),to=setTimeout(()=>ctl.abort(),35000);
 try{const r=await fetch("/api/chat",{method:"POST",headers:{"Content-Type":"application/json"},signal:ctl.signal,
  body:JSON.stringify({question:q,mode:$("mode2").value,subject,history})});const j=await r.json();
  if(!r.ok){add("a",j.error||"Something went wrong.","Error","err");state("idle","Error. Try again.")}
  else{const lab=j.source==="ai"?"AI answer":j.source==="calculator"?"Calculator":"Offline knowledge base";
   add("a",j.answer,lab,j.source==="offline"?"offline":"",j.note);history.push({role:"user",content:q},{role:"assistant",content:j.answer});history=history.slice(-10);
   last=j.answer;state("idle","Answer ready");speak(j.answer)}}
 catch(e){add("a","Cannot reach the CommerceBuddy backend. Make sure the black start window is still open.","Error","err");state("idle","Backend not reachable")}
 clearTimeout(to);busy=false;$("send").disabled=false;$("micbtn").disabled=false;health()}
function initMic(){if(!SR){micStatus("not supported (use Chrome or Edge)","err");$("micbtn").disabled=true;$("state").textContent="Voice needs Chrome or Edge. Type your question instead.";return}
 rec=new SR();rec.lang="en-IN";rec.interimResults=true;rec.continuous=false;rec.maxAlternatives=1;
 rec.onstart=()=>{recOn=true;heard="";$("micbtn").textContent="Stop";$("micbtn").classList.add("rec");micStatus("listening","on");state("listening","Listening...")};
 rec.onresult=e=>{let t="";for(const r of e.results)t+=r[0].transcript;heard=t;$("q").value=t};
 rec.onerror=e=>{const m={"not-allowed":"Microphone blocked. Click the lock icon in the address bar and allow it.","service-not-allowed":"Microphone blocked.","no-speech":"I heard nothing. Try again.","audio-capture":"No microphone found.","network":"Voice needs internet. Type your question instead."};
  micStatus(e.error==="no-speech"?"ready":"problem","err");state("idle",m[e.error]||"Voice error. Type instead.");heard=""};
 rec.onend=()=>{recOn=false;$("micbtn").textContent="Speak";$("micbtn").classList.remove("rec");if($("mic").className.indexOf("err")<0)micStatus("ready");
  const t=heard.trim();heard="";if(t)ask(t);else if($("orb").classList.contains("listening"))state("idle","Tap the microphone and ask a question")}}
$("micbtn").onclick=()=>{if(!rec||busy)return;if(recOn){rec.stop();return}if(synth)synth.cancel();try{rec.start()}catch(e){}};
$("send").onclick=()=>ask($("q").value);$("q").onkeydown=e=>{if(e.key==="Enter")ask($("q").value)};
$("stop").onclick=stopSpeech;$("pause").onclick=()=>{if(!synth)return;if(synth.paused){synth.resume();$("pause").textContent="Pause"}else{synth.pause();$("pause").textContent="Resume"}};
$("repeat").onclick=()=>{if(last)speak(last)};$("mute").onclick=()=>{muted=!muted;$("mute").textContent=muted?"Unmute":"Mute";if(muted&&synth)synth.cancel()};
$("clear").onclick=()=>{if(confirm("Clear the whole conversation?")){$("log").innerHTML="";history=[];last="";if(synth)synth.cancel();state("idle","Conversation cleared")}};
$("expo").onclick=()=>{document.body.classList.toggle("expo");$("expo").textContent=document.body.classList.contains("expo")?"Exit exhibition mode":"Exhibition mode"};
SUBJ.forEach(s=>{const b=document.createElement("button");b.textContent=s;b.className=s===subject?"sel":"";b.onclick=()=>{subject=s;[...$("subjects").children].forEach(c=>c.classList.toggle("sel",c===b))};$("subjects").appendChild(b)});
TIPS.forEach(t=>{const b=document.createElement("button");b.textContent=t;b.onclick=()=>ask(t);$("tips").appendChild(b)});
if(synth){loadVoices();synth.onvoiceschanged=loadVoices}else{$("voice").disabled=true}
add("a","Hello! I am CommerceBuddy AI. Ask me about Economics, Business Studies, Business Law or Accountancy. Tap Speak or type below.","CommerceBuddy");
initMic();health();setInterval(health,30000);
})();
