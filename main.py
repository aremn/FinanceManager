from user import User
from financial import Income, Expense
from file_operations import save_data, load_data
from visualization import plot_data
import os


def main(user, filename):
    try:
        while True:
            print('----------------------')
            print(f"Welcome, {user.name}!")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. Show Summary")
            print("4. Show All Incomes")
            print("5. Show All Expenses")
            print("6. Settings")
            print("7. Save and Exit")
            print('----------------------')
            choice = input("Enter your choice: ")
            if choice == "1":
                for i, income in enumerate(user.predefined_incomes, start=1):
                    print(f"{i}. {income}")
                print(f"{len(user.predefined_incomes) + 1}. New one")
                source_choice = int(input("Choose the source of income: "))
                if source_choice == len(user.predefined_incomes) + 1:
                    source = input("Enter the new source of income: ")
                else:
                    source = user.predefined_incomes[source_choice - 1]
                amount = input("Enter amount of income: ")
                try:
                    amount = float(amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
                    continue
                user.add_income(source, amount)
            elif choice == "2":
                for i, expense in enumerate(user.predefined_expenses, start=1):
                    print(f"{i}. {expense}")
                print(f"{len(user.predefined_expenses) + 1}. New one")
                category_choice = int(input("Choose the expense category: "))
                if category_choice == len(user.predefined_expenses) + 1:
                    category = input("Enter the new expense category: ")
                else:
                    category = user.predefined_expenses[category_choice - 1]
                amount = input("Enter amount of expense: ")
                try:
                    amount = float(amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
                    continue
                user.add_expense(category, amount)
            elif choice == "3":
                print(f"Total Income: {user.total_income()}")
                print(f"Total Expense: {user.total_expense()}")
                print(f"Savings: {user.savings()}")
                plot_data(user, filename)
            elif choice == "4":
                print("All Incomes:")
                for income in user.incomes:
                    print(f"{income.source}: {income.amount} ({income.date})")
            elif choice == "5":
                print("All Expenses:")
                for expense in user.expenses:
                    print(f"{expense.category}: {expense.amount} ({expense.date})")
            elif choice == "6":
                print("1. Auto")
                print("2. Manual")
                date_input_choice = input("Enter your date input choice: ")
                if date_input_choice == "1":
                    user.date_input = 'auto'
                elif date_input_choice == "2":
                    user.date_input = 'manual'
                else:
                    print("Invalid choice. Please enter again.")
            elif choice == "7":
                save_data(user, filename)
                break
            else:
                print("Invalid choice. Please enter again.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    try:
        name = input("Enter your name: ")
        user = User(name)
        filename = f"{name}_data.csv"
        if os.path.exists(filename):
            load_data(filename, user)
        main(user, filename)
    except Exception as e:
        print("An error occurred:", str(e))
