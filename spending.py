class Calculation:
    """ Docstring for class goes here """
    
    function 1 # Sarwat:
        sdf
    
    function 2 # Sarwat:
        sdf
    
    def interest(): # Laraib:
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
    
    def spending_allocation(): # Laraib:
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
    
    Args:
        earnings (dict):  dictionary of monthly income
        expenses (dict):  dictionary of monthly outflow
    """
    
    def __init__(self, earnings, expenses):

    def biggest_expenses(self):
        """ Provides a visual representation of the users largest expenses
        """
        
    def cutbacks(self):
        """  Provides a visual representation of how much money the user 
        would save by cutting back on specific spending habits.
        """