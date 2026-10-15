import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")

cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        age INTEGER NOT NULL,
        phone TEXT NOT NULL,
        city TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

conn.commit()


def load_employees():
  for item in tree.get_children():
    tree.delete(item)

  cursor.execute("""
        SELECT id, fullname, age, phone, city, email
        FROM employees
        ORDER BY id
    """)

  rows = cursor.fetchall()

  for row in rows:
    tree.insert("", tk.END, values=row)


def Add_employee():
  fullname = fullname_entry.get().strip()
  age = age_entry.get().strip()
  phone = phone_entry.get().strip()
  city = city_entry.get().strip()
  email = email_entry.get().strip()

  if not fullname or not age or not phone or not city or not email:
    messagebox.showwarning("Warning", "Please fill in all fields.")
    return

  try:
    age = int(age)
    if age <= 0:
      messagebox.showerror("Error", "Age must be greater than 0.")
      return
  except ValueError:
    messagebox.showerror("Error", "Age must be a number.")
    return

  cursor.execute(
      """
        INSERT INTO employees
        (fullname, age, phone, city, email)
        VALUES (?, ?, ?, ?, ?)
    """,
      (fullname, age, phone, city, email),
  )

  conn.commit()
  messagebox.showinfo("Success", "Employee added successfully.")

  Clear_employee()
  load_employees()


def Update_employee():
  selected = tree.selection()

  if not selected:
    messagebox.showwarning("Warning", "Please select an employee.")
    return

  item = tree.item(selected[0])
  employee_id = item["values"][0]

  fullname = fullname_entry.get().strip()
  age = age_entry.get().strip()
  phone = phone_entry.get().strip()
  city = city_entry.get().strip()
  email = email_entry.get().strip()

  if not fullname or not age or not phone or not city or not email:
    messagebox.showwarning("Warning", "Please fill in all fields.")
    return

  try:
    age = int(age)
    if age <= 0:
      messagebox.showerror("Error", "Age must be greater than 0.")
      return
  except ValueError:
    messagebox.showerror("Error", "Age must be a number.")
    return

  cursor.execute(
      """
        UPDATE employees
        SET fullname = ?,
            age = ?,
            phone = ?,
            city = ?,
            email = ?
        WHERE id = ?
    """,
      (fullname, age, phone, city, email, employee_id),
  )

  conn.commit()
  messagebox.showinfo("Success", "Employee updated successfully.")

  Clear_employee()
  load_employees()


def Delete_employee():
  selected = tree.selection()

  if not selected:
    messagebox.showwarning("Warning", "Please select an employee.")
    return

  item = tree.item(selected[0])
  employee_id = item["values"][0]

  confirm = messagebox.askyesno(
      "Confirm Delete", "Are you sure you want to delete this employee?"
  )

  if confirm:
    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    conn.commit()
    messagebox.showinfo("Success", "Employee deleted successfully.")

    Clear_employee()
    load_employees()


def Clear_employee():
  fullname_entry.delete(0, tk.END)
  age_entry.delete(0, tk.END)
  phone_entry.delete(0, tk.END)
  city_entry.delete(0, tk.END)
  email_entry.delete(0, tk.END)

  for selected_item in tree.selection():
    tree.selection_remove(selected_item)


def select_employee(event):
  selected = tree.selection()
  if not selected:
    return

  item = tree.item(selected[0])
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")

cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        age INTEGER NOT NULL,
        phone TEXT NOT NULL,
        city TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

conn.commit()


def load_employees():
  for item in tree.get_children():
    tree.delete(item)

  cursor.execute("""
        SELECT id, fullname, age, phone, city, email
        FROM employees
        ORDER BY id
    """)

  rows = cursor.fetchall()

  for row in rows:
    tree.insert("", tk.END, values=row)


def Add_employee():
  fullname = fullname_entry.get().strip()
  age = age_entry.get().strip()
  phone = phone_entry.get().strip()
  city = city_entry.get().strip()
  email = email_entry.get().strip()

  if not fullname or not age or not phone or not city or not email:
    messagebox.showwarning("Warning", "Please fill in all fields.")
    return

  try:
    age = int(age)
    if age <= 0:
      messagebox.showerror("Error", "Age must be greater than 0.")
      return
  except ValueError:
    messagebox.showerror("Error", "Age must be a number.")
    return

  cursor.execute(
      """
        INSERT INTO employees
        (fullname, age, phone, city, email)
        VALUES (?, ?, ?, ?, ?)
    """,
      (fullname, age, phone, city, email),
  )

  conn.commit()
  messagebox.showinfo("Success", "Employee added successfully.")

  Clear_employee()
  load_employees()


def Update_employee():
  selected = tree.selection()

  if not selected:
    messagebox.showwarning("Warning", "Please select an employee.")
    return

  item = tree.item(selected[0])
  employee_id = item["values"][0]

  fullname = fullname_entry.get().strip()
  age = age_entry.get().strip()
  phone = phone_entry.get().strip()
  city = city_entry.get().strip()
  email = email_entry.get().strip()

  if not fullname or not age or not phone or not city or not email:
    messagebox.showwarning("Warning", "Please fill in all fields.")
    return

  try:
    age = int(age)
    if age <= 0:
      messagebox.showerror("Error", "Age must be greater than 0.")
      return
  except ValueError:
    messagebox.showerror("Error", "Age must be a number.")
    return

  cursor.execute(
      """
        UPDATE employees
        SET fullname = ?,
            age = ?,
            phone = ?,
            city = ?,
            email = ?
        WHERE id = ?
    """,
      (fullname, age, phone, city, email, employee_id),
  )

  conn.commit()
  messagebox.showinfo("Success", "Employee updated successfully.")

  Clear_employee()
  load_employees()


