📚 Student Budget Tracker

This repository contains the code for a simple Student Budget Tracker, implemented in Python using tkinter for the Graphical User Interface (GUI) and sqlite3 for local data persistence.

The application allows students to set a monthly budget, log their expenses by category, and track their remaining budget in real-time.


✨ Features

Budget Management: Set and update a monthly spending limit.

Expense Logging: Easily record expenses with details like category, amount, date, and description.

Expense List: View a history of all logged expenses, sorted by date.

Real-time Tracking: Instantly see the remaining budget after setting a limit or adding an expense.

Visual Alerts: The remaining budget text changes color to provide visual alerts:

Green: Healthy remaining balance.

Orange: Remaining balance is less than 20% of the total budget.

Red: Budget has been exceeded (remaining balance is negative).

Local Database: Uses SQLite to store data locally, ensuring data persistence between sessions.


💻 Technology Stack

Frontend/GUI: Python's tkinter library.

Backend/Database: Python's sqlite3 library.

Language: Python 3.x


⚙️ Installation and Setup

1)Clone the Repository (or download the files):https://github.com/rathis25bcy10030-rgb/vityarti-project-25bcy10030.git

2)Prerequisites: The application only requires a standard Python 3 installation, as tkinter and sqlite3 are typically included in the standard library.

3)Run the Application: Ensure both project.py (database logic) and project2.py (GUI/main application) are in the same directory. Run the main GUI file: 

python project2.py
                                                                                                                                                          


🏗️ Application Logic Highlights

⚙️Backend.py (Database Manager)

initialize(): Creates the expenses and budget tables if they do not exist. It also ensures a default budget row (id=1) is present with a limit of 0.0.

add_expense(): Inserts a new expense record into the expenses table. (Note: The current implementation uses incorrect string formatting for the SQL query, which should be corrected to use parameter 
substitution to prevent SQL Injection.)

update() & get_budget(): Functions to manage and retrieve the single monthly budget limit.


⚙️Frontend.py (GUI & Controller)

BudgetApp.__init__: Sets up the main window, initializes the database (db.initialize()), and creates the three main frames for Budget Management, Input, and the Expense List.

set_budget(): Reads the input, validates it, and calls db.update() to set the new budget.

add_new_expense(): Reads the input fields, validates the amount, and calls db.add_expense() to log the transaction.

refresh_ui(): This is the primary controller function that:

Clears the expense list (ttk.Treeview).

Calls db.fetch_expenses() to get all data.

Populates the Treeview and calculates total_spent.

Calls db.get_budget() and calculates remaining.

Updates the Remaining label and applies the Alert Logic (color change) based on the remaining amount.

🤝 Contributing

This project is a great starting point for practicing Python GUI and database integration. Contributions or suggestions for improvements are welcome!
