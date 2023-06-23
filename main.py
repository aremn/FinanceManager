from user import User
from file_operations import save_data, load_data
from visualization import plot_data, monthly_totals, calculate_available_years
import os
import datetime


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
            years = calculate_available_years(user)
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
                # calculate monthly totals
                monthly_income, monthly_expense = monthly_totals(user)

                # Current month summary
                current_month = datetime.date.today().strftime('%Y-%m')
                if current_month not in monthly_income:
                    monthly_income[current_month] = 0
                if current_month not in monthly_expense:
                    monthly_expense[current_month] = 0

                print(f"This month ({current_month}):")
                print(f"Total Income: {monthly_income[current_month]}")
                print(f"Total Expense: {monthly_expense[current_month]}")
                print(f"Savings for this month: {monthly_income[current_month] - monthly_expense[current_month]}")

                # Extra menu options for 3
                while True:
                    print("1. Change month")
                    print("2. Make graphs")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == "1":
                        print(f"Available years: {years}")
                        selected_year = int(input("Enter a year: "))
                        if selected_year in years:
                            available_months = [date for date in monthly_income.keys() if
                                                str(date).startswith(str(selected_year))]
                            print(f"Available months for {selected_year}: {available_months}")
                            selected_month = input("Enter a month (yyyy-mm): ")
                            if selected_month in available_months:
                                print(f"Selected month ({selected_month}):")
                                print(f"Total Income: {monthly_income[selected_month]}")
                                print(f"Total Expense: {monthly_expense[selected_month]}")
                                print(
                                    f"Savings for this month: {monthly_income[selected_month] - monthly_expense[selected_month]}")
                            else:
                                print("Invalid month.")
                        else:
                            print("Invalid year.")
                    elif sub_choice == "2":
                        plot_data(user, filename)
                        break
                    else:
                        print("Invalid choice. Please enter again.")

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
            available_years = load_data(filename, user)
        main(user, filename)
    except Exception as e:
        print("An error occurred:", str(e))
