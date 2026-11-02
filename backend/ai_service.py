import json, os, urllib.request, urllib.error
SYSTEM="You are CommerceBuddy AI, a friendly Commerce professor for Indian school students. Topics: Economics, Business Studies, Business Law, Accountancy. Answer in simple English only, with Indian examples where useful. Show numerical work step by step (given, formula, substitution, result). Never invent figures, laws or section numbers; say when unsure. State assumptions, or ask for clarification if the question is ambiguous. For law, give general education, not legal advice. Politely redirect non-commerce questions. Use plain text (no markdown tables)."
MODES={"quick":"Reply in at most 3 short sentences.","detailed":"Give a structured explanation: definition, example, key points.","exam":"Format as an exam answer: definition, headings, numbered points."}
def ask(question, history, mode, subject):
    key=os.environ.get("ANTHROPIC_API_KEY","").strip()
    if not key: return None,"no_key"
    msgs=[{"role":m["role"],"content":m["content"]} for m in history[-8:] if isinstance(m,dict) and m.get("role") in("user","assistant") and isinstance(m.get("content"),str)]
    while msgs and msgs[0]["role"]!="user": msgs.pop(0)
    msgs.append({"role":"user","content":question})
    body={"model":os.environ.get("CLAUDE_MODEL","claude-sonnet-5-5"),"max_tokens":int(os.environ.get("MAX_TOKENS","700")),
      "system":SYSTEM+" "+MODES.get(mode,MODES["quick"])+" Subject focus: "+subject+".","messages":msgs}
    req=urllib.request.Request("https://api.anthropic.com/v1/messages",json.dumps(body).encode(),
      {"content-type":"application/json","x-api-key":key,"anthropic-version":"2023-06-01"})
    try:
        with urllib.request.urlopen(req,timeout=25) as r: d=json.load(r)
        return "".join(b.get("text","") for b in d["content"] if b.get("type")=="text") or None,"ok"
    except urllib.error.HTTPError as e: return None,{401:"bad_key",429:"rate_limit"}.get(e.code,"service_error")
    except (urllib.error.URLError,TimeoutError,OSError): return None,"network"
    except Exception: return None,"service_error"
