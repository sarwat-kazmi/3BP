class Calculation:
    """ Calculating various components of and building a user's financial profile.
    
    Attributes:
        total_income (float): total income user makes
        total_expenses (float): total of expenses user spends on        
    """
    
    def __init__(self, total_income, total_expenses):

    def user_expenses(self, fixed_expenses, var_expenses):
        """ Gathers user info on fixed expenses (i.e. rent, tuition, etc.) 
        and variable expenses (i.e. coffee, gas, etc.).
        
        Args:
            fixed_expenses (float): sum of user fixed expenses
            var_expenses (float): sum of user variable expenses
        
        Returns:
            CSV of user's financial profile
        
        """
    
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
    
    def interest(self, principle_amt, interest_rate, duration): # Laraib:
        """Calculates the amount of interest that will be accumulated on loans
        as well as remaining balance.
        
        Args:
            principle_amt(float): the principle amount of the loan
            interest_rate(float): the interest rate on the loan
            duration(int): the time in years of the loan
        
        Returns:
            (float): the total amount of interest due at the end of the
            loan period.
        """
        # if simple interest
        #interest_due = (principle_amt * interest_rate * duration) / 100 
        
        # if compound interest
        #interest_due = principle_amt * ((1 + interest_rate/100)**duration)
    
    def spending_allocation(self): # Laraib:
        """Calculates the percentages of income that goes towards everyday 
        expenses (recreation, groceries, dining, etc).
        
        Args:
            total_income(float): total earnings
            rec_spending(float): the amount spent on recreational activities
            grocery_spending(float): the amount spent on groceries
        
        Returns:
            (float): the percentage of income going towards each category.
        """

class Graphs:
      """  A visual representation of user spending
    
    Attributes:
        earnings (dict):  dictionary of yearly income
        expenses (dict):  dictionary of yearly outflow 
    """
    
    def __init__(self, earnings, expenses):

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