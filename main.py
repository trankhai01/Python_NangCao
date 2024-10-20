import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import Menu
from tkinter import messagebox as msg
from db import Database
import csv

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.config(bg="#0D92F4")
        #connect DBs
        self.db = Database("Employee", "postgres", "123456", "127.0.0.1", "5432")

        self.name = tk.StringVar()
        self.age = tk.StringVar()
        self.doj = tk.StringVar()
        self.gender = tk.StringVar()
        self.email = tk.StringVar()
        self.contact = tk.StringVar()
        self.address = tk.StringVar()
        self.search_term = tk.StringVar()

        self.create_widgets()
        self.create_menu_bar()
        self.display_employees()

    def create_widgets(self):
        # Entries Frame
        entries_frame = tk.LabelFrame(self.root, text="Employee Infomation", font=("Calibri", 18, "bold"), bg="#024CAA", fg="#C62E2E")
        entries_frame.grid(row=0, columnspan=3, padx=10, pady=20, sticky="nsew")

        # Name
        tk.Label(entries_frame, text="Name", font=("Calibri", 16), bg="#024CAA", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.name, font=("Calibri", 16), width=30).grid(row=1, column=1, padx=10, pady=10, sticky="w")
        # Age
        tk.Label(entries_frame, text="Age", font=("Calibri", 16), bg="#024CAA", fg="white").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.age, font=("Calibri", 16), width=30).grid(row=1, column=3, padx=10, pady=10, sticky="w")
        # DOJ - day of joining
        tk.Label(entries_frame, text="Start", font=("Calibri", 16), bg="#024CAA", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.doj, font=("Calibri", 16), width=30).grid(row=2, column=1, padx=10, pady=10, sticky="w")
        # Email
        tk.Label(entries_frame, text="Email", font=("Calibri", 16), bg="#024CAA", fg="white").grid(row=2, column=2, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.email, font=("Calibri", 16), width=30).grid(row=2, column=3, padx=10, pady=10, sticky="w")
        # Gender
        tk.Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#024CAA", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        combo_gender = ttk.Combobox(entries_frame, font=("Calibri ", 16), width =28, textvariable=self.gender)
        combo_gender['values'] = ('Male', 'Female')
        combo_gender.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        # Phone
        tk.Label(entries_frame, text="Phone", font=("Calibri", 16), bg="#024CAA", fg="white").grid(row=3, column=2, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.contact, font=("Calibri", 16), width=30).grid(row=3, column=3, padx=10, pady=10, sticky="w")
        # Address
        tk.Label(entries_frame, text="Address", font=("Calibri", 16), bg="#024CAA", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.address, font=("Calibri", 16), width=30).grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="w")
        #Search
        tk.Label(entries_frame, text="Search", font=("Calibri", 16), bg="#024CAA", fg="white").grid(row=4, column=2, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.search_term, font=("Calibri", 16), width=30).grid(row=4, column=3, padx=10, pady=10, sticky="w")
        
        # Buttons Frame
        buttons_frame = tk.LabelFrame(self.root,text="Actions", font=("Calibri", 18, "bold"), fg="#C62E2E", bg="#024CAA")
        buttons_frame.grid(row=1, columnspan=2, padx=10, pady=20, sticky="w")
        tk.Button(buttons_frame, text="Add Employee", font=("Calibri", 16), bg="#FF6500", fg="white", command=self.add_employee).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Button(buttons_frame, text="Update Employee", font=("Calibri", 16), bg="#535c68", fg="white", command=self.update_employee).grid(row=0, column=1, padx=10, pady=10, sticky="w")
        tk.Button(buttons_frame, text="Delete Employee", font=("Calibri", 16), bg="#535c68", fg="white", command=self.delete_employee).grid(row=0, column=2, padx=10, pady=10, sticky="w")
        tk.Button(buttons_frame, text="Clear", font=("Calibri", 16), bg="#535c68", fg="white", command=self.clear_fields).grid(row=0, column=3, padx=10, pady=10, sticky="w")
        tk.Button(buttons_frame, text="Search", font=("Calibri", 16), command=self.search_employee, bg="#535c68", fg="white").grid(row=0, column=4, padx=10, pady=10, sticky="w")
        tk.Button(buttons_frame, text="Export Data", command=self.export_data, font=("Calibri", 16), bg="#FF6500", fg="white").grid(row=0, column=5, padx=10, pady=10)
        # Treeview
        tree_frame = tk.LabelFrame(self.root, text="Employee List", font=("Calibri", 18, "bold"), bg="#024CAA", fg="#C62E2E")
        tree_frame.grid(row=3, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Age", "Day Start", "Email", "Gender", "Phone", "Address"), show="headings")
        self.tree.grid(sticky="nsew", padx=10, pady=10)
        # Thiết lập kích thước cột
        self.tree.column("ID", width=25, anchor="c")  
        self.tree.column("Name", width=150, anchor="w") 
        self.tree.column("Age", width=40, anchor="c") 
        self.tree.column("Day Start", width=80, anchor="c") 
        self.tree.column("Email", width=180, anchor="w")  
        self.tree.column("Gender", width=60, anchor="w")  
        self.tree.column("Phone", width=90, anchor="c")  
        self.tree.column("Address", width=200, anchor="w")  
        # Thiết lập tiêu đề cột
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Calibri", 15, "bold"))
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Day Start", text="Day Start")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Address", text="Address")
        self.tree.bind("<ButtonRelease-1>", self.select_item)
    
    def connect_db(self):
        if self.db is None:
            try:
                self.db = Database("Employee", "postgres", "123456", "127.0.0.1", "5432")
                msg.showinfo("Connected", "Successfully connected to the database.")
                self.display_employees()
            except Exception as e:
                msg.showerror("Error", f"Failed to connect to the database: {str(e)}")

    def _quitDB(self):
        if self.db is not None:
            self.db.close()
            msg.showinfo("Disconnected", "Successfully disconnected from the database.")
            self.db = None
            for i in self.tree.get_children():
                self.tree.delete(i)
    def _quit(self):
        self.root.quit()
        self.root.destroy()
        exit() 
    def show_about(self):
        msg.showinfo("About", "This is an Employee Management System application built using Tkinter.")

    def create_menu_bar(self):
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Connect", command=self.connect_db)
        file_menu.add_command(label="Disconnect", command=self._quitDB)
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def display_employees(self):
        # Xóa dữ liệu cũ trong Treeview
        for i in self.tree.get_children():
            self.tree.delete(i)
        employees = self.db.fetch() # Lấy dữ liệu từ database 
        employees.sort(key=lambda x: x[0])
        for employee in employees:
            self.tree.insert("", "end", values=employee)

    def search_employee(self):
        search_term = self.search_term.get().lower()
        # Xóa dữ liệu cũ trong Treeview
        for i in self.tree.get_children():
            self.tree.delete(i)
        employees = self.db.fetch() # Lấy dữ liệu từ database 
        # Lọc nhân viên theo từ khóa tìm kiếm trong bất kỳ trường nào
        filtered_employees = [
            employee for employee in employees 
            if (search_term in employee[1].lower() or  
                search_term in employee[2].lower() or  
                search_term in employee[3].lower() or  
                search_term in employee[4].lower() or  
                search_term in employee[5].lower() or  
                search_term in employee[6].lower() or 
                search_term in employee[7].lower())    
        ]
        # Hiển thị dữ liệu đã lọc
        for employee in filtered_employees:
            self.tree.insert("", "end", values=employee)
    
    def add_employee(self):
        if self.name.get() and self.age.get() and self.doj.get() and self.email.get() and self.gender.get() and self.contact.get() and self.address.get():
            self.db.insert(self.name.get(), self.age.get(), self.doj.get(), 
                           self.email.get(), self.gender.get(), self.contact.get(), 
                           self.address.get())
            msg.showinfo("Success", "Employee added successfully")
            self.clear_fields()
            self.display_employees()
        else:
            msg.showerror("Error", "All fields are required")

    def update_employee(self):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected)["values"]
            self.db.update(values[0], self.name.get(), self.age.get(), self.doj.get(),
                           self.email.get(), self.gender.get(), self.contact.get(),
                           self.address.get())
            msg.showinfo("Success", "Employee updated successfully")
            self.clear_fields()
            self.display_employees()
        else :
            msg.showerror("Error", "Select an employee to update")

    def delete_employee(self):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected)["values"]
            if msg.askyesno("Confirm Delete", f"Are you sure you want to delete {values[1]}?"):
                try:
                    self.db.delete(values[0])
                    msg.showinfo("Success", "Employee deleted successfully")
                    self.clear_fields()
                    self.display_employees()
                except Exception as e:
                    msg.showerror("Error", f"An error occurred: {str(e)}")
        else:
            msg.showerror("Error", "Select an employee to delete")

    def clear_fields(self):
        self.name.set("")
        self.age.set("")
        self.doj.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.address.set("") 
        self.search_term.set("")

    def select_item(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected)["values"]
            self.name.set(values[1])
            self.age.set(values[2])
            self.doj.set(values[3])
            self.email.set(values[4])
            self.gender.set(values[5])
            self.contact.set(values[6])
            self.address.set(values[7]) 

    def sort_by_id(self):
        for row in self.tree.get_children():
            self.tree.move(row, "end")
            self.tree.move(row, self.tree.get_children().index(row), "end")
        self.tree.sort_children(self.tree.get_children(), key=lambda x: int(self.tree.item(x, "values")[0]))

    def export_data(self, event=None):
        data = []
        for row in self.tree.get_children():
            data.append(self.tree.item(row)["values"])
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            # Write the data to the file
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Age", "Day Start", "Email", "Gender", "Phone", "Address"])
                writer.writerows(data)
            msg.showinfo("Success", "Data exported successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()