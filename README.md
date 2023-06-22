# Personal Finance Manager

## Description

Personal Finance Manager is a tool for tracking a user's income and expenses. It includes income and expense entry, analytics over a selected time period, income and expense charts, and data saving to a file.

## Installation

To install and run the Personal Finance Manager, follow these steps:

1. Clone the repository: `git clone https://github.com/aremn/ACAFinance.git`
2. Navigate to the project directory: `cd ACAFinance`
3. Run the main Python file: `python main.py`

## Usage

After running `main.py`, the program will ask for your name, then offer several options for adding income or expenses, displaying totals, and saving data.

## Contact

If you have any questions, suggestions, or issues, feel free to reach us at ncpaacbypass@gmail.com

# Documentation

## User Class

### __init__(self, name: str)
Initializes a new User object.

**Parameters:**
- name (str): The name of the user.

### add_income(self, source: str, amount: float, date: Optional[datetime.date] = None)
Adds a new income to the user's income list.

**Parameters:**
- source (str): The source of the income.
- amount (float): The amount of the income.
- date (Optional[datetime.date]): The date when the income was received. Defaults to the current date.

### add_expense(self, category: str, amount: float, date: Optional[datetime.date] = None)
Adds a new expense to the user's expense list.

**Parameters:**
- category (str): The category of the expense.
- amount (float): The amount of the expense.
- date (Optional[datetime.date]): The date when the expense was made. Defaults to the current date.

### total_income(self) -> float
Calculates the user's total income.

**Returns:** The total amount of income.

### total_expense(self) -> float
Calculates the user's total expenses.

**Returns:** The total amount of expenses.

### total_savings(self) -> float
Calculates the user's total savings (total income - total expenses).

**Returns:** The total amount of savings.

### get_expenses_summary(self) -> dict
Gets a summary of the user's expenses, grouped by category.

**Returns:** A dictionary where the keys are expense categories and the values are the total amount spent in each category.

## Income Class

### __init__(self, source: str, amount: float, date: datetime.date)
Initializes a new Income object.

**Parameters:**
- source (str): The source of the income.
- amount (float): The amount of the income.
- date (datetime.date): The date when the income was received.

### __str__(self) -> str
Returns a string representation of the Income object.

## Expense Class

### __init__(self, category: str, amount: float, date: datetime.date)
Initializes a new Expense object.

**Parameters:**
- category (str): The category of the expense.
- amount (float): The amount of the expense.
- date (datetime.date): The date when the expense was made.

### __str__(self) -> str
Returns a string representation of the Expense object.

## Functions

### is_valid_date(date_string: str) -> bool
Checks if a string can be parsed into a valid date.

**Parameters:**
- date_string (str): The string to check.

**Returns:** True if the string can be parsed into a date, False otherwise.

### parse_date(date_string: str) -> datetime.date
Parses a string into a date.

**Parameters:**
- date_string (str): The string to parse.

**Returns:** The parsed date.

### main()
The main function to start the program.

---

