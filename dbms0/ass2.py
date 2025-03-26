import tkinter as tk
from tkinter import ttk, messagebox


DEPARTMENTS = {"CSE": "Computer Science", "ECE": "Electronics", "ME": "Mechanical", "CE": "Civil","EE": "Electrical", "IT": "Information Technology"}
STUDENTS = []  
current_page = 0  

def reset_form():
    roll_var.set("")
    name_var.set("")
    address_var.set("")
    phone_var.set("")
    dept_var.set("CSE")

def save_student():
    roll = roll_var.get().strip()
    name = name_var.get().strip()
    address = address_var.get().strip()
    phone = phone_var.get().strip()
    dept = dept_var.get().strip()

    if not roll or not name or not address or not phone or not dept:
        messagebox.showerror("Error", "All fields are required!")
        return

    if any(student["roll"] == roll and student["dept"] == dept for student in STUDENTS):
        messagebox.showerror("Error", "Roll number must be unique within the department!")
        return

    STUDENTS.append({"roll": roll, "name": name, "address": address, "phone": phone, "dept": dept})
    messagebox.showinfo("Success", "Student record saved successfully!")
    reset_form()
    display_students(0)

def search_student():
    roll = roll_var.get().strip()
    dept = dept_var.get().strip()
    student = next((s for s in STUDENTS if s["roll"] == roll and s["dept"] == dept), None)

    if student:
        name_var.set(student["name"])
        address_var.set(student["address"])
        phone_var.set(student["phone"])
        dept_var.set(student["dept"])
    else:
        messagebox.showinfo("Not Found", "No student record found with this roll number and department.")

def delete_student():
    roll = roll_var.get().strip()
    dept = dept_var.get().strip()
    global STUDENTS
    initial_len = len(STUDENTS)
    STUDENTS = [s for s in STUDENTS if not (s["roll"]==roll and s["dept"]==dept)]

    if len(STUDENTS) < initial_len:
        messagebox.showinfo("Success", "Student record deleted successfully!")
        reset_form()
        display_students(0)
    else:
        messagebox.showinfo("Not Found", "No student record found with this roll number and department.")
def cancel():
    reset_form()
    
def edit_student():
    roll = roll_var.get().strip()
    dept = dept_var.get().strip()
    student = next((s for s in STUDENTS if s["roll"] == roll and s["dept"] == dept), None)

    if student:
        student["name"] = name_var.get().strip()
        student["address"] = address_var.get().strip()
        student["phone"] = phone_var.get().strip()
        messagebox.showinfo("Success", "Student record updated successfully!")
        reset_form()
        display_students(0)
    else:
        messagebox.showinfo("Not Found", "No student record found with this roll number and department.")

def display_students(page):
    global current_page
    current_page = page

    start = page * 5
    end = start + 5
    display_box.delete(*display_box.get_children())

    for student in STUDENTS[start:end]:
        display_box.insert("", "end", values=(
            student["roll"],
            student["name"],
            DEPARTMENTS[student["dept"]],
            student["address"],
            student["phone"]
        ))

   
def validate_positive_integer(value):
    if value.isdigit() and int(value) > 0:  
        return True
    else:
        messagebox.showerror("Invalid Input", "Roll number must be a positive integer!")
        return False
def validate_phone_number(value):
    if value.isdigit() and len(value) == 10: 
        return True
    else:
        messagebox.showerror("Invalid Input", "Phone number must be exactly 10 digits!")
        return False

root = tk.Tk()
root.title("Student Management System")


roll_var = tk.StringVar()
name_var = tk.StringVar()
address_var = tk.StringVar()
phone_var = tk.StringVar()
dept_var = tk.StringVar()
dept_var.set("CSE")

# Form elements
ttk.Label(root, text="Roll Number:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
vcmd = root.register(validate_positive_integer)  
ttk.Entry(root, textvariable=roll_var, validate="focusout", validatecommand=(vcmd, '%P')).grid(row=0, column=1, padx=10, pady=5)


ttk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
ttk.Entry(root, textvariable=name_var).grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Address:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
ttk.Entry(root, textvariable=address_var).grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Phone:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
vcmd_phone = root.register(validate_phone_number)  
ttk.Entry(root, textvariable=phone_var, validate="focusout", validatecommand=(vcmd_phone, '%P')).grid(row=3, column=1, padx=10, pady=5)


ttk.Label(root, text="Department:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
ttk.OptionMenu(root, dept_var, *DEPARTMENTS.keys()).grid(row=4, column=1, padx=10, pady=5)

# Buttons
ttk.Button(root, text="Save", command=save_student).grid(row=5, column=0, padx=10, pady=10)
ttk.Button(root, text="Search", command=search_student).grid(row=5, column=1, padx=10, pady=10)
ttk.Button(root, text="Delete", command=delete_student).grid(row=6, column=0, padx=10, pady=10)
ttk.Button(root, text="Edit", command=edit_student).grid(row=6, column=1, padx=10, pady=10)
ttk.Button(root, text="Cancel",command=cancel).grid(row=8, column=2, padx=10, pady=10)

display_box = ttk.Treeview(root, columns=("Roll", "Name", "Department", "Address", "Phone"), show="headings")
display_box.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
display_box.heading("Roll", text="Roll")
display_box.heading("Name", text="Name")
display_box.heading("Department", text="Department")
display_box.heading("Address", text="Address")
display_box.heading("Phone", text="Phone")


# prev_button = ttk.Button(root, text="Prev", command=lambda: display_students(current_page - 1))
# prev_button.grid(row=8, column=0, padx=10, pady=10)
# next_button = ttk.Button(root, text="Next", command=lambda: display_students(current_page + 1))
# next_button.grid(row=8, column=1, padx=10, pady=10)


display_students(0)

root.mainloop()