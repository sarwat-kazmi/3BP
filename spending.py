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
            cost = int(input("How much did you spend?"))
            
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
            
    
    def spend_check(self, fixed_spend, var_spend):
        """ Calculates whether user is overspending by checking whether their 
        variable expenses surpass their fixed expenses.
        
        Args:
            fixed_spend (float): amount of fixed expenses
            var_spend (float): amount of variable expenses
        
        Returns:
            break_even (float): check point to see how expenditures 
            and earnings compare
        
        """
        
        
    
    def interest(self, principle_amt, interest_rate, duration, int_type = "simple"): 
        """Calculates the amount of interest that will be accumulated on loans.
        
        Args:
            principle_amt(float): the principle amount of the loan
            interest_rate(float): the interest rate on the loan
            duration(int): the time in years of the loan
            int_type(str): simple or compound interest
        
        Returns:
            (float): the total amount of interest due at the end of the
            loan period.
        """
        if int_type == "simple": 
            interest_due = (principle_amt * interest_rate * duration) / 100 
        
        if int_type == "compound":
            interest_due = principle_amt * ((1 + interest_rate/100)**duration)
    
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
        
    def cutbacks(self, habits):
        """  Provides a visual representation of how much money the user 
        would save by cutting back on specific spending habits.
        
        Args:
            habits (dict):  a dictionary of habits that could be cut to save 
            money, monthly spending
            
        Returns:
            pie chart of money saved  
        """