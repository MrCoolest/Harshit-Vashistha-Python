# ---notepad contain two pages
# page1                                                  page2
# wedgets                                                wedgets


# import tkinter as tk
# from tkinter import ttk

# win = tk.Tk()
# win.title('Tab control')

# nb = ttk.Notebook(win)

# page1 = ttk.Frame(nb)
# page2 = ttk.Frame(nb)
# page3 = ttk.Frame(nb)

# nb.add(page1, text='one')
# nb.add(page2, text='two')
# nb.add(page3, text='three')
# # nb.grid(row=0,column=0)
# nb.pack(expand=True, fill='both')


# label1 = ttk.Label(page1, text='This is label of page1')
# label1.grid(row=0,column=0)

# entrybox = ttk.Entry(page1, width = 17)
# entrybox.grid(row=0,column=1)
 

# label2= ttk.Label(page2, text='This is label of page2')
# label2.grid(row=0,column=0)
# entrybox2 = ttk.Entry(page2, width = 17)
# entrybox2.grid(row=0,column=1)



# my try

try :
    num = int(input("Enter number of pages you want in notebook :"))
except:
    print('please Enter number')
else:
    import tkinter as tk
    from tkinter import ttk

    win = tk.Tk()
    win.title('Tab control')

    nb = ttk.Notebook(win)
    nb.pack(expand=True, fill='both')
    for i in range(1,num+1):
        pages = 'page' + str(i)
        pages = ttk.Frame(nb)
        nb.add(pages, text=f'Page{i}')
        labels = 'label' + str(i)
        labels = ttk.Label(pages, text=f'This is label {i}')
        labels.grid(row=0,column=0)
        entrys = 'Entrybox' + str(i)
        entrys = ttk.Entry(pages, width=16)
        entrys.grid(row=0, column=1)



win.mainloop()