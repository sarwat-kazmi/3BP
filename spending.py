import pandas as pd
import numpy as np
import matplotlib
import csv
import sys
from argparse import ArgumentParser


""" classes for calculation and visual display """

class Calculation:
    """ Calculating various components of and building a user's financial profile.
    
    Attributes:
        total_income (float): users total income (yearly)
            
    Returns:
        CSV file       
    """
    
    def __init__(self, total_income):
        self.total_income = total_income
        
    def user_expenses(self):
        """ Gathers user info on fixed expenses (i.e. rent, tuition, etc.) 
        and variable expenses (i.e. coffee, gas, etc.).
        
        Args:
            fixed_expenses (dict): dictionary of user's fixed expenses
            var_expenses (dict): dictionary of user's variable expenses
        
        Returns:
            Dictionaries of user's financial profile
        
        """

        fixed_expenses = {}
        var_expenses = {}
        """
        test_fixed = {'rent':1000.00, 'loans':400.00, 'cellphone':200.00}
        test_var = {'gas':60.0, 'gifts':150.00, 'clothing':400.00}
        """
        income_df = pd.DataFrame()

        while True:
            fixed = str(input("FIXED expenses, name? "))
            if fixed == "done":
                break
            cost = float(input("How much?  (dollars and cents) "))
            fixed_expenses[fixed] = cost

        while True:
            var = str(input("VARIABLE expenses, name? "))
            if var == "done":
                break
            cost = float(input("How much?  (dollars and cents) "))
            var_expenses[var] = cost

        print(fixed_expenses)
        print(var_expenses)
        
        income_df = pd.DataFrame({'fixed expenses':fixed_expenses, 
                                  'variable expenses':var_expenses})

        income_df.fillna(0).to_csv('expense_sheet.csv', encoding='utf-8', 
                                   index=False)
        """
        test_df = pd.DataFrame({'fixed expenses':test_fixed, 
                                  'variable expenses':test_var})
        """
        return income_df.fillna(0)
        
    def spend_check(self):
        """ Calculates whether user is overspending by adding fixed and variable
        epxenses and comparing to the users total income.

        Returns:
            str:  lets user know if they are over spending or on budget.
        """
        spend = ""

        check = Calculation(self.total_income)
        user_expenses = check.user_expenses()
        fixed = sum(user_expenses['fixed expenses'])
        var = sum(user_expenses['variable expenses'])

        overspend = round(fixed + var, 2)
        monthly_earn = round(self.total_income/12, 2)
        excess_spend = round(monthly_earn - overspend, 2)

        if fixed + var > monthly_earn:
            spend = ('Every month you are spending $' + str(overspend) + '.' +
                    '  This is $' + str(excess_spend) + 
                    ' dollars over your monthly earnings of $' + 
                    str(monthly_earn))
        else:
            spend = ('Every month you are spending $' + str(overspend) + '.' +
                    '  This is under your monthly earnings of $' + 
                    str(monthly_earn))
        return spend

    def interest(self): 
        """Calculates the amount of interest that will be accumulated on loans.
        
        Returns:
            (float): the total amount of interest due at the end of the
            loan period.
        """
        
        while True: 
            loan = str(input("Enter NAME of loan: "))
            p = float(input("Enter the PRINCIPAL (dollars and cents): "))
            r = float(input("Enter the RATE (% per year): "))
            R = r/100
            t = int(input("Enter the TIME (months): "))
            T = t/12
            int_type = str(input("Enter SIMPLE or COMPOUND: "))

            if int_type == "SIMPLE": 
                #total_due = (p + (p * r * t))
                interest_due = p * R * T
                break
            elif int_type == "COMPOUND":
                n = str(input("Enter MONTHLY, QUARTERLY, or YEARLY: "))
                if n == "MONTHLY":
                    total_due = p * (1 + R/12)**(12*T)
                    interest_due = round(total_due - p)
                    break
                elif n == "QUARTERLY":
                    total_due = p * (1 + R/4)**(4*T)
                    interest_due = round(total_due - p, 2)
                    break
                elif n == "YEARLY":
                    total_due = p * (1 + R/1)**(1*T)
                    interest_due = round(total_due - p, 2)
                    break
                else:
                    pass
        
        print("Loan: " + loan)
        print("Principal amount: " + str(p))
        print("Rate: " + str(r) + '%')
        print("Time: " + str(t) + ' months')
        return interest_due

    def spending_allocation(self): 
        """Calculates the percentage of income that goes towards fixed/variable 
        expenses.
    
<<<<<<< HEAD
=======
    def spending_allocation(self, var_spend, var_expenses): 
        """Calculates the percentages of income that goes towards variable 
        expenses (groceries, recreation, etc).

>>>>>>> 8339f3b8a1096a9c6563f0c4819f8a7bd3c03876
        Returns:
            (tuple): the percentage of income going towards each category.
        """
<<<<<<< HEAD
        
        check = Calculation(self.total_income)
        
        user_expenses = check.user_expenses()
        
        fixed = sum(user_expenses['fixed expenses'])
        var = sum(user_expenses['variable expenses'])

        pctg1 = round((fixed/self.total_income)*100, 2)
        pctg2 = round((var/self.total_income)*100, 2)
        return pctg1, pctg2
=======
        pctg = (var_spend/total_income)
        return("Percentage of income going toward all variable expenses: {:.2%}".format(pctg))
        
        for key in var_expenses:
            eachpctg = (var_expenses[key]/total_income) 
            print("Percentage of income going toward",key,": {:.2%}".format(eachpctg))

>>>>>>> 8339f3b8a1096a9c6563f0c4819f8a7bd3c03876

class Graphs:
    """  A visual representation of user spending
    
    Attributes:
        expenses (dict):  dictionary of users monthly expenses

    Returns:
        pie chart, bar plot
    """
    
    def __init__(self):
        self.expenses = {}

    def expenses(self):
        """ Provides a visual representation of the users expenses
        
        Returns:
            bar plot of users' expenses
        """

    def cutbacks(self):
        """  Provides a visual representation of how much money the user 
        would save by cutting back on specific spending habits.
        
        Returns:
            pie chart of money saved  
        """
        
        habits = {}
        
        while True:
            habit = input(str("Enter NAME of habit (one word): "))
            if habit == "done":
                break    
            cost = float(input("How much do you spend monthly to supplement this "
                             "habit? (enter dollars and cents): "))
            habits[habit] = cost

        costs = {}
        total = 0.0
        
        for v in habits.values():
            total += v*12
        costs['habits'] = total
        
        return round(costs['habits'], 2)

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("total_income", help="total income for current year",
                        type=float)
    args = parser.parse_args(arglist)
    return args

def main(arglist):
    args = parse_args(arglist)
    c = Calculation(args.total_income)
    #print(c.user_expenses())
    print(c.spend_check())
    #print('Total interest paid is $' + str(c.interest()))
    #print('Fixed/variable spending (percent of total income): ' 
    #      + str(c.spending_allocation()))
    g = Graphs()
    #expenses = c.user_expenses()
    #fixed = float(sum(expenses['fixed expenses']))
    #var = float(sum(expenses['variable expenses']))
    #print('You could be saving $' + str(g.cutbacks()) + 
    #          ' dollar(s) every year.')
    
if __name__ == "__main__":
    main(sys.argv[1:])