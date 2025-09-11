from expenseFunctions import add_expense, get_expenses, clear_expenses, get_total_expenses, get_total_expenses_by_category
# clear_expenses()
add_expense(12.551, "Food")
add_expense(7.058, "Transport")
add_expense(20.00, "Entertainment")
for e in get_expenses():
    print(f"  ${e['amount']:.2f} - {e['category']}")
print(f"Total expenses: ${get_total_expenses():.2f}")
print(f"Food expenses: ${get_total_expenses_by_category('Food')}")
print(f"Entertainment expenses: ${get_total_expenses_by_category('Entertainment')}")

clear_expenses()
get_expenses()