import unittest
from spending import Calculation, Graphs

class TestSkills(unittest.TestCase):
    
    def setUp(self):
        self.calculation1 = Calculation(40000.00, 10000.00)
        self.calculation2 = Calculation(98000.00, 33000.00)
        self.graph1 = Graphs({"maitre'd": 19200.00, "delivery driver": 24000.00}, {"cellphone": 1200.00, "gas bill": 720.00})
        self.graph2 = Graphs({"cyber security consultant", 90000.00}, {"mortgage": 16800.00, "cellphone": 1440.00})
    
    def test_income_df(self):
        # check that sum of each column in the dataframe is equal to the sum of the dictionary values
        self.assertEqual(income_df['fixed expenses'].sum, sum(fixed_expenses.values()))
        self.assertEqual(income_df['variable expenses'].sum, sum(var_expenses.values()))
    
    def test_validation(self):
        with self.assertRaises(ValueError):
            Graphs(["plumber", 3000], ["welder", 3000])
            Calculation("addition", "subtraction")
    
    def test_income_expenses(self):
        self.graph3 = Graphs({"high school teacher": 35000.00}, {"pepco bill":720.00})
        self.assertEqual(self.calculation1.total_income, 40000.00)
        self.assertEqual(self.calculation1.total_expenses, 10000.00)
        self.assertEqual(self.graph3.earnings, {"high school teacher": 35000.00}, {"pepco bill": 720.00})
    
    def test_habits(self):
        dict1 = {"smoking": 64.00, "eating out for lunch": 200.00}
        self.assertEqual(self.graph1.cutbacks(dict1), {"smoking": 64.00, "eating out for lunch": 200.00}) 
    
if __name__ == '__main__':
    unittest.main()