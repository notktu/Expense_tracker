import tkinter as tk
from tkinter import messagebox
from accountFunctions import add_accountInfo


def registrationUi(parent):
    win = tk.Toplevel(parent)
    win.title("Create Account")

    frm = tk.Frame(win,padx = 75,pady = 75)    
    frm.pack()

    tk.Label(frm, text="Username:").pack()
    Username_entry = tk.Entry(frm)
    Username_entry.pack()

    tk.Label(frm, text="Password:").pack()
    Password_entry = tk.Entry(frm)
    Password_entry.pack()

    tk.Button(
        frm, 
        text="Create Account", 
        command=lambda: finishRegistration(win,Username_entry,Password_entry,parent)
    ).pack(pady=10)

    tk.Button(
        frm, 
        text="Go Back", 
        command=lambda: return_login(win, parent)
    ).pack(pady=10)

def finishRegistration(win,User,Pass,root):
    Username = User.get().strip()
    Password = Pass.get()
    
    if not Username or not Password:
        messagebox.showwarning("Missing info", "Please enter both username and password.")
        return

    try:
        add_accountInfo(Username, Password)  # expects two strings
    except Exception as e:
        messagebox.showerror("Error", f"Could not create account:\n{e}")
        return
    root.deiconify()   
    win.destroy()

def return_login(win, root):
    root.deiconify()   
    win.destroy()

