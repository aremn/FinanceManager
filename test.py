import random
import csv
import datetime
from user import User


def generate_random_data(user, num_entries):
    random.seed()  # Initialize the random module
    start_date = datetime.date(2018, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    time_delta = end_date - start_date

    for _ in range(num_entries):
        if random.random() < 0.5:
            source = random.choice(user.predefined_incomes)
            amount = random.uniform(100, 1000)
            amount = round(amount / random.choice([20, 50])) * random.choice([20, 50])
            date = start_date + datetime.timedelta(days=random.randint(0, time_delta.days))
            user.add_income(source, amount, date.strftime("%Y-%m-%d"))
        else:
            category = random.choice(user.predefined_expenses)
            amount = random.uniform(10, 100)
            amount = round(amount / random.choice([20, 50])) * random.choice([20, 50])
            date = start_date + datetime.timedelta(days=random.randint(0, time_delta.days))
            user.add_expense(category, amount, date.strftime("%Y-%m-%d"))


def save_data_to_csv(user, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Source/Category", "Amount", "Date"])
        for income in user.incomes:
            writer.writerow(["Income", income.source, income.amount, str(income.date)])
        for expense in user.expenses:
            writer.writerow(["Expense", expense.category, expense.amount, str(expense.date)])


def main():
    name = input("Enter your name: ")
    user = User(name)
    num_entries = int(input("Enter the number of random entries to generate: "))
    generate_random_data(user, num_entries)
    filename = f"{name}_data.csv"
    save_data_to_csv(user, filename)
    print(f"Random data for {name} has been generated and saved to {filename}.")


if __name__ == "__main__":
    main()