def Delete_employee():
  selected = tree.selection()

  if not selected:
    messagebox.showwarning("Warning", "Please select an employee.")
    return

  item = tree.item(selected[0])
  employee_id = item["values"][0]

  confirm = messagebox.askyesno(
      "Confirm Delete", "Are you sure you want to delete this employee?"
  )

  if confirm:
    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    conn.commit()
    messagebox.showinfo("Success", "Employee deleted successfully.")

    Clear_employee()
    load_employees()


def Clear_employee():
  fullname_entry.delete(0, tk.END)
  age_entry.delete(0, tk.END)
  phone_entry.delete(0, tk.END)
  city_entry.delete(0, tk.END)
  email_entry.delete(0, tk.END)

  for selected_item in tree.selection():
    tree.selection_remove(selected_item)


def select_employee(event):
  values = item["values"]

  fullname_entry.delete(0, tk.END)
  fullname_entry.insert(0, values[1])

  age_entry.delete(0, tk.END)
  age_entry.insert(0, values[2])

  phone_entry.delete(0, tk.END)
  phone_entry.insert(0, values[3])

  city_entry.delete(0, tk.END)
  city_entry.insert(0, values[4])

  email_entry.delete(0, tk.END)
  email_entry.insert(0, values[5])


def close_program():
  conn.close()
  root.destroy()


root = tk.Tk()
root.title("Employee Management System")
root.geometry("1000x650")
root.resizable(True, True)
root.configure(bg="#f4f6f8")

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Treeview.Heading",
    background="#2c3e50",
    foreground="white",
    font=("Arial", 10, "bold"),
)
style.configure("Treeview", rowheight=26, font=("Arial", 10))

title_label = tk.Label(
    root,
    text="Employee Management System",
    font=("Arial", 20, "bold"),
    bg="#f4f6f8",
    fg="#2c3e50",
)
title_label.pack(pady=15)

input_frame = tk.Frame(root, bg="#f4f6f8")
input_frame.pack(pady=10)

tk.Label(
    input_frame,
    text="Fullname:",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#2c3e50",
).grid(row=0, column=0, padx=10, pady=7, sticky="e")
fullname_entry = tk.Entry(
    input_frame, width=40, font=("Arial", 11), relief="solid", bd=1
)
fullname_entry.grid(row=0, column=1, padx=10, pady=7)

tk.Label(
    input_frame, text="Age:", font=("Arial", 11), bg="#f4f6f8", fg="#2c3e50"
).grid(row=1, column=0, padx=10, pady=7, sticky="e")
age_entry = tk.Entry(
    input_frame, width=40, font=("Arial", 11), relief="solid", bd=1
)
age_entry.grid(row=1, column=1, padx=10, pady=7)

tk.Label(
    input_frame,
    text="Phone Number:",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#2c3e50",
).grid(row=2, column=0, padx=10, pady=7, sticky="e")
phone_entry = tk.Entry(
    input_frame, width=40, font=("Arial", 11), relief="solid", bd=1
)
phone_entry.grid(row=2, column=1, padx=10, pady=7)

tk.Label(
    input_frame, text="City:", font=("Arial", 11), bg="#f4f6f8", fg="#2c3e50"
).grid(row=3, column=0, padx=10, pady=7, sticky="e")
city_entry = tk.Entry(
    input_frame, width=40, font=("Arial", 11), relief="solid", bd=1
)
city_entry.grid(row=3, column=1, padx=10, pady=7)

tk.Label(
    input_frame, text="Email:", font=("Arial", 11), bg="#f4f6f8", fg="#2c3e50"
).grid(row=4, column=0, padx=10, pady=7, sticky="e")
email_entry = tk.Entry(
    input_frame, width=40, font=("Arial", 11), relief="solid", bd=1
)
email_entry.grid(row=4, column=1, padx=10, pady=7)

button_frame = tk.Frame(root, bg="#f4f6f8")
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Add",
    width=12,
    font=("Arial", 10, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=Add_employee,
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Update",
    width=12,
    font=("Arial", 10, "bold"),
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=Update_employee,
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Delete",
    width=12,
    font=("Arial", 10, "bold"),
    bg="#e74c3c",
    fg="white",
    activebackground="#c0392b",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=Delete_employee,
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Clear",
    width=12,
    font=("Arial", 10, "bold"),
    bg="#95a5a6",
    fg="white",
    activebackground="#7f8c8d",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=Clear_employee,
).grid(row=0, column=3, padx=5)

tree_frame = tk.Frame(root, bg="#f4f6f8")
tree_frame.pack(pady=10, padx=15, fill="both", expand=True)

columns = ("ID", "Fullname", "Age", "Phone Number", "City", "Email")

tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

tree.heading("ID", text="ID")
tree.heading("Fullname", text="Fullname")
tree.heading("Age", text="Age")
tree.heading("Phone Number", text="Phone Number")
tree.heading("City", text="City")
tree.heading("Email", text="Email")

tree.column("ID", width=50, anchor="center")
tree.column("Fullname", width=180)
tree.column("Age", width=60, anchor="center")
tree.column("Phone Number", width=140)
tree.column("City", width=130)
tree.column("Email", width=220)

vertical_scrollbar = ttk.Scrollbar(
    tree_frame, orient="vertical", command=tree.yview
)
horizontal_scrollbar = ttk.Scrollbar(
    tree_frame, orient="horizontal", command=tree.xview
)

tree.configure(
    yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set
)

vertical_scrollbar.pack(side="right", fill="y")
horizontal_scrollbar.pack(side="bottom", fill="x")
tree.pack(side="left", fill="both", expand=True)

tree.bind("<ButtonRelease-1>", select_employee)
