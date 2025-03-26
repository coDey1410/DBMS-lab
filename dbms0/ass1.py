import tkinter as tk
from tkinter import ttk
from datetime import datetime

def perform_operation(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "add":
            result.set(f"Result: {num1 + num2}")
        elif operation == "subtract":
            result.set(f"Result: {num1 - num2}")
    except ValueError:
        result.set("Error: Invalid input")

# Initialize main window
app = tk.Tk()
current_date = datetime.now().strftime("%Y-%m-%d")
app.title(f"ADDER AND SUBTRACTER - {current_date}")

# UI Elements
ttk.Label(app, text="Enter First Number:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry1 = ttk.Entry(app, width=20)
entry1.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(app, text="Enter Second Number:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry2 = ttk.Entry(app, width=20)
entry2.grid(row=1, column=1, padx=10, pady=5)

result = tk.StringVar()
ttk.Label(app, textvariable=result, foreground="blue").grid(row=4, column=0, columnspan=2, padx=10, pady=5)


ttk.Button(app, text="Add", command=lambda: perform_operation("add")).grid(row=2, column=0, padx=10, pady=5)
ttk.Button(app, text="Subtract", command=lambda: perform_operation("subtract")).grid(row=2, column=1, padx=10, pady=5)


ttk.Label(app, text="", width=20).grid(row=3, column=0, columnspan=2, pady=5)


app.mainloop()
