import re
def _n(t): return [float(x.replace(',','')) for x in re.findall(r'\d[\d,]*\.?\d*', t)]
def r(x): return f"{x:,.2f}"
def calculate(q):
    t=q.lower(); n=_n(t)
    if 'compound interest' in t and len(n)>=3:
        p,rt,y=n[:3]; a=p*(1+rt/100)**y
        return f"Compound Interest\nGiven: P={r(p)}, R={rt:g}%, T={y:g} years\nFormula: A = P(1+R/100)^T\nA = {r(p)} x (1+{rt:g}/100)^{y:g} = {r(a)}\nCI = A - P = {r(a-p)}\nAssumes yearly compounding."
    if 'simple interest' in t and len(n)>=3:
        p,rt,y=n[:3]; i=p*rt*y/100
        return f"Simple Interest\nGiven: P={r(p)}, R={rt:g}%, T={y:g} years\nFormula: SI = P x R x T / 100\nSI = {r(p)} x {rt:g} x {y:g} / 100 = {r(i)}\nTotal amount = {r(p+i)}"
    if 'current ratio' in t and len(n)>=2:
        a,l=n[:2]
        if l==0: return "Current liabilities cannot be zero."
        return f"Current Ratio\nGiven: Current Assets={r(a)}, Current Liabilities={r(l)}\nFormula: Current Assets / Current Liabilities\n= {r(a)} / {r(l)} = {a/l:.2f} : 1\nA ratio of about 2:1 is traditionally seen as comfortable."
    if 'gross profit' in t and len(n)>=2 and n[0]:
        s,c=n[:2]; g=s-c
        return f"Gross Profit\nGiven: Net Sales={r(s)}, Cost of Goods Sold={r(c)}\nFormula: Gross Profit = Sales - COGS\n= {r(s)} - {r(c)} = {r(g)}\nGross Profit % = {g/s*100:.2f}% of sales"
    if 'break' in t and 'even' in t and len(n)>=3:
        f,p,v=n[:3]
        if p<=v: return "Selling price must be higher than variable cost per unit."
        return f"Break-even Point\nGiven: Fixed Cost={r(f)}, Price/unit={r(p)}, Variable Cost/unit={r(v)}\nFormula: BEP (units) = Fixed Cost / (Price - Variable Cost)\n= {r(f)} / ({r(p)} - {r(v)}) = {f/(p-v):.2f} units\nBEP (sales) = {r(f/(p-v)*p)}"
    if 'elasticity' in t and len(n)>=4 and n[0] and n[2] and n[1]!=n[0]:
        p1,p2,q1,q2=n[:4]; e=((q2-q1)/q1)/((p2-p1)/p1)
        return f"Price Elasticity of Demand (percentage method)\nGiven: P1={p1:g}, P2={p2:g}, Q1={q1:g}, Q2={q2:g}\nFormula: Ed = (% change in Q) / (% change in P)\n= ({(q2-q1)/q1*100:.2f}%) / ({(p2-p1)/p1*100:.2f}%) = {e:.2f}\n|Ed| = {abs(e):.2f}: demand is {'elastic' if abs(e)>1 else 'unitary' if abs(e)==1 else 'inelastic'}."
    if 'depreciation' in t and len(n)>=3 and ('straight' in t or 'slm' in t) and n[2]:
        c,s,y=n[:3]; d=(c-s)/y
        return f"Straight Line Depreciation\nGiven: Cost={r(c)}, Scrap Value={r(s)}, Life={y:g} years\nFormula: (Cost - Scrap) / Life\n= ({r(c)} - {r(s)}) / {y:g} = {r(d)} per year"
    return None
