import unittest
from unittest.mock import patch
from spending import Calculation, Graphs

class TestSpending(unittest.TestCase):
    """ Test the Calculation methods."""
    def setUp(self):
        
        self.calc1 = Calculation(50000.00) #laraib
        self.calc1.user_expenses() # laraib 
        self.calc1.spend_check()
        self.calc1.spending_allocation()
        
        #self.calculation1 = Calculation(40000.00, 10000.00)
        #self.calculation2 = Calculation(98000.00, 33000.00)
        
    def test_total_income(self): #laraib
        """ A newly initialized Calculation instance should have a total_income 
        attribute equal to the total income passed in."""
        
        self.assertTrue(hasattr(self.calc, "total_income"), "Calculation has no"
                        " total_income attribute")
        self.assertEqual(self.calc.total_income, 50000.00, "total_income"
                         " attribute of new Calculation instance is wrong")
    
    def test_income_df(self): #laraib
        # check that sum of each column in the dataframe is equal to the sum 
        # of the dictionary values
        self.assertEqual(income_df['fixed expenses'].sum, 
                         sum(fixed_expenses.values()))
        self.assertEqual(income_df['variable expenses'].sum, 
                         sum(var_expenses.values()))
    
    def test_validation(self):
        with self.assertRaises(ValueError):
            Graphs(["plumber", 3000], ["welder", 3000])
            Calculation("addition", "subtraction")
    
    def test_income_expenses(self):
        self.graph3 = Graphs({"high school teacher": 35000.00}, {"pepco bill":720.00})
        self.assertEqual(self.calculation1.total_income, 40000.00)
        self.assertEqual(self.calculation1.total_expenses, 10000.00)
        self.assertEqual(self.graph3.earnings, {"high school teacher": 35000.00}, {"pepco bill": 720.00})
    
    def test_spending_allocation(self): #laraib
        """ Is spending_allocation correct given fixed_expenses, var_expenses 
        dictionaries as well as total_income? """
        self.assertEqual(spending_allocation(self.calc1))
    
    #fixed_expenses = {"cellphone": 1200.00, "gas": 720.00, "car": 200.00}
    #var_expenses = {"movies": 20.00, "groceries": 65.00}
    #total_income = 50000.00
    
    #@patch('builtins.input', side_effect = [total_income, fixed_expenses, 
                                            #var_expenses])
    #def test_spendalloc(self, mock_inputs):
        #pctg1, pctg2 = spending_allocation()
        #self.assertEqual(pctg1, pctg2, 4.24, 0.17) 
        
    def test_habits(self):
        dict1 = {"smoking": 64.00, "eating out for lunch": 200.00}
        self.assertEqual(self.graph1.cutbacks(dict1), {"smoking": 64.00, "eating out for lunch": 200.00}) 

class TestGraphs(unittest.TestCase): #laraib
    """ Test Graphs methods."""
    def setUp(self):
        
        self.graph1 = Graphs()
        self.graph1.expenses({"cellphone": 1200.00, "gas": 720.00, "car": 200.00},
                             {"movies": 20.00, "groceries": 65.00})
        self.graph1.habits(50000.00)
    
    def test_expenses(self): #laraib
        """ self.expense is a dictionary created from the 
        keys and values of both fixed and var. Is the sum of the values 
        in the self.expense dictionary equal to the sum of the values in fixed 
        plus the sum of the values in var?
        """
        
        self.assertEqual(sum(self.expense.values()), 2205.00)
        
        #self.graph1 = Graphs({"maitre'd": 19200.00, "delivery driver": 24000.00}, {"cellphone": 1200.00, "gas bill": 720.00})
        #self.graph2 = Graphs({"cyber security consultant", 90000.00}, {"mortgage": 16800.00, "cellphone": 1440.00})
    
    @patch("builtins.input", side_effect = [habit1, cost1, habit2, cost2, habit3,
                                            cost3, habit4, cost4, habit5])
    def test_habits(self): 
        habits = input_habits()
        self.assertEqual(habits, {"uber eats": 34.50, "online shopping": 50.00, 
                                  "fast food": 25.60, "smoking": 14.00})
    
if __name__ == '__main__':
    unittest.main()