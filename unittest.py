import unittest
from spending import Graphs

class TestSkills(unittest.TestCase):
    
    def setUp(self):
        self.graph1 = Graphs({"host job": 400, "delivery": 500}, {"cellphone": 100, "gas bill": 60})
        self.graph2 = Graphs({"cyber security consultant", 7500}, {"mortgage": 1400, "cellphone": 120})
        
    def test_biggestexpense(self):
        self.assertEqual(self.graph2.earnings, dict)
                             
    if __name__ == '__main__':
        unittest.main()