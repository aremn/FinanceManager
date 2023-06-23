import csv
import datetime


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
        available_years = set()  # Initialize available years set
        for row in reader:
            if row[0] == "Income":
                user.add_income(row[1], float(row[2]), datetime.datetime.strptime(row[3], "%Y-%m-%d").date())
                available_years.add(row[3][:4])  # Add year to available years
            elif row[0] == "Expense":
                user.add_expense(row[1], float(row[2]), datetime.datetime.strptime(row[3], "%Y-%m-%d").date())
                available_years.add(row[3][:4])  # Add year to available years
        return available_years
