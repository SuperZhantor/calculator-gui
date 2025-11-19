import tkinter as tk
from tkinter import messagebox


# Password Strength Functions
def check_password_strength(password):
    strength = 0

    # Check length
    if len(password) < 8:
        strength -= 2
    elif len(password) == 8:
        strength -= 1
    else:
        strength += 2

    # Capital letter
    if any(c.isupper() for c in password):
        strength += 2
    else:
        strength -= 2

    # Lowercase letter
    if any(c.islower() for c in password):
        strength += 2
    else:
        strength -= 2

    # Digit
    if any(c.isdigit() for c in password):
        strength += 2
    else:
        strength -= 2

    # Special character
    if not password.isalnum():
        strength += 2
    else:
        strength -= 2

    # No spaces
    if " " in password:
        raise ValueError("Password shouldn't contain any spaces.")

    # Repeated characters
    unique_chars = set(password)
    for char in unique_chars:
        if password.count(char) > 3:
            strength -= 2

    # Common passwords
    common_passwords = {'password', 'qwerty', '123456', 'admin', 'abc123'}
    if password.lower() in common_passwords:
        strength -= 5

    return max(strength, 0)


# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)


# Button Logic
def on_check_password():
    password = password_entry.get()
    try:
        score = check_password_strength(password)
        if score >= 8:
            messagebox.showinfo("Result", f" Strong password! Strength: {score}")
        elif 5 < score < 8:
            messagebox.showwarning("Result", f" Medium strength password. Strength: {score}")
        else:
            messagebox.showerror("Result", f" Weak password. Strength: {score}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

check_btn = tk.Button(root, text="Check Password", command=on_check_password, font=("Arial", 10))
check_btn.pack(pady=10)

root.mainloop()
