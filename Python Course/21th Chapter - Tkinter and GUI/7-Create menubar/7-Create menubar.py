# menubar

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Menu bar')

def Action():
    print('This is menu options')


# ------------------------------------------------Simple Menubar------------------------------------------------------------
# Menubar = tk.Menu(win)
# Menubar.add_command(label = 'Save', command=Action)
# Menubar.add_command(label = 'Save AS', command=Action)
# Menubar.add_command(label = 'Not Saved', command=Action)

# ----------------------------------------------menu list------------------------------------------------------------------
main_menu = tk.Menu(win)
file_menu = tk.Menu(main_menu, tearoff = 0)
file_menu.add_command(label='New File', command=Action)
file_menu.add_command(label='New Window', command=Action)
file_menu.add_separator()
file_menu.add_command(label='Next Page', command=Action)
file_menu.add_command(label='New Texts', command=Action)
main_menu.add_cascade(label='File', menu=file_menu)

edit_menu = tk.Menu(main_menu, tearoff = 0)
edit_menu.add_command(label='Undo', command=Action)
edit_menu.add_command(label='Redo', command=Action)
edit_menu.add_separator()
edit_menu.add_command(label='Copy', command=Action)
edit_menu.add_command(label='Past', command=Action)
main_menu.add_cascade(label='Edit', menu=edit_menu)


win.config(menu=main_menu)
# win.config(menu=Menubar)
win.mainloop()