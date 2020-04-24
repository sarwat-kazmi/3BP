import pandas as pd
import numpy as np
import matplotlib
import csv


""" classes for calculation and visual display """

class Calculation:
    """ Calculating various components of and building a user's financial profile.
    
    Attributes:
        total_income (float): total income user makes
        total_expenses (float): total of expenses user spends on
        fixed_expenses (float):  total number for fixed expenses
        var_expenses (float):  total number for variable expenses
            
    Returns:
        CSV file       
    """
    
    def __init__(self, total_income, total_expenses, fixed_expenses, var_expenses):
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.fixed_expenses = fixed_expenses
        self.var_expenses = var_expenses

    def user_expenses(self, fixed_expenses, var_expenses):
        """ Gathers user info on fixed expenses (i.e. rent, tuition, etc.) 
        and variable expenses (i.e. coffee, gas, etc.).
        
        Args:
            fixed_expenses (dict): dictionary of user's fixed expenses
            var_expenses (dict): dictionary of user's variable expenses
        
        Returns:
            Dictionaries of user's financial profile
        
        """
        
        # dictionaries for expenses
        
        fixed_expenses = {}
        # ex. "rent": 1000.00, "tuition": 5000.00, "car insurance": 200.00, 
        # "student loans": 500.00, "gym": 90.00
        
        var_expenses = {}
        # ex. "gifts": 150.00, "clothing": 400.00, "gas": 100.00, 
        # "groceries": 200.00, "parking": 85.00
        
        while True:
            
            # FIXED EXPENSES
            
            # name of expense (i.e. rent, tuition)
            fixed = input(str("FIXED expenses, name? "))
            if fixed == "done":
                break
            # how much they spent (i.e. 500.00)
            cost = input("How much?  (dollars and cents) ")

            fixed_expenses[fixed] = cost
            
        while True:
            
            # VARIABLE EXPENSES
            
            var = input(str("VARIABLE expenses, name? "))
            if var == "done":
                break
            cost = input("How much?  (dollars and cents) ")
            
            var_expenses[var] = cost

        with open('user_expenses.csv', 'w', newline='') as csvfile:
            csv_col = ['Expense Type', 'Expense Cost']
            writer = csv.DictWriter(csvfile, fieldnames=csv_col)
            writer.writeheader()
    
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
            fixed_spend = sum(fixed_expenses.values())
            var_spend = sum(var_expenses.values())
            total_income = float(input("Enter total income here: "))
            total_spend = fixed_spend + var_spend
            if total_spend > total_income:
                print("You have gone over budget.")
            else:
                print("You are within budget.")
            
    def interest(self): 
        """Calculates the amount of interest that will be accumulated on loans.
       
        Returns:
            (float): the total amount of interest due at the end of the
            loan period.
        """
        
        loan = str(input("Enter what the loan is for: "))
        principle_amt = float(input("Enter the principle amount of the loan: "))
        interest_rate = float(input("Enter the interest rate on the loan: "))
        duration = int(input("Enter the full duration of the loan: "))
        int_type = str(input("Enter if 'simple' or 'compound': "))
        
        if int_type.lower() == "simple": 
            interest_due = (principle_amt * interest_rate * duration) / 100
            print(interest_due)
        
        else:
            interest_due = principle_amt * ((1 + interest_rate/100)**duration)
            print(interest_due)
            
    #repeat()
    
    #def repeat(): potential function to repeat interest() calculations for a diff loan
        #repeat = input("Would you like to get the total interest due for another loan? enter yes or no: ")
        #if repeat.lower() == "yes":
            #interest()
        #elif repeat.lower() == "no":
            #print("Your interest amounts have been calculated.")
        #else:
            #repeat()
    
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
        
        
        for exp in self.expenses.items():
            
        
        
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
                             "habit? (enter dollars and cents)"))
            
            habits[habit] = cost
            
            if habit == "done":
                break
        
        costs = {}
        total = 0
        
        for k, v in dict.items():
            total += v*12
        
        costs['habits'] = total
        
        print('You could be saving ' + str(costs['habits']) + ' dollar(s) every year')
