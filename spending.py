import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from argparse import ArgumentParser
from docx import Document
from docx.shared import Inches

""" classes for calculation and visual display """

class Calculation:
    """ Calculating various components of and building a user's financial profile.
    
    Attributes:
        total_income (float): users total income (yearly)
        fixed_expenses (dict):  contains name and dollar amount of 
                                fixed expenses (monthly)
        var_expenses (dict):  contains name and dollar amount of 
                              variable expenses (monthly)
    
    Side effects:
        creates a CSV file and a Word document, 'finances.docx'
            
    Returns:
        CSV file       
    """
    
    def __init__(self, total_income):
        self.total_income = total_income
        self.fixed_expenses = {}
        self.var_expenses = {}
        
    def user_expenses(self):
        """ Gathers user info on fixed expenses (i.e. rent, tuition, etc.) 
        and variable expenses (i.e. coffee, gas, etc.).
        
        Side effects:
            modifies self.fixed_expenses, self.var_expenses,
            creates 'expense_sheet.csv' file,
            asks user for input, 
            writes return result to Word document

        Returns:
            DataFrame object:  contains fixed and variable expenses
        
        """
        
        income_df = pd.DataFrame()
        
        while True:
            try:
                fixed = input("FIXED expenses, name? ")
                if fixed == 'done':
                    break
                if fixed.isalpha():
                    pass
                else:
                    raise TypeError
            except TypeError:
                print("Letters only please.", fixed)
                continue
            try:
                cost = input("How much?  (dollars and cents) ")
                if cost == 'done':
                    break
                cost = round(float(cost), 2)
            except ValueError:
                print("Only numbers allowed, please enter expense again.")
                continue
            self.fixed_expenses[fixed] = cost

        while True:
            try:
                var = input("VARIABLE expenses, name? ")
                if var == "done":
                    break
                if var.isalpha():
                    pass
                else:
                    raise TypeError
            except TypeError:
                print("Letters only please.")
                continue
            try:
                cost = input("How much?  (dollars and cents) ")
                if cost == 'done':
                    break
                cost = round(float(cost), 2)
            except ValueError:
                print("Please enter expense again.")
                continue
            self.var_expenses[var] = cost

        if len(self.fixed_expenses) == 0 and len(self.var_expenses) == 0:
            print("Please enter FIXED and VARIABLE expenses to continue,", 
                  "goodbye.")
            exit()
        
        income_df = pd.DataFrame({'fixed expenses':self.fixed_expenses, 
                                  'variable expenses':self.var_expenses})

        income_df.fillna(0).to_csv('expense_sheet.csv', encoding='utf-8', 
                                   index=False)
        return income_df.fillna(0)
        
    def spend_check(self):
        """ Calculates whether user is overspending by adding fixed and variable
        epxenses and comparing to the users total income.

        Side effects:
            writes return result to Word document

        Returns:
            str:  lets user know if they are over spending or on budget.
        """

        if len(self.fixed_expenses) == 0 & len(self.var_expenses) == 0:
            return 'Please run user_expenses() in Calculations class.'
        
        spend = ""
        fixed = sum(self.fixed_expenses.values())
        var = sum(self.var_expenses.values())

        overspend = round(fixed + var, 2)
        monthly_earn = round(self.total_income/12, 2)
        excess_spend = round(overspend - monthly_earn, 2)

        if fixed + var > monthly_earn:
            spend = ('Every month you are spending $' + str(overspend) + '.' +
                    '  This is $' + str(excess_spend) + 
                    ' over your monthly earnings of $' + 
                    str(monthly_earn))
        else:
            spend = ('Every month you are spending $' + str(overspend) + '.' +
                    '  This is under your monthly earnings of $' + 
                    str(monthly_earn))
        return spend

    def interest(self): 
        """Calculates the amount of interest that will be accumulated on loans.
        
        Side effects:
            asks user for input, 
            prints to the terminal,
            writes the return result to the Word document

        Returns:
            (float): the total amount of interest due at the end of the
            loan period.
        """
        interest_due = 'Total interest paid is $' + str(0.0)
        
        while True:
            try:
                loan = input("Enter NAME of loan: ")
                if loan == 'skip':
                    return interest_due
                if loan.isalpha():
                    pass
                else:
                    raise TypeError
            except TypeError:
                print("Letters only please.")
                continue
            try:
                p = input("Enter the PRINCIPAL (dollars and cents): ")
                if p == 'skip':
                    return interest_due
                p = float(p)
            except ValueError:
                print("Numbers only, please enter PRINCIPAL again.")
                continue
            try:
                r = input("Enter the RATE (% per year): ")
                if r == 'skip':
                    return interest_due
                r = float(r)
                R = r/100
            except ValueError:
                print("Numbers only, please enter RATE again.")
                continue
            try:
                t = input("Enter the TIME (months): ")
                if t == 'skip':
                    return interest_due
                t = float(t)
                T = t/12
            except ValueError:
                print("Numbers only, please enter TIME again.")
                continue
            try:
                int_type = input("Enter SIMPLE or COMPOUND: ")
                if int_type == 'skip':
                    return interest_due
                if int_type.isalpha():
                    pass
                else:
                    raise TypeError
            except TypeError:
                print("Letters only, please enter information again.")
                continue
            if int_type == "SIMPLE":
                #total_due = (p + (p * r * t))
                interest_due = ('Loan: ' + str(loan) + ', ' + 
                                 'Principal amount: ' + str(p) + 
                                 ', ' + 'Rate: ' + str(r) + '%' + 
                                 ', ' + 'Time: ' + str(t) + 
                                 ' months' + ', ' +
                                 'Simple Interest Loan' + ', ' + 
                                 'Total interest paid is $' + 
                                 str(round((p * R * T), 2)))
                return interest_due
            elif int_type == "COMPOUND":
                try:
                    n = input("Enter MONTHLY, QUARTERLY, or YEARLY: ")
                    if n.isalpha():
                        if n == "MONTHLY":
                            total_due = p * (1 + R/12)**(12*T)
                            interest_due = ('Loan: ' + str(loan) + ', ' + 
                                            'Principal amount: ' + str(p) + 
                                            ', ' + 'Rate: ' + str(r) + '%' + 
                                            ', ' + 'Time: ' + str(t) + 
                                            ' months' + ', ' +
                                            'Compounded: Monthly' + ', ' + 
                                            'Total interest paid is $' + 
                                            str(round(total_due - p, 2)))
                            break
                        elif n == "QUARTERLY":
                            total_due = p * (1 + R/4)**(4*T)
                            interest_due = ('Loan: ' + str(loan) + ', ' + 
                                            'Principal amount: ' + str(p) + 
                                            ', ' + 'Rate: ' + str(r) + '%' + 
                                            ', ' + 'Time: ' + str(t) + 
                                            ' months' + ', ' +
                                            'Compounded: Quarterly' + ', ' + 
                                            'Total interest paid is $' + 
                                            str(round(total_due - p, 2)))
                            break
                        elif n == "YEARLY":
                            total_due = p * (1 + R/1)**(1*T)
                            interest_due = ('Loan: ' + str(loan) + ', ' + 
                                            'Principal amount: ' + str(p) + 
                                            ', ' + 'Rate: ' + str(r) + '%' + 
                                            ', ' + 'Time: ' + str(t) + 
                                            ' months' + ', ' +
                                            'Compounded: Yearly' + ', ' + 
                                            'Total interest paid is $' + 
                                            str(round(total_due - p, 2)))
                            break
                        else:
                            pass
                    else:
                        raise TypeError
                except TypeError:
                    print("Letters only please, please enter information ",
                          "again.")
                    continue
        return interest_due

    def spending_allocation(self): 
        """Calculates the percentage of income that goes towards fixed/variable 
        expenses.
        
        Side effects:
            prints to the terminal,
            writes the return result to the Word document
    
        Returns:
            (tuple): the percentage of income going towards each category.
        """
        if len(self.fixed_expenses) == 0 & len(self.var_expenses) == 0:
            return 'Please run user_expenses() in Calculations class.'
        
        fixed = sum(self.fixed_expenses.values())
        var = sum(self.var_expenses.values())

        pctg1 = round((fixed/self.total_income)*100, 2)
        pctg2 = round((var/self.total_income)*100, 2)
        return pctg1, pctg2

