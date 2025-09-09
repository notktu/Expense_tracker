from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from storage import add_expense, get_expenses, clear_expenses, get_total_expenses, get_total_expenses_by_category

def launch_expense_tracker():

    root = tk.Tk()
    root.title("Expense Tracker")    

    def clear_tree():
        for row in tree.get_children():
            tree.delete(row)
        update_chart()

    def show_expenses():
        clear_tree()
        expenses = get_expenses()
        update_chart()
        if not expenses:
            tree.insert("", "end", values=("No expenses found", ""))
        else:
            for e in expenses:
                tree.insert("", "end", values=(f"${e['amount']:.2f}", e["category"]))

    def add_expense_ui(event=None):
        try:
            amount = float(amount_entry.get())
        except ValueError:
            set_message("Invalid amount. Please enter a valid number.")
            return "break"

        category = category_entry.get().strip()
        if not category:
            set_message("Category is required. Please enter a category.")
            return "break"

        add_expense(amount, category)
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        amount_entry.focus_set()
        show_expenses()  # refresh Treeview
        update_chart()
        return "break"

    def display_total_expenses():
        set_message(f"Total expenses: ${get_total_expenses():.2f}")

    def get_expense_of_category():
        category = category_entry.get().strip()
        if not category:
            set_message("Category is required. Please enter a category.")
            return
        if get_total_expenses_by_category(category) == 0:
            set_message(f'No expenses found for "{category}."')
            return
        set_message(f"Expenses for {category}: ${get_total_expenses_by_category(category):.2f}")
        update_chart()
        
    def clear_all_ui():
        clear_expenses()
        clear_tree()
        update_chart()
        set_message("All expenses cleared.")

    def set_message(msg):
        message_label.config(text=msg)

    # Main window
    message_label = tk.Label(root, text="", fg="blue")
    message_label.pack(pady=2)
    set_message("Welcome to Expense Tracker")

    # Input Frame
    input_frame = tk.Frame(root)
    input_frame.pack(pady=5)

    tk.Label(input_frame, text="Amount:").grid(row=0, column=0, sticky="e")
    amount_entry = tk.Entry(input_frame)
    amount_entry.grid(row=0, column=1, padx=5)

    tk.Label(input_frame, text="Category:").grid(row=1, column=0, sticky="e")
    category_entry = tk.Entry(input_frame)
    category_entry.grid(row=1, column=1, padx=5)

    # Buttons Frame
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    tk.Button(button_frame, text="Add Expense", command=add_expense_ui).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Show Expenses", command=show_expenses).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Clear All", command=clear_all_ui).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Total Expenses", command=display_total_expenses).grid(row=0, column=3, padx=5)
    tk.Button(button_frame, text="Get Expense of Category", command=get_expense_of_category).grid(row=0, column=4, padx=5)

    # Output + Chart Frame (side by side)
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # --- Left side: Treeview ---
    output_frame = tk.Frame(main_frame)
    output_frame.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(output_frame)
    scrollbar.pack(side="right", fill="y")

    columns = ("Amount", "Category")
    tree = ttk.Treeview(output_frame, columns=columns, show="headings", yscrollcommand=scrollbar.set)
    tree.heading("Amount", text="Amount")
    tree.heading("Category", text="Category")
    tree.pack(fill="both", expand=True)

    scrollbar.config(command=tree.yview)

    # --- Right side: Chart ---
    chart_frame = tk.Frame(main_frame)
    chart_frame.pack(side="right", fill="both", expand=True)

    fig = Figure(figsize=(4, 3), dpi=100)
    ax = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    def update_chart():
        ax.clear()
        expenses = get_expenses()
        if expenses:
            category_totals = {}
            for e in expenses:
                category_totals[e["category"]] = category_totals.get(e["category"].lower().strip(), 0) + e["amount"]

            labels = list(category_totals.keys())
            values = list(category_totals.values())

            ax.pie(values, labels=labels, autopct="%1.1f%%")
            ax.set_title("Expenses by Category")
        else:
            ax.text(0.5, 0.5, "no data", ha="center", va="center")

        canvas.draw()
    category_entry.bind("<Return>", lambda event: add_expense_ui())

    update_chart()  # draw the first time
    root.mainloop()

# def back_to_start(root):
#     from Login import login_ui
#     for w in root.winfo_children():
#         w.destroy()
#     login_ui(root)