Student Budget Tracker

This is a simple, desktop-based budget tracking application designed specifically for students to manage their monthly expenses and monitor their spending against a set budget limit. The application is built using Python with the tkinter library for the graphical user interface (GUI) and sqlite3 for persistent data storage.

Features

Set Monthly Budget: Easily define or update your maximum monthly spending limit.

Log Expenses: Quickly record new expenses with category, amount, date, and a description.

Real-time Tracking: The dashboard displays the remaining budget in real-time.

Visual Alerts: The remaining budget text changes color to provide visual alerts:

Green: Budget is healthy.

Orange: Approaching the limit (less than 20% remaining).

Red: Budget exceeded (negative remaining balance).

Expense History: View a detailed, sortable list of all recorded expenses.

Persistent Storage: All data (budget limit and expenses) is saved locally in an SQLite database.

Prerequisites

To run this application, you need:

Python 3.x installed on your system.

The standard Python libraries tkinter and sqlite3, which are typically included in most Python installations.

Project Structure

The application is split into two files for better organization:

File

Role

Description

project.py

Database Manager (Backend)

Handles all interactions with the SQLite database (tracker.db). Contains functions for initialization, adding expenses, fetching history, and managing the budget limit.

project2.py

GUI & Analytics (Frontend)

Contains the BudgetApp class, which implements the tkinter GUI. It handles user input, updates the display, and calls the functions in project.py to manage data.

How to Run the Application

Save Files: Ensure both project.py and project2.py are saved in the same directory.

Execute: Run the frontend file (project2.py) from your terminal:

python project2.py


A new window titled "Student Budget Tracker" will appear.

Usage Guide

1. Set Your Monthly Budget

Locate the Budget Manager section at the top of the window.

Enter your total desired monthly spending limit (in ₹) into the text box.

Click the Set Budget button.

The Remaining balance will update immediately.

2. Log a New Expense

Navigate to the Log New Expense section.

Select a Category (Food, Travel, Fees, Stationery, Other) from the dropdown.

Enter the Amount (₹).

Enter the Date in YYYY-MM-DD format (it defaults to today's date).

Provide a short Description (e.g., "Library books," "Bus ticket").

Click the Add Expense button.

The expense will be added to the history list, and the remaining budget will be recalculated.

3. View Expense History

All logged expenses are displayed in the table below the input form. You can view the ID, Category, Amount, Date, and Description of each transaction. Data is typically displayed with the most recent entries first.

Database Schema

The application uses a local SQLite database file named tracker.db with two tables:

expenses Table

Stores individual transaction records.
| Column | Type | Description |
| :--- | :--- | :--- |
| id | INTEGER | Primary Key for the expense. |
| category | TEXT | Category of the expense (e.g., "Food"). |
| amount | REAL | The numerical cost of the expense. |
| date | TEXT | Date of the expense (YYYY-MM-DD). |
| description | TEXT | Detailed note about the expense. |

budget Table

Stores the user's defined monthly limit.
| Column | Type | Description |
| :--- | :--- | :--- |
| id | INTEGER | Always 1 (used to locate the single budget record). |
| total_limit | REAL | The maximum amount the user can spend this month. |