class Graphs:
    """  A visual representation of user spending
    
    Attributes:
        expense (dict):  name and dollar amount of users monthly expenses

    Returns:
        pie chart, bar plot
    """
    
    def __init__(self):
        self.expense = {}

    def expenses(self, fixed, var):
        """ Provides a visual representation of the users expenses
        
        Args:
            fixed (dict):  name and dollar amount of fixed expenses (monthly)
            var (dict):  name and dollar amount of variable expenses (monthly)
        
        Side effects:
            modifies self.expense, prints to the terminal, and displays visual
            graphic

        Returns:
            bar plot:  displays users' expenses
        """
        if len(fixed) == 0 & len(var) == 0:
            return 'Please run user_expenses() in Calculations class.'
        
        for x in [fixed, var]:
            self.expense.update(x)
        keys = self.expense.keys()
        values = self.expense.values()
        
        fig, ax = plt.subplots()
        bp = ax.bar(keys, values)
        
        ax.set_ylabel("Amount in dollars")
        ax.set_title("User Fixed and Variable Expenses")
        ax.set_xlabel("Expense Name")
        return plt.show()

    def habits(self, income):
        """  Provides a visual representation of how much money the user 
        would save by cutting back on specific spending habits.
        
        Args:
            income (float):  users total income (yearly amount)
        
        Side effects:
            prints to the terminal, displays visual graphic
        
        Returns:
            pie chart:  displays users' spending habits  
        """
        
        habits = {}
        
        while True:
            try:
                habit = input("Enter NAME of habit (one word): ")
                if habit == "done":
                    break
                if habit == "none":
                    break
                if habit.isalpha():
                    pass
                else:
                    raise TypeError
            except TypeError:
                print("Letters only please.")
                continue
            try:
                cost = input("How much do you spend monthly to supplement this " +
                                "habit? (enter dollars and cents): ")
                cost = float(cost)
                habits[habit] = cost
                continue
            except ValueError:
                print("Numbers only please.")
                continue

        hab = [] 
        total = []
        saving = 0.0
        lst = []

        for k, v in habits.items():
            hab.append(k)
            total.append(v)
            print('You are spending ' + str(v) + 
                  ' dollar(s) every month on ' + '[' + k + ']' + '.')
            print('This means every year you are spending ' + str(v*12) + 
                  ' dollar(s) on ' + '[' + k + ']' + '.')
            print('[' + k + ']' + ' account(s) for ' + 
                  str(round(((v*12)/income)*100, 2)) + 
                  ' percent of your total income per year.\n')
            saving += v*12
            lst.append((k, v, v*12))
        
        print('You are spending $' + str(round(saving, 2)) + 
              ' dollar(s) a year on your habits.')
        
        for_doc = (lst)
        
        if len(habits) == 0:
            for_doc = "No habits entered."

        labels = hab
        sizes = total
        
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct = '%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title("Habits")
        
        return for_doc, plt.show()

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("total_income", help="total income for current year",
                        type=float)
    args = parser.parse_args(arglist)
    return args

