import matplotlib.pyplot as plt
import pandas as pd
import datetime
import csv
from collections import defaultdict

def plot_data(user, filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            entry_type = row[0]
            source_category = row[1]
            amount = float(row[2])
            date_str = row[3]
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

            if entry_type == 'Income':
                user.add_income(source_category, amount, date)
            elif entry_type == 'Expense':
                user.add_expense(source_category, amount, date)

    monthly_yearly_totals = defaultdict(float)

    for income in user.incomes:
        month_year = income.date.strftime("%b-%Y")
        monthly_yearly_totals[month_year] += income.amount

    for expense in user.expenses:
        month_year = expense.date.strftime("%b-%Y")
        monthly_yearly_totals[month_year] -= expense.amount

    sorted_months = sorted(monthly_yearly_totals.keys(), key=lambda x: datetime.datetime.strptime(x, "%b-%Y"))
    years = set(income.date.year for income in user.incomes) | set(expense.date.year for expense in user.expenses)

    selected_year = input(f"Available years: {years}\nEnter a year: ")

    monthly_totals = defaultdict(float)
    for month_year in sorted_months:
        year = datetime.datetime.strptime(month_year, "%b-%Y").year
        if str(year) == selected_year:
            monthly_totals[month_year] = monthly_yearly_totals[month_year]

    fig, axs = plt.subplots(3, 2, figsize=(15, 15))

    expense_categories = set(expense.category for expense in user.expenses)
    expense_totals = defaultdict(float)
    for expense in user.expenses:
        year = expense.date.year
        if str(year) == selected_year:
            expense_totals[expense.category] += expense.amount

    axs[0, 0].pie(list(expense_totals.values()), labels=list(expense_totals.keys()), autopct='%1.1f%%')
    axs[0, 0].set_title(f'Annual Expenses by Categories - {selected_year}')

    income_sources = set(income.source for income in user.incomes)
    income_totals = defaultdict(float)
    for income in user.incomes:
        year = income.date.year
        if str(year) == selected_year:
            income_totals[income.source] += income.amount

    axs[0, 1].pie(list(income_totals.values()), labels=list(income_totals.keys()), autopct='%1.1f%%')
    axs[0, 1].set_title(f'Annual Income by Categories - {selected_year}')

    source_of_funds = defaultdict(float)
    for income in user.incomes:
        month_year = income.date.strftime("%b-%Y")
        if str(income.date.year) == selected_year:
            source_of_funds[(month_year, income.source)] += income.amount

    for expense in user.expenses:
        month_year = expense.date.strftime("%b-%Y")
        if str(expense.date.year) == selected_year:
            source_of_funds[(month_year, expense.category)] -= expense.amount

    source_of_funds_df = pd.DataFrame.from_dict(source_of_funds, orient='index').reset_index()
    source_of_funds_df[['Month', 'Source_of_Funds']] = pd.DataFrame(source_of_funds_df['index'].tolist(), index=source_of_funds_df.index)
    source_of_funds_pivot = source_of_funds_df.pivot(index='Month', columns='Source_of_Funds', values=0)

    source_of_funds_pivot.plot(kind='bar', stacked=True, ax=axs[1, 0], edgecolor='black', linewidth=0.2, width=0.6)
    axs[1, 0].set_xlabel('Month')
    axs[1, 0].set_ylabel('Source_of_Funds')
    axs[1, 0].set_title('Source_of_Funds', fontsize=20)
    axs[1, 0].legend(loc="upper right", fontsize=13)

    monthly_income = defaultdict(float)
    monthly_expense = defaultdict(float)
    for income in user.incomes:
        month_year = income.date.strftime("%b-%Y")
        if str(income.date.year) == selected_year:
            monthly_income[month_year] += income.amount

    for expense in user.expenses:
        month_year = expense.date.strftime("%b-%Y")
        if str(expense.date.year) == selected_year:
            monthly_expense[month_year] += expense.amount

    months = sorted(set(monthly_income.keys()) | set(monthly_expense.keys()))
    income_amounts = [monthly_income[month] for month in months]
    expense_amounts = [monthly_expense[month] for month in months]

    axs[1, 1].plot(months, income_amounts, marker='o', label='Income')
    axs[1, 1].plot(months, expense_amounts, marker='o', label='Expense')
    axs[1, 1].set_xlabel('Month')
    axs[1, 1].set_ylabel('Amount')
    axs[1, 1].set_title(f'Monthly Income and Expense Ratio - {selected_year}')
    axs[1, 1].legend()

    annual_saving = sum(monthly_income.values()) - sum(monthly_expense.values())
    annual_expense = sum(monthly_expense.values())

    axs[2, 0].pie([annual_saving, annual_expense], labels=['Saving', 'Expense'], autopct='%1.1f%%')
    axs[2, 0].set_title(f'Annual Saving vs Expense - {selected_year}')

    axs[2, 1].scatter(income_amounts, expense_amounts)
    axs[2, 1].set_xlabel('Income')
    axs[2, 1].set_ylabel('Expenses')
    axs[2, 1].set_title(f'Income vs Expenses - {selected_year}')
    axs[2, 1].grid(True)

    plt.tight_layout()
    plt.show()

    fig.savefig('combined_plot.png')
