import os
import json

# JSON path relative to storage.py (same folder as main.py)
FILE = os.path.join(os.path.dirname(__file__), "data", "expenses.json")

# Ensure the file exists
if not os.path.exists(FILE):
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    with open(FILE, "w") as f:
        json.dump([], f)

def get_expenses(): # returns a list of dicts of expenses and categories
    with open(FILE, "r") as f:
        data = json.load(f)
        if not data:  # True if the list is empty
            print("No expenses found.")
            return []  # return empty list so code doesn’t break
        return data
    
def save_expenses(expenses): # expects a list of dicts of expenses and categories to save in json file
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(amount, category): # expects a float amount and a string category to add to the json file
    expenses = get_expenses()
    expenses.append({"amount": amount, "category": category})
    save_expenses(expenses)
    print(f"Added: ${amount} to {category}")

def clear_expenses(): # clears all expenses from the json file
    save_expenses([])
    print("All expenses cleared.")

def get_total_expenses(): # returns the total of all expenses as a float
    expenses = get_expenses()
    return sum(e["amount"] for e in expenses)

def get_total_expenses_by_category(category): # expects a string category and returns the total of that category as a float
    expenses = get_expenses()
    return sum([e["amount"] for e in expenses if e["category"].lower() == category.lower()])