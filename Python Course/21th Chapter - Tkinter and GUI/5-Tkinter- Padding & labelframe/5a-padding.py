# Giving padding to code

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Loop')

# Create label
labals = ['Whats your name :', 'Whats your age :','Whats your gender :','Country :','State :','city :']
for i in range(len(labals)):
    cur_label = 'labes' + str(i)
    cur_label = ttk.Label(win, text=labals[i])
    cur_label.grid(row=i,column=0, sticky=tk.W, padx=10, pady=10)

# Create entrybox's
user_var = {'Name' : tk.StringVar(),'Age' : tk.StringVar(),'Gender' : tk.StringVar(),'Country' : tk.StringVar(),'State' : tk.StringVar(),'City' : tk.StringVar(),}
counter = 0
for i in user_var:
    cur_entry = 'entry' + i
    cur_entry = ttk.Entry(win, width=16, textvariable=user_var[i])
    cur_entry.grid(row=counter,column=1,  padx=10, pady=10)
    counter+=1

# Submint button
def Submits():
    for i in user_var:
        print(user_var.get(i).get())
submit_btn = ttk.Button(win, text='Submit', command=Submits)
submit_btn.grid(row=6,columnspan=2)

win.mainloop()