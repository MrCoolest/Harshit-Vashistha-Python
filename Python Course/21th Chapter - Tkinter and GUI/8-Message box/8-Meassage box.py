import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mg

win = tk.Tk()
win.title('Message box')

# lable fram
labelframe = ttk.LabelFrame(win, text='Contact Detail')
labelframe.grid(row=0, column=0, padx=20, pady=20)

# labels
name_label = ttk.Label(labelframe, text='Enter your name', font=('Helvetica', 14))
age_label = ttk.Label(labelframe, text='Enter your age',font=('Helvetica', 14))

# entry_var
name_var = tk.StringVar()
age_var = tk.StringVar()

# Entry box
name_entry = ttk.Entry(labelframe, width=22, textvariable=name_var)
age_entry = ttk.Entry(labelframe, width=22, textvariable=age_var)

# grid
name_label.grid(row=0,column=0, padx=5, pady=5,sticky = tk.W)
name_entry.grid(row=1,column=0 , padx=5, pady=5, sticky = tk.W)
age_label.grid(row=0,column=1, padx=5, pady=5, sticky = tk.W)
age_entry.grid(row=1, column=1, padx=5, pady=5, sticky = tk.W)

# Submit button
def Submit():
    name = name_var.get()
    age = age_var.get()
    if name=='' or age=='':
        mg.showerror('Empty','Please fill Name & age')
    else:
        try:
            age = int(age)
        except ValueError:
            mg.showerror('Age!!','Please Enter age in Digit')
        else:
            if age <18:
                mg.showwarning('UnderAge','You are underage')
            print(f'{name} :{age}')           


Sub_btn = ttk.Button(win, width =15, text='Submit', command=Submit)
Sub_btn.grid(row=1, columnspan=2, padx=40)





win.mainloop()