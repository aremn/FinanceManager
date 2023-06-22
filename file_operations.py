import csv


def save_data(user, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Source/Category", "Amount", "Date"])
        for income in user.incomes:
            writer.writerow(["Income", income.source, income.amount, income.date])
        for expense in user.expenses:
            writer.writerow(["Expense", expense.category, expense.amount, expense.date])


def load_data(filename, user):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            if row[0] == "Income":
                user.add_income(row[1], float(row[2]))
            elif row[0] == "Expense":
                user.add_expense(row[1], float(row[2]))
