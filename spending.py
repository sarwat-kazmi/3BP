import pandas as pd
import numpy as np
import madplotlib
import csv


""" classes for calculation and visual display """

class Calculation:
    """ Calculating various components of and building a user's financial profile.
    
    Attributes:
        total_income (float): total income user makes
        total_expenses (float): total of expenses user spends on
            
    Returns:
        CSV file       
    """
    
    def __init__(self, total_income, total_expenses):

    def user_expenses(self, fixed_expenses, var_expenses):
        """ Gathers user info on fixed expenses (i.e. rent, tuition, etc.) 
        and variable expenses (i.e. coffee, gas, etc.).
        
        Args:
            fixed_expenses (dict): dictionary of user's fixed expenses
            var_expenses (dict): dictionary of user's variable expenses
        
        Returns:
            Dictionaries of user's financial profile
        
        """
        
        # # # dictionaries for expenses
        fixed_expenses = {}
        #"rent": 1000, "tuition": 5000, "car insurance": 200, "student loans": 500, "gym": 90
        var_expenses = {}
        # "gifts": 150, "clothing": 400, "gas": 100, "groceries": 200, "parking": 85
        
        expenses = True
        
        while expenses:
            # type of expense (i.e. gym, food)
            type = input("What type of expense was it?")
            # how much they spent
            cost = float(input("How much did you spend?"))
            
            # asking which expense to append to respective dictionary
            exp = input("Which expense did you spend on?")
            if exp == "fixed":
                fixed_expenses[type] = cost
            elif exp == "variable":
                var_expenses[type] = cost
            else:
                break
            
        # creating csv column headers
        csv_col = ['Fixed or Variable', 'Expense Type', 'Expense Cost']
        
        with open('expenses.csv', 'w', newLine='') as f:
            write = csv.DictWriter(f, filenames = csv_col)
            write.writeheader()
    
    def spend_check(self, fixed_spend, var_spend):
        """ Calculates whether user is overspending by checking whether their 
        variable expenses surpass their fixed expenses.
        
        Args:
            fixed_spend (float): amount of fixed expenses
            var_spend (float): amount of variable expenses
        
        Returns:
            total_spend (float): check point to see how expenditures 
            and earnings compare
        
        """
        
        while True:
            total_income = float(input("Enter total income here: "))
            total_spend = fixed_spend + var_spend
            if total_spend > total_income:
                print("You have gone over budget.")
            else:
                print("You are within budget.")
            
    def interest(self, principle_amt, interest_rate, duration, int_type, loan): 
        """Calculates the amount of interest that will be accumulated on loans.
        
        Args:
            principle_amt(float): the principle amount of the loan
            interest_rate(float): the interest rate on the loan
            duration(int): the time in years of the loan
            int_type(str): simple or compound interest
            loan(str): the type of loan (student, etc)
        
        Returns:
            (float): the total amount of interest due at the end of the
            loan period.
        """
        
        while True: 
            loan = str(input("Enter what the loan is for: "))
            principle_amt = float(input("Enter the principle amount of the loan: "))
            interest_rate = float(input("Enter the interest rate on the loan: "))
            duration = int(input("Enter the full duration of the loan: "))
            int_type = str(input("Enter if simple or compound: "))
            if input("Would you like to get the total interest due for another loan? yes/no: ") == "no":
                break

            if int_type == "simple": 
                interest_due = (principle_amt * interest_rate * duration) / 100
                return interest_due 
        
            elif int_type == "compound":
                interest_due = principle_amt * ((1 + interest_rate/100)**duration)
                return interest_due
    
    def spending_allocation(self, var_expenses): 
        """Calculates the percentages of income that goes towards variable 
        expenses (groceries, recreation, etc).
        
        Args:
            var_expenses(float): total variable expenses
            
        Returns:
            (float): the percentage of income going towards each category.
        """
        pctg = (var_expenses/total_income)
        return("Percentage of income going toward variable expenses: {:.2%}".format(pctg))

class Graphs:
      """  A visual representation of user spending
    
    Attributes:
        earnings (dict):  dictionary of yearly income
        expenses (dict):  dictionary of yearly outflow
    
    Returns:
        pie chart, bar plot
    """
    
    def __init__(self, earnings, expenses):
        self.earnings = {}
        self.expenses = {}

    def biggest_expenses(self):
        """ Provides a visual representation of the users largest expenses
        
        Returns:
            bar plot of largest expenses from expenses dictionary
        """
        print('balls')
        
        
    def cutbacks(self):
        """  Provides a visual representation of how much money the user 
        would save by cutting back on specific spending habits.
        
        Returns:
            pie chart of money saved  
        """
        
        habits = {}
        
        while True:
            habit = input(str("Enter name of habit (one word)"))    
            cost = input(float("How much do you spend monthly to supplement this"
                             "habit? (enter dollars and decimals)"))
            
            habits[habit] = cost
            
            if habit == "done":
                break
        
        print(habits)
        
x = Graphs({'job':40000.00, 'online sales':10000.00}, {'gas':960, 'phone':1200})
print(x.cutbacks())


        
        