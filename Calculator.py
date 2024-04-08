import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Division by zero is not allowed.")
            return
    else:
        messagebox.showerror("Error", "Invalid operation.")
        return
    
    result_label.config(text=f"Result: {result}")

window = tk.Tk()
window.title("Simple Calculator")
window.configure(bg="lightblue")

# Entry widgets for numbers
entry_num1 = tk.Entry(window, width=15)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(window, width=15)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Operation selection
operation_var = tk.StringVar(window)
operation_var.set("+")  # Default operation

operation_menu = tk.OptionMenu(window, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=0, column=2, padx=10, pady=10)

# Button to perform calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Label to display result
result_label = tk.Label(window, text="Result: ", font=("Arial", 12), bg="lightblue")
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
