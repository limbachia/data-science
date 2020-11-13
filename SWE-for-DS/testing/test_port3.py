import unittest 
from portfolio1 import Portfolio

class PortfolioSellTest(unittest.TestCase):
    # The following setUp method is invoked before each test method
    def setUp(self):
        self.p = Portfolio()
        self.p.buy("MSFT", 100, 27.0)
        self.p.buy("DELL", 100, 17.0)
        self.p.buy("ORCL", 100, 34.0)
        
    def test_sell(self):
        self.p.sell("MSFT", 50)
        self.assertEqual(self.p.cost(),6450)
    
    def test_not_enough(self):
        with self.assertRaises(ValueError):
            self.p.sell("MSFT",200)
            
    def test_dont_own_it(self):
        with self.assertRaises(ValueError):
            self.p.sell("IBM",1)
