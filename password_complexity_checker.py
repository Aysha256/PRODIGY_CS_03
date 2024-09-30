import re
import tkinter as tk
from tkinter import messagebox

def check_password():
    password = password_entry.get()
    
    if len(password) < 8:
        messagebox.showwarning("Weak Password", "Password must be at least 8 characters long!")
    elif not re.search("[A-Z]", password):
        messagebox.showwarning("Weak Password", "Password must contain at least one Uppercase letter.")
    elif not re.search("[a-z]", password):
        messagebox.showwarning("Weak Password", "Password must contain at least one Lowercase letter.")
    elif not re.search("[0-9]", password):
        messagebox.showwarning("Weak Password", "Password must contain at least one number.")
    else:
        messagebox.showinfo("Strong Password", "Your password is strong!")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

label = tk.Label(root, text="Enter your password:", font=("Arial", 14))
label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
password_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Password", command=check_password, font=("Arial", 12))
check_button.pack(pady=10)

root.mainloop()
