import tkinter as tk
from tkinter import messagebox
def perform_calculation():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        operation=operation_var.get()
        if operation=="Add":
            result=num1+num2
        elif operation=="Subtract":
            result=num1-num2
        elif operation=="Multiply":
            result=num1*num2
        elif operation=="Divide":
            if num2==0:
                raise ZeroDivisionError
            result=num1/num2
        else:
            result="Invalid Operation"
        label_result.config(text=f"Result:{result}",
                            fg="white",
                            font=("courier",18,"bold")
                            )
    except ValueError:
        messagebox.showerror("Input Error","Please enter valid numbers!")
    except ZeroDivisionError:
        messagebox.showerror("Math Error","Cannot divide by zero!")
window=tk.Tk()
window.title("Basic Calculator")
window.config(
    background="brown"
    )
window.geometry("1920x1200")
label1=tk.Label(
    master=window,
    text="Enter first number:",
    background="brown",
    font=("courier",18,"bold"),
    fg="white"
    )
label1.pack()
entry1=tk.Entry(
    master=window,
    font=("courier",18,"bold")
    )
entry1.pack()
label2=tk.Label(
    master=window,
    text="Enter second number:",
    background="brown",
    font=("courier",18,"bold"),
    fg="white"
    )
label2.pack()
entry2=tk.Entry(
    master=window,
    font=("courier",18,"bold")
    )
entry2.pack()

operation_var=tk.StringVar(value="Add")
operation_menu=tk.OptionMenu(window,operation_var,"Add","Subtract","Multiply","Divide")
operation_menu.pack()

button_calculate=tk.Button(
    master=window,
    text="Calculate",
    command=perform_calculation,
    font=("courier",18,"bold")
    )
button_calculate.pack()
label_result=tk.Label(
    text="Result:",
    background="brown",
    fg="white",
    font=("courier",16,"bold")
    )
label_result.pack()
label3=tk.Label(
    master=window,
    text="BASIC CALCULATOR WHICH PERFORMS YOUR SIMPLE CALCULATION...",
    background="brown",
    font=("courier",18,"bold"),
    fg="white"
    )
label3.pack()
window.mainloop()
    












            
                
                