def main(arglist):
    count = 0
    lst = set()
    lst2 = set()
    
    args = parse_args(arglist)
    c = Calculation(args.total_income)
    g = Graphs()
    
    d = Document()
    d.add_heading("Three Blind Programmers Presents:  A Birds-eye-view" 
                  " of your finances", 0)
    d.add_paragraph('Yearly income: $' + str(c.total_income))
    d.add_heading('Monthly fixed and variable expenses.', 1)
    
    print(c.user_expenses())
    for exp, num in c.fixed_expenses.items():
        count += 1
        lst.add(str((exp, num)))
    
    count = 0
    for exp, num in c.var_expenses.items():
        count += 1
        lst2.add(str((exp, num)))
    
    table = d.add_table(rows=count, cols=2)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Fixed Expenses'
    hdr_cells[1].text = 'Variable Expenses'

    for num in lst:
        row_cells = table.add_row().cells
        row_cells[0].text = num
    
    for num in lst2:
        row_cells = table.add_row().cells
        row_cells[1].text = num
    
    print(c.spend_check())
    d.add_heading('Spending per month.', 1)
    d.add_paragraph(str(c.spend_check()))

    d.add_heading('Loan information.', 1)
    d.add_paragraph(str(c.interest()))
    
    print('Fixed/variable spending, respectively (percent of total income): ' 
          + str(c.spending_allocation()))
    d.add_heading('Monthly expenses against total income: $' + 
                  str(c.total_income), 1)
    d.add_paragraph('Fixed expenses account for ' + 
                    str(c.spending_allocation()[0]) + '%' + 
                    ' of your total income, totaling $' + 
                    str(sum(c.fixed_expenses.values())) + ' a month.')
    d.add_paragraph('Variable expenses account for ' + 
                    str(c.spending_allocation()[1]) + '%' + 
                    ' of your total income, totaling $' + 
                    str(sum(c.var_expenses.values())) + ' a month.')
    
    print(g.expenses(c.fixed_expenses, c.var_expenses))

    d.add_heading('Monthly habit expenses.', 1)
    d.add_paragraph('Habit, Monthly cost, Yearly cost')
    d.add_paragraph(str(g.habits(c.total_income)[0]))
    
    d.save('finances.docx')
  
if __name__ == "__main__":
    main(sys.argv[1:])