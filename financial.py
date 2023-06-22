class Income:
    def __init__(self, source, amount, date):
        self.source = source
        self.amount = amount
        self.date = date


class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date
