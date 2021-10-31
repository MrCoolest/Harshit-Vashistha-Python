# Label Frame

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Label frame')

labe_frame = ttk.LabelFrame(win, text='Details form')
labe_frame.grid(row=0,column=0, padx=50)

labals = ['Whats your name :', 'Whats your age :','Whats your gender :','Country :','State :','city :']
for i in range(len(labals)):
    cur_label = 'labes' + str(i)
    cur_label = ttk.Label(labe_frame, text=labals[i])
    cur_label.grid(row=i,column=0, sticky=tk.W) #padx=10, pady=10

user_var = {'Name' : tk.StringVar(),'Age' : tk.StringVar(),'Gender' : tk.StringVar(),'Country' : tk.StringVar(),'State' : tk.StringVar(),'City' : tk.StringVar(),}
counter = 0
for i in user_var:
    cur_entry = 'entry' + i
    cur_entry = ttk.Entry(labe_frame, width=16, textvariable=user_var[i])
    cur_entry.grid(row=counter,column=1)  #padx=10, pady=10)
    counter+=1

def Submits():
    for i in user_var:
        print(user_var.get(i).get())
submit_btn = ttk.Button(win, text='Submit', command=Submits)
submit_btn.grid(row=1,columnspan=2)

for child in labe_frame.winfo_children():
    child.grid_configure(padx=5,pady=5)


win.mainloop()