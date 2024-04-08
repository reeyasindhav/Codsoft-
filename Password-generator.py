import tkinter as tk
import random
import string

def generate_password():
    length = int(entry_length.get())
    if length <= 0:
        result_label.config(text="Invalid length")
        return
    else:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        result_label.config(text=f"Generated Password: {password}")

window = tk.Tk()
window.title("Password Generator")
window.geometry("300x200")
window.configure(bg="lightgray")

label_length = tk.Label(window, text="Enter Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(window)
entry_length.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="", bg="lightgray")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
