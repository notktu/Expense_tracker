import tkinter as tk
from tkinter import messagebox
from expenseUI import expenseTracker
from registration import registrationUi
from accountFunctions import verify_login

def login_ui(root):
    root.title("Welcome")
    frame = tk.Frame(root)
    frame.pack(expand=True, pady=50, padx=50)

    tk.Label(frame, text="Welcome to the Expense Tracker").pack(pady=10)
        # Add login fields if needed
    tk.Label(frame, text="Username:").pack(anchor="w")
    username_entry = tk.Entry(frame)
    username_entry.pack(fill="x")

    tk.Label(frame, text="Password:").pack(anchor="w", pady=(8, 0))
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack(fill="x")

    def set_message(msg):
        message_label.config(text=msg)

    message_label = tk.Label(frame, text="", fg="blue")
    message_label.pack(pady=10)

    def attempt_login():
        u = username_entry.get()
        p = password_entry.get()
        ok, msg = verify_login(u, p)
        if ok:
            open_main_app(root)
        else:
            set_message( msg)
            if msg == "incorrect password":
                password_entry.delete(0, tk.END)
                password_entry.focus_set()
            else:  # "no such user"
                username_entry.focus_set()

    tk.Button(
        frame, 
        text="Log in", 
        command=attempt_login
    ).pack(pady=10, fill="x")

    tk.Button(
        frame,
        text="Make new account",
        command=lambda: open_registration_menu(root)
    ).pack(fill="x")
    # Press Enter to submit
    password_entry.bind("<Return>", lambda e: attempt_login())
    username_entry.focus_set()
# def opem_reg_menu(root):
#     root.destory()
#     launch_reg_menu()

def open_main_app(root):
    # for w in root.winfo_children():
    #     w.destroy()
    try:
        expenseTracker(root)   # preferred signature
    except TypeError:
        # Option B fallback: if your existing expenseTracker creates its own Tk()
        root.destroy()
        expenseTracker()


def open_registration_menu(root):
    root.withdraw()
    registrationUi(root)

if __name__ == "__main__":
    root = tk.Tk()
    login_ui(root)
    root.mainloop()
