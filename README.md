# Personal Finance Manager

## Description

Personal Finance Manager is a tool for tracking a user's income and expenses. It includes income and expense entry, analytics over a selected time period, income and expense charts, and data saving to a file.

## Installation

To install and run the Personal Finance Manager, follow these steps:

1. Clone the repository: `git clone https://github.com/aremn/FinanceManager.git`
2. Navigate to the project directory: `cd FinanceManager`
3. Run the main Python file: `python main.py`

## Usage

After running `main.py`, the program will ask for your name, then offer several options for adding income or expenses, displaying totals, and saving data.

## Contact

If you have any questions, suggestions, or issues, feel free to reach us at ncpaacbypass@gmail.com

# Documentation

## Module: visualization.py

This module provides functions for visualizing financial data using matplotlib and seaborn libraries.

### Functions

- `plot_data(user, filename)`: Plots various financial data for a given user based on the data loaded from a CSV file. It generates multiple visualizations, including pie charts, bar charts, scatter plots, and saving them as image files.

## Module: user.py

This module defines the User class, which represents a user with financial data.

### Classes

- `User`: Represents a user with financial data.

### Methods

- `__init__(self, name, date_input='auto')`: Initializes a User object with the given name and date input preference.
- `add_income(self, source, amount, date=None)`: Adds an income to the user's financial data.
- `add_expense(self, category, amount, date=None)`: Adds an expense to the user's financial data.
- `get_date(self)`: Prompts the user for a date and returns a valid date object.
- `total_income(self)`: Calculates the total income of the user.
- `total_expense(self)`: Calculates the total expense of the user.
- `savings(self)`: Calculates the savings of the user.
- `operation_count(self)`: Calculates the total number of operations (incomes and expenses) of the user.
- `last_operation_date(self)`: Returns the date of the last operation performed by the user.

## Module: main.py

This module is the entry point of the program and provides the main functionality.

### Functions

- `main(user, filename)`: Implements the main menu and handles user interactions with the program.

## Module: financial.py

This module defines the Income and Expense classes, representing financial transactions.

### Classes

- `Income`: Represents an income transaction.
- `Expense`: Represents an expense transaction.

### Module: file_operations.py

This module provides functions for saving and loading financial data to/from a CSV file.

### Functions

- `save_data(user, filename)`: Saves the user's financial data to a CSV file.
- `load_data(filename, user)`: Loads financial data from a CSV file and populates the user's data.


