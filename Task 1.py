import tkinter as tk
from tkinter import messagebox
def add_task():
    task=entry.get()
    if task:
        tasks_listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
        print("Your task saved sucessfully...")
    else:
        messagebox.showwarning("Input Error","Please enter a Task")
window=tk.Tk()
window.title("To-Do-List")
window.config(
    background="navyblue"
    )
window.geometry("1900x1200")
    
label1=tk.Label(
    master=window,
    background="navyblue",
    text="Enter your tasks",
    font=("courier",16,"bold"),
    fg="white"
    )
label1.place(x=150,y=10)
label2=tk.Label(
    master=window,
    text="OUR BEST WISHES FOR COMPLETING YOUR TASKS...",
    font=("courier",20,"bold"),
    background="navyblue",
    fg="white"
    )
label2.place(x=250,y=350)
entry=tk.Entry(
    master=window,
    width=40,
    font=("courier",16,"bold"),
    bg="white",
    fg="black"
    )
entry.pack(pady=10)
add_button=tk.Button(
    master=window,
    text="Add Task",
    command=add_task)
add_button.pack(pady=5)
tasks_listbox=tk.Listbox(
    master=window,
    width=50
    )
tasks_listbox.pack(pady=10)
window.mainloop()
                           
