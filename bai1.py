import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg

class OOP():
    def __init__(self):
        self.dk = tk.Tk()
        self.dk.title("Calculator")
        self.dk.configure(background="black")
        self.exp = ""
        self.equation = tk.StringVar()
        self.create_menu_bar()
        # Create Tabs
        self.tabControl = ttk.Notebook(self.dk)         
        self.tab1 = ttk.Frame(self.tabControl)            
        self.tabControl.add(self.tab1, text='Linear Equation')     
        self.tab2 = ttk.Frame(self.tabControl)          
        self.tabControl.add(self.tab2, text='Calculator') 
        self.tabControl.grid(row=0, column=0, padx=10, pady=10)
        # Create widgets in tabs
        self.create_linear_equation_tab()
        self.create_calculator_tab()
        self.dk.mainloop()

    def press(self, num):
        self.exp += str(num)
        self.equation.set(self.exp)

    def equalpress(self):
        try:
            total = str(eval(self.exp))
            self.equation.set(total)
            self.exp = ""
        except:
            self.equation.set("error")
            self.exp = ""

    def clear(self):
        self.exp = ""
        self.equation.set("")

    def _quit(self):
        self.dk.quit()
        self.dk.destroy()
        exit() 

    def create_menu_bar(self):
        menu_bar = Menu(self.dk)
        self.dk.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def show_about(self):
        msg.showinfo("About", "This is a simple calculator application using Tkinter.")
        
    def create_linear_equation_tab(self):
        frame = tk.LabelFrame(self.tab1, text="Phương trình: ax + b = 0")
        frame.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        # Labels and Entry for a and b
        tk.Label(frame, text="Nhập a:").grid(row=1, column=0, padx=5, pady=5)
        self.a_entry = tk.Entry(frame, width=10)
        self.a_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(frame, text="Nhập b:").grid(row=2, column=0, padx=5, pady=5)
        self.b_entry = tk.Entry(frame, width=10)
        self.b_entry.grid(row=2, column=1, padx=5, pady=5)
        self.a_entry.focus()
        # Button to solve equation
        solve_button = ttk.Button(frame, text="Solve", command=self.solve_linear_equation)
        solve_button.grid(row=3, columnspan=2, pady=10)
        # Display result
        self.result_label = tk.Label(frame, text="")
        self.result_label.grid(row=4, columnspan=2, pady=10)

    def solve_linear_equation(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            if a == 0:
                result = "Infinite solutions" if b == 0 else "No solution"
            else:
                x = -b / a
                result = f"x = {x:.2f}"
            self.result_label.config(text=result)
        except ValueError:
            msg.showerror("Input Error", "Please enter valid numbers for a and b.")
        
    def create_calculator_tab(self):
        self.equation = tk.StringVar()
        # Create a frame for the calculator
        calc_frame = tk.LabelFrame(self.tab2, text="Simple Calculator")
        calc_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        # Create entry display
        self.dis_entry = ttk.Entry(calc_frame, width=20, state="readonly", textvariable=self.equation, justify='right')
        self.dis_entry.grid(row=0, columnspan=5, ipadx=5, ipady=4)
        self.dis_entry.focus()
        # Create buttons
        # 7 8 9 
        btn7 = ttk.Button(calc_frame, text="7", width=5, command=lambda: self.press(7))
        btn7.grid(row=1, column=0, padx=2, pady=2)
        btn8 = ttk.Button(calc_frame, text="8", width=5, command=lambda: self.press(8))
        btn8.grid(row=1, column=1, padx=2, pady=2)
        btn9 = ttk.Button(calc_frame, text="9", width=5, command=lambda: self.press(9))
        btn9.grid(row=1, column=2, padx=2, pady=2)
        # - *
        btnminus = ttk.Button(calc_frame, text="-", width=5, command=lambda: self.press("-"))
        btnminus.grid(row=1, column=3, padx=2, pady=2)
        btnmulti = ttk.Button(calc_frame, text="x", width=5, command=lambda: self.press("*"))
        btnmulti.grid(row=1, column=4, padx=2, pady=2)
        # 4 5 6
        btn4 = ttk.Button(calc_frame, text="4", width=5, command=lambda: self.press(4))
        btn4.grid(row=2, column=0, ipady=2, ipadx=2)
        btn5 = ttk.Button(calc_frame, text="5", width=5, command=lambda: self.press(5))
        btn5.grid(row=2, column=1, ipady=2, ipadx=2)
        btn6 = ttk.Button(calc_frame, text="6", width=5, command=lambda: self.press(6))
        btn6.grid(row=2, column=2, ipady=2, ipadx=2) 
        # + /
        btnplus = ttk.Button(calc_frame, text="+", width=5, command=lambda: self.press("+"))
        btnplus.grid(row=2, column=3, ipady=2, ipadx=2)
        btndiv = ttk.Button(calc_frame, text="/", width=5, command=lambda: self.press("/"))
        btndiv.grid(row=2, column=4, ipady=2, ipadx=2)
        # 1 2 3 0
        btn1 = ttk.Button(calc_frame, text="1", width=5, command=lambda: self.press(1))
        btn1.grid(row=3, column=0, ipady=2, ipadx=2)
        btn2 = ttk.Button(calc_frame, text="2", width=5, command=lambda: self.press(2))
        btn2.grid(row=3, column=1, ipady=2, ipadx=2)
        btn3 = ttk.Button(calc_frame, text="3", width=5, command=lambda: self.press(3))
        btn3.grid(row=3, column=2, ipady=2, ipadx=2)
        btn0 = ttk.Button(calc_frame, text="0", width=5, command=lambda: self.press(0))
        btn0.grid(row=3, column=3, ipady=2, ipadx=2)
        # Clear button
        btnclr = tk.Button(calc_frame, text="AC",background='orange', width=5, command=self.clear)
        btnclr.grid(row=3, column=4, ipady=2, ipadx=2)
        # Equals button
        btnequal = tk.Button(calc_frame, text="=", fg='White', background='orange', width=10, command=self.equalpress)
        btnequal.grid(row=4, columnspan=5, ipady=10, ipadx=10)

if __name__ == "__main__":
    calculator = OOP()
