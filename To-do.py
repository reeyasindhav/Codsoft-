import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    listbox.delete(0, tk.END)

window = tk.Tk()
window.title("To-Do List")
window.geometry("300x400")
window.configure(bg="lightgray")

entry = tk.Entry(window, width=25)
entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=10)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5, pady=10)

clear_button = tk.Button(window, text="Clear All", command=clear_tasks)
clear_button.grid(row=0, column=3, padx=5, pady=10)

listbox = tk.Listbox(window, width=30, height=15)
listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL)
scrollbar.grid(row=1, column=4, sticky=tk.NS)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

window.mainloop()
