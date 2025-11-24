# ==========================================
# MODULE 2 & 3: GUI & ANALYTICS (Frontend)
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import project as db 

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Budget Tracker")
        self.root.geometry("750x550")
        
        # 1. Initialize Database
        db.initialize()

        # Define styles
        self.bg_color = "#f9f9f9"
        self.root.configure(bg=self.bg_color)
        
        # --- FRAME 1: Budget Management (Module 1) ---
        self.frame_budget = tk.LabelFrame(root, text="Budget Manager", bg=self.bg_color, font=("Arial", 10, "bold"))
        self.frame_budget.pack(fill="x", padx=15, pady=10)

        tk.Label(self.frame_budget, text="Monthly Limit (₹):", bg=self.bg_color).pack(side="left", padx=10)
        self.entry_budget = tk.Entry(self.frame_budget, width=15)
        self.entry_budget.pack(side="left", padx=5)
        
        # NOTE: Calls your function 'update'
        tk.Button(self.frame_budget, text="Set Budget", command=self.set_budget, bg="#4CAF50", fg="white").pack(side="left", padx=10)
        
        self.lbl_remaining = tk.Label(self.frame_budget, text="Remaining: ₹0", font=("Arial", 12, "bold"), bg=self.bg_color)
        self.lbl_remaining.pack(side="right", padx=15)

        # --- FRAME 2: Add Expense (Input) (Module 2) ---
        self.frame_input = tk.LabelFrame(root, text="Log New Expense", bg=self.bg_color, font=("Arial", 10, "bold"))
        self.frame_input.pack(fill="x", padx=15, pady=5)

        # Inputs Grid
        tk.Label(self.frame_input, text="Category:", bg=self.bg_color).grid(row=0, column=0, padx=5, pady=5)
        self.combo_category = ttk.Combobox(self.frame_input, values=["Food", "Travel", "Fees", "Stationery", "Other"], state="readonly", width=12)
        self.combo_category.grid(row=0, column=1, padx=5)
        self.combo_category.current(0)

        tk.Label(self.frame_input, text="Amount (₹):", bg=self.bg_color).grid(row=0, column=2, padx=5)
        self.entry_amount = tk.Entry(self.frame_input, width=10)
        self.entry_amount.grid(row=0, column=3, padx=5)

        tk.Label(self.frame_input, text="Date (YYYY-MM-DD):", bg=self.bg_color).grid(row=0, column=4, padx=5)
        self.entry_date = tk.Entry(self.frame_input, width=15)
        self.entry_date.grid(row=0, column=5, padx=5)
        self.entry_date.insert(0, datetime.date.today())

        tk.Label(self.frame_input, text="Description:", bg=self.bg_color).grid(row=1, column=0, padx=5, pady=5)
        self.entry_desc = tk.Entry(self.frame_input, width=50)
        self.entry_desc.grid(row=1, column=1, columnspan=4, sticky="w", padx=5)

        tk.Button(self.frame_input, text="Add Expense", command=self.add_new_expense, bg="#3498db", fg="white").grid(row=1, column=5, padx=5)

        # --- FRAME 3: Expense List & Analytics (Module 3) ---
        self.tree_frame = tk.Frame(root)
        self.tree_frame.pack(fill="both", expand=True, padx=15, pady=10)

        columns = ("id", "category", "amount", "date", "description")
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show="headings", height=15)

        self.tree.heading("id", text="ID")
        self.tree.heading("category", text="Category")
        self.tree.heading("amount", text="Amount (₹)")
        self.tree.heading("date", text="Date")
        self.tree.heading("description", text="Description")

        self.tree.column("id", width=30, anchor="center")
        self.tree.column("amount", width=80, anchor="e")
        
        # Scrollbar and layout
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Load initial data
        self.refresh_ui()

    # --- Controller Methods ---
    def set_budget(self):
        """Calls your 'update' function to set the new budget."""
        try:
            amount = float(self.entry_budget.get())
            if amount < 0:
                raise ValueError
            db.update(amount)
            self.refresh_ui()
            messagebox.showinfo("Success", "Budget updated!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number.")

    def add_new_expense(self):
        """Calls your 'add_expense' function."""
        category = self.combo_category.get()
        date = self.entry_date.get()
        desc = self.entry_desc.get()
        
        try:
            amount = float(self.entry_amount.get())
            if amount <= 0:
                raise ValueError
            
            # NOTE: Calls your function 'add_expense'
            db.add_expense(category, amount, date, desc)
            
            # Clear inputs
            self.entry_amount.delete(0, tk.END)
            self.entry_desc.delete(0, tk.END)
            
            self.refresh_ui()
            
        except ValueError:
            messagebox.showerror("Error", "Invalid Amount or Date format.")

    def refresh_ui(self):
        """Fetches data and updates the expense list and dashboard status."""
        # 1. Clear Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        # 2. Populate Treeview
        # NOTE: Calls your function 'fetch_expenses'
        expenses = db.fetch_expenses()
        total_spent = 0.0
        
        for exp in expenses:
            # exp structure: (id, category, amount, date, description)
            self.tree.insert("", "end", values=exp)
            total_spent += exp[2] 

        # 3. Update Status Labels
        budget_limit = db.get_budget() # NOTE: Calls your function 'get_budget'
        remaining = budget_limit - total_spent
        
        self.entry_budget.delete(0, tk.END)
        self.entry_budget.insert(0, str(budget_limit))
        
        self.lbl_remaining.config(text=f"Remaining: ₹{remaining:.2f}")

        # Alert Logic (Module 3 - Analytics/Alerts)
        if remaining < 0:
            self.lbl_remaining.config(fg="red")
        elif remaining < (budget_limit * 0.2): 
            self.lbl_remaining.config(fg="orange")
        else:
            self.lbl_remaining.config(fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()