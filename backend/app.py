import json, os, sys, time, threading
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import ai_service, calc, knowledge_base
ROOT=Path(__file__).resolve().parent.parent
env=ROOT/".env"
if env.exists():
    for l in env.read_text().splitlines():
        if "=" in l and not l.strip().startswith("#"):
            k,v=l.split("=",1); os.environ.setdefault(k.strip(),v.strip().strip('"'))
ERR={"bad_key":"The API key was rejected. Check ANTHROPIC_API_KEY in .env.","rate_limit":"AI is busy (rate limit). Try again in a minute.","network":"No internet or AI unreachable.","service_error":"AI service error."}
MIME={".html":"text/html",".css":"text/css",".js":"text/javascript"}
hits={}; lock=threading.Lock()
def has_key(): return bool(os.environ.get("ANTHROPIC_API_KEY","").strip()) and os.environ.get("OFFLINE_ONLY")!="1"
def answer(d):
    q=str(d.get("question","")).strip()[:1000]
    if not q: return 400,{"error":"Please type or speak a question."}
    mode=d.get("mode","quick"); subj=str(d.get("subject","Mixed Commerce"))[:40]
    c=calc.calculate(q)
    if c: return 200,{"answer":c,"source":"calculator","note":"Exact arithmetic by the built-in calculator."}
    err="Offline demo mode (no AI connected)."
    if has_key():
        text,st=ai_service.ask(q,d.get("history",[]) if isinstance(d.get("history"),list) else [],mode,subj)
        if text: return 200,{"answer":text,"source":"ai"}
        err=ERR.get(st,"AI unavailable.")
    if q.lower().strip("!. ") in("hi","hello","hey"): return 200,{"answer":"Hello! I am CommerceBuddy AI. Ask me about Economics, Business Studies, Business Law or Accountancy.","source":"offline"}
    k=knowledge_base.lookup(q)
    if k: return 200,{"answer":k[1],"source":"offline","note":err+" Answer from the offline knowledge base."}
    return 200,{"answer":"I have no offline answer for that. Try demand, inflation, GDP, partnership, contract, depreciation, or a sum like 'simple interest on 5000 at 8% for 3 years'. Add an API key to answer any question.","source":"offline","note":err}
class H(BaseHTTPRequestHandler):
    def log_message(self,*a): pass
    def send(self,code,obj=None,raw=None,ct="application/json"):
        b=raw if raw is not None else json.dumps(obj).encode()
        self.send_response(code); self.send_header("Content-Type",ct+"; charset=utf-8"); self.send_header("Content-Length",str(len(b))); self.send_header("Cache-Control","no-store"); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path=="/api/health": return self.send(200,{"ok":True,"mode":"online" if has_key() else "offline","model":os.environ.get("CLAUDE_MODEL","claude-sonnet-5-5")})
        p="index.html" if self.path in("/","") else self.path.lstrip("/").split("?")[0]
        f=(ROOT/"frontend"/p).resolve()
        if (ROOT/"frontend").resolve() in f.parents and f.is_file(): return self.send(200,raw=f.read_bytes(),ct=MIME.get(f.suffix,"text/plain"))
        self.send(404,{"error":"not found"})
    def do_POST(self):
        if self.path!="/api/chat": return self.send(404,{"error":"not found"})
        n=int(self.headers.get("Content-Length",0))
        if n>20000: return self.send(413,{"error":"Request too large."})
        now=time.time(); ip=self.client_address[0]
        with lock:
            hits[ip]=[t for t in hits.get(ip,[]) if now-t<60]+[now]
            if len(hits[ip])>30: return self.send(429,{"error":"Too many questions. Wait a moment."})
        try: d=json.loads(self.rfile.read(n))
        except Exception: return self.send(400,{"error":"Invalid request."})
        code,obj=answer(d if isinstance(d,dict) else {}); self.send(code,obj)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))

    print(
        f"CommerceBuddy running on port {port} "
        f"({'ONLINE AI' if has_key() else 'OFFLINE DEMO'})"
    )

    server = ThreadingHTTPServer(
        ("0.0.0.0", port),
        H
    )

    server.serve_forever()
