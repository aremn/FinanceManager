import datetime
from financial import Income, Expense


class User:
    predefined_incomes = ["Salary", "Dividends", "Rent"]
    predefined_expenses = ["Groceries", "Rent", "Bills", "Entertainment"]

    def __init__(self, name, date_input='auto'):
        self.name = name
        self.incomes = []
        self.expenses = []
        self.date_input = date_input

    def add_income(self, source, amount, date=None):
        if date is None:
            date = self.get_date()
        self.incomes.append(Income(source, amount, date))
        if source not in self.predefined_incomes:
            self.predefined_incomes.append(source)

    def add_expense(self, category, amount, date=None):
        if date is None:
            date = self.get_date()
        self.expenses.append(Expense(category, amount, date))
        if category not in self.predefined_expenses:
            self.predefined_expenses.append(category)

    def get_date(self):
        if self.date_input == 'auto':
            return datetime.date.today()
        else:
            while True:
                try:
                    date_str = input("Enter date (yyyy-mm-dd): ")
                    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                    return date
                except ValueError:
                    print("Invalid date format. Please try again.")

    def total_income(self):
        return sum([income.amount for income in self.incomes])

    def total_expense(self):
        return sum([expense.amount for expense in self.expenses])

    def savings(self):
        return self.total_income() - self.total_expense()

    def operation_count(self):
        return len(self.incomes) + len(self.expenses)

    def last_operation_date(self):
        dates = [income.date for income in self.incomes] + [expense.date for expense in self.expenses]
        if dates:
            return max(dates)
        return None
