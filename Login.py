import tkinter as tk
from expenseUI import launch_expense_tracker

def login_ui(root):
    root.title("Welcome")
    frame = tk.Frame(root)
    frame.pack(expand=True, pady=20, padx=20)

    tk.Label(frame, text="Welcome to the Expense Tracker").pack(pady=10)
        # Add login fields if needed
    tk.Label(frame, text="Username:").pack()
    username_entry = tk.Entry(frame)
    username_entry.pack()
    tk.Label(frame, text="Password:").pack()
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack()

    tk.Button(
        frame, 
        text="Log in", 
        command=lambda: open_main_app(root)
    ).pack(pady=10)

    tk.Button(
        frame,
        text="Make new account"

    ).pack(pady=10)

# def opem_reg_menu(root):
#     root.destory()
#     launch_reg_menu()

def open_main_app(root):
    root.destroy()  # Close login window
    launch_expense_tracker()  # Open the main app (modify launch_expense_tracker to create its own Tk window)

if __name__ == "__main__":
    root = tk.Tk()
    login_ui(root)
    root.mainloop()
