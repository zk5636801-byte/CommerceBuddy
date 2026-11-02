KB=[
(["demand"],"Economics","Law of Demand: when the price of a good rises, quantity demanded falls, other things remaining constant (ceteris paribus). Example: if tea becomes costlier, people buy less of it. The demand curve slopes downward."),
(["supply"],"Economics","Law of Supply: when price rises, quantity supplied rises, other things constant. Producers earn more per unit, so they offer more. The supply curve slopes upward."),
(["inflation"],"Economics","Inflation is a sustained rise in the general price level, so each rupee buys less. In India it is measured by the Consumer Price Index (CPI). The RBI controls it mainly through the repo rate."),
(["gdp"],"Economics","GDP (Gross Domestic Product) is the total market value of all final goods and services produced within a country in a year. Expenditure method: GDP = C + I + G + (X - M)."),
(["fiscal"],"Economics","Fiscal policy is the government's use of taxes and spending to influence the economy. Monetary policy, by contrast, is run by the central bank (RBI)."),
(["monetary","repo"],"Economics","Monetary policy is the RBI's control of money supply and interest rates. Tools: repo rate, reverse repo, CRR, SLR and open market operations."),
(["management"],"Business Studies","Management is the process of planning, organising, staffing, directing and controlling resources to achieve goals effectively and efficiently. Fayol's 14 principles are a classic guide."),
(["marketing mix"],"Business Studies","The marketing mix is the 4 Ps: Product, Price, Place and Promotion. Example: a phone company decides its features, cost, shops and advertisements."),
(["partnership"],"Business Law","A partnership is a relationship between persons who agree to share the profits of a business carried on by all or any of them acting for all. In India it is governed by the Indian Partnership Act, 1932."),
(["contract"],"Business Law","A contract is an agreement enforceable by law. Essentials: offer and acceptance, lawful consideration, capacity of parties, free consent, lawful object (Indian Contract Act, 1872). This is general education, not legal advice."),
(["void","voidable"],"Business Law","A void agreement is not enforceable at all. A voidable contract is enforceable until the injured party (e.g. one whose consent was caused by coercion or fraud) chooses to cancel it."),
(["accounting equation"],"Accountancy","Accounting Equation: Assets = Liabilities + Capital (Owner's Equity). Every transaction keeps both sides equal."),
(["debit","credit"],"Accountancy","Golden rules: Personal account - debit the receiver, credit the giver. Real account - debit what comes in, credit what goes out. Nominal account - debit expenses and losses, credit incomes and gains."),
(["depreciation"],"Accountancy","Depreciation is the decrease in the value of a fixed asset due to use, wear and tear or obsolescence. Common methods: Straight Line and Written Down Value."),
(["balance sheet"],"Accountancy","A balance sheet shows a firm's assets, liabilities and capital on a particular date. It must balance: Assets = Liabilities + Capital."),
(["journal"],"Accountancy","The journal is the book of original entry where transactions are recorded date-wise as debit and credit entries, followed by a short narration."),
(["trial balance"],"Accountancy","A trial balance lists all ledger balances to check that total debits equal total credits. It checks arithmetic accuracy only, not every error."),
]
def lookup(q):
    t=q.lower()
    for keys,subj,ans in KB:
        if any(k in t for k in keys): return subj,ans
    return None
