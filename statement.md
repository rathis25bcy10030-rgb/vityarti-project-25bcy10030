Student Budget Tracker: Project Statement

1. Problem Statement

University and college students often operate on tight, fixed budgets and lack effective tools to track their daily expenditures against a predetermined monthly limit. This leads to common issues such as overspending, difficulty in identifying spending patterns (e.g., excessive spending on food or non-essential items), and general financial stress due to a lack of visibility into their remaining funds. A simple, dedicated, and accessible tool is needed to provide immediate feedback and help students maintain financial discipline.

2. Scope of the Project

The project is a Desktop Budget Tracking Application built using Python (tkinter and sqlite3).

In Scope:

Setting and updating a single monthly budget limit.

Logging daily expenses with category, amount, date, and description.

Calculating and displaying the real-time remaining budget.

Providing visual alerts when the budget is running low or has been exceeded.

Storing all data persistently in a local SQLite database.

Displaying a comprehensive list of past expenses.

Out of Scope (Future Enhancements):

Multi-user functionality or cloud synchronization.

Advanced analytics (e.g., generating charts, monthly reports, trend analysis).

Handling multiple currencies or advanced financial products (investments, loans).

Integration with external bank accounts or payment services.

3. Target Users

The primary target users are university and college students who:

Are managing limited monthly funds (e.g., student loans, stipends, or parental allowance).

Need a straightforward, low-friction tool for daily expense entry.

Require immediate visibility into their financial status to prevent overspending.

May not have access to or prefer not to use complex, enterprise-level financial software.

4. High-Level Features

Feature Category

High-Level Feature

Description

Budget Management

Set Budget Limit

Allows the user to define the maximum spend for the current period (monthly).

Expense Logging

Add Transaction

Enables quick recording of new expenses with mandatory fields for amount, category, and date.

Real-time Tracking

Remaining Budget Dashboard

Dynamically calculates and displays the current amount remaining from the set budget.

Financial Alerts

Over-Limit Warning

Changes the status indicator color (e.g., to red or orange) when the spending limit is near or exceeded.

Data Persistence

Local Storage

Uses an SQLite database to ensure budget limits and transaction history are saved between sessions.

Review & History

Expense List View

Provides a table view of all logged transactions, allowing users to review their spending history.
