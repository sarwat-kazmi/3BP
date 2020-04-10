import unittest
from spending import Graphs

class TestSkills(unittest.TestCase):
    
     def setUp(self):
        self.calculation1 = Calculation()
        self.graph1 = Graphs({"maitre'd": 400.00, "delivery": 500.00}, {"cellphone": 100.00, "gas bill": 60.00})
        self.graph2 = Graphs({"cyber security consultant", 7500.00}, {"mortgage": 1400.00, "cellphone": 120.00})
    
    def test_user_expenses(self):
        test = self.calculation1.user_expenses(40000.00, 10000.00, 5400.00, 4600.00)
        self.assertEqual(test, float)

    def test_spend_check(self):        
    
    def test_validation(self):
        with self.assertRaises(ValueError):
            Graphs(["plumber", 3000], ("welder", 3000))
    
    def test_habits(self):
        lst = {"smoking": 64.00, "eating out for lunch": 200.00}
        self.assertEqual(self.graph1.cutbacks(lst), list())
    
    if __name__ == '__main__':
        unittest.main()