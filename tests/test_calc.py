import sys,os,unittest
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","backend"))
os.environ["OFFLINE_ONLY"]="1"
import calc, app
class T(unittest.TestCase):
    def test_si(self): self.assertIn("= 1,200.00",calc.calculate("simple interest on 5000 at 8% for 3 years"))
    def test_ci(self): self.assertIn("CI = A - P = 1,000.00",calc.calculate("compound interest 10000 at 10% for 1 year"))
    def test_cr(self): self.assertIn("2.00 : 1",calc.calculate("current ratio assets 50000 liabilities 25000"))
    def test_bep(self): self.assertIn("100.00 units",calc.calculate("break even fixed cost 5000 price 100 variable cost 50"))
    def test_ed(self): self.assertIn("elastic",calc.calculate("elasticity price 10 to 8 quantity 100 to 130"))
    def test_dep(self): self.assertIn("18,000.00",calc.calculate("straight line depreciation cost 100000 scrap 10000 life 5"))
    def test_empty(self): self.assertEqual(app.answer({"question":" "})[0],400)
    def test_kb(self): self.assertEqual(app.answer({"question":"what is inflation"})[1]["source"],"offline")
    def test_unknown(self): self.assertEqual(app.answer({"question":"zzz"})[1]["source"],"offline")
if __name__=="__main__": unittest.main()
